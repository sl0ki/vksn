from tornado import websocket, web, ioloop
from scapy.all import sniff
from threading import Thread

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

class IndexHandler(web.RequestHandler):
    def get(self):
        self.render('./web/dist/index.html')

app = web.Application([
    (r'/', IndexHandler),
    (r'/ws', SocketHandler),
    (r'/(.*)', web.StaticFileHandler, {'path': './web/dist/'}),
])

def send_message(raw='Empty'):
    for client in clients:
        # client.write_message('Test Hi ;)')
        client.write_message({
            'user': {
                'name': 'Username',
                'raw': raw
            },
            'text': 'Some text here i = '
        })

def parse_packg(pack):
    print pack.show()
    # send_message('Good')

def start_sniff():
    sniff(iface='eth0', prn=parse_packg, filter="port 80")
    pass

if __name__ == '__main__':
    app.listen(3000)
    sniffer = Thread(target = start_sniff)
    sniffer.daemon = True
    sniffer.start()
    main_loop = ioloop.IOLoop.instance().start()
