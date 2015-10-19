from tornado import websocket, web, ioloop
import json

cl = []

# class IndexHandler(web.RequestHandler):
#     def get(self):
#         self.render("index.html")

class SocketHandler(websocket.WebSocketHandler):
    def check_origin(self, origin):
        return True

    def open(self):
        print "opened"
        if self not in cl:
            cl.append(self)
    def on_message(self, message):
        print 'Got :', message
        # self.write_message("Received: " + message)

    def on_close(self):
        print "closed"
        if self in cl:
            cl.remove(self)

app = web.Application([
    # (r'/', IndexHandler),
    (r'/ws', SocketHandler),
    # (r'/api', ApiHandler),
    # (r'/(favicon.ico)', web.StaticFileHandler, {'path': '../'}),
    # (r'/(rest_api_example.png)', web.StaticFileHandler, {'path': './'}),
])

if __name__ == '__main__':
    app.listen(9000)
    ioloop.IOLoop.instance().start()
