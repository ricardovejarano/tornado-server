import tornado.web
import tornado.ioloop

class serveRequestHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")

class requestHandler(tornado.web.RequestHandler):
    def get(self):
        amount = int(self.get_argument("requested_amount"))
        self.write("Value: " + str(amount))

if __name__ == "__main__":
    app = tornado.web.Application([
        (r"/", serveRequestHandler),
        (r"/request", requestHandler)
    ])

    app.listen(8881)
    print("Listening on port 8881")
    tornado.ioloop.IOLoop.current().start()
    