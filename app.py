from tornado import websocket, web, ioloop
from scapy.all import sniff
from threading import Thread
import json
import urllib2

clients = []

class SocketHandler(websocket.WebSocketHandler):
    def check_origin(self, origin):
        return True

    def open(self):
        print "opened"
        if self not in clients:
            clients.append(self)

    def on_message(self, message):
        pass

    def on_close(self):
        print "closed"
        if self in clients:
            clients.remove(self)

app = web.Application([
    (r'/ws', SocketHandler),
    (r'/(.*)', web.StaticFileHandler, {'path': './web/dist/', "default_filename": "index.html"}),
])

def send_message(message):
    for client in clients:
        # client.write_message('Test Hi ;)')
        client.write_message(message)

def get_name_by_id(id):
	get_name = json.loads(urllib2.urlopen('https://api.vk.com/method/getProfiles?uids='+str(id)).readlines()[0])
	friend_name = get_name["response"][0]["first_name"]+' '+get_name["response"][0]["last_name"]
	return friend_name

def parse_packg(pkt):
	if hasattr(pkt, "load") and '{"ts":' in pkt.load and '"updates"' in pkt.load:
		#print pkt.load.split("\r\n\r\n")[1][:-2]
		try:
			obj = json.loads(pkt.load.split("\r\n\r\n")[1][:-2])
		except:
			print "Cant parse JSON"
			obj = {"updates": []}
		for item in obj[u'updates']:
			#print item
			if item[0] == 4:
				num, uid, time, msg = item[1], item[3], item[4], item[6]
				message = {
					'user': {
						'id': uid,
						'name': get_name_by_id(uid)
					},
					'text': msg,
					'time': time,
				}
				print message
				send_message(message)




def start_sniff():
    sniff(iface='wlan0', prn=parse_packg, filter="tcp and port 80")
    pass

if __name__ == '__main__':
    app.listen(3000)
    sniffer = Thread(target = start_sniff)
    sniffer.daemon = True
    sniffer.start()
    main_loop = ioloop.IOLoop.instance().start()
