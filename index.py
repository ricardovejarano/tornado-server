import tornado.web
import tornado.ioloop

class basicRequestHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Tornado Server")

if __name__ == "__main__":
    app = tornado.web.Application([
        (r"/", basicRequestHandler)
    ])

    app.listen(8881)
    print("Listening on port 8881")
    tornado.ioloop.IOLoop.current().start()
    