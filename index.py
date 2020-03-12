import tornado.web
import tornado.ioloop


def loanDesicion(amount):
    numberToDecide = 5000
    if amount > numberToDecide:
        return "Declined"
    elif amount == numberToDecide:
        return "Undecided"     
    else:
        return "Approved"  

def validRequest(query):
    if (query).isdigit():
        return True
    else:
        return False    
   
class serveRequestHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")


class requestHandler(tornado.web.RequestHandler):
    def set_default_headers(self):
        print("setting headers!!!")
        self.set_header("access-control-allow-origin", "*")
        self.set_header("Access-Control-Allow-Headers", "x-requested-with")
        self.set_header('Access-Control-Allow-Methods', 'GET, PUT, DELETE, OPTIONS')
        # HEADERS!
        self.set_header("Access-Control-Allow-Headers", "access-control-allow-origin,authorization,content-type") 


    def get(self):
        canContinue = validRequest(self.get_argument("requested_amount"))
        if canContinue:
            amount = int(self.get_argument("requested_amount"))
            message = loanDesicion(amount)
            response = {
                'status': 200,
                'response': str(message)
            }
            self.write(response)
        else:
            responseError = {
                'status': 400,
                'response': 'Bad request'
            }
            self.write(responseError)

if __name__ == "__main__":
    app = tornado.web.Application([
        (r"/", serveRequestHandler),
        (r"/request", requestHandler)
    ])

    app.listen(8881)
    print("Listening on port 8881")
    tornado.ioloop.IOLoop.current().start()
    