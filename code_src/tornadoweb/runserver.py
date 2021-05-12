"""
:author: subofrank
:date: 12/5/2021
:description: for example gin web server get/post
"""
import tornado.gen
import tornado.httpclient
import tornado.ioloop
import tornado.web
import json
class ComperforLocal(tornado.web.RequestHandler):
    def get(self):
        self.set_header("Content-Type", 'application/json')
        print(f"g.")
        self.write(json.dumps({"name":"tornado"}))

    def post(self):
        self.set_header("Content-Type", 'application/json')
        print(f"p+")
        self.write(json.dumps({"name":"tornado port"}))

def define_url(port):
    active_port = port
    application = tornado.web.Application([
        (r"/user", ComperforLocal),
    ],
    )
    application.listen(active_port)
    print(f"server start at port:{active_port}")
    tornado.ioloop.IOLoop.instance().start()


if __name__ == '__main__':
    define_url(8009)