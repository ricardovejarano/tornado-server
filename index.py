import tornado.web
import tornado.ioloop


def loanDesicion(amount):
    if amount > 5000:
        return "Declined"
    elif amount == 5000:
        return "Undecided"     
    else:
        return "Approved"  

   

class serveRequestHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")

class requestHandler(tornado.web.RequestHandler):
    def get(self):
        amount = int(self.get_argument("requested_amount"))
        message = loanDesicion(amount)
        response = {
            'status': 200,
            'response': str(message)
        }
        self.write(response)


      

if __name__ == "__main__":
    app = tornado.web.Application([
        (r"/", serveRequestHandler),
        (r"/request", requestHandler)
    ])

    app.listen(8881)
    print("Listening on port 8881")
    tornado.ioloop.IOLoop.current().start()
    