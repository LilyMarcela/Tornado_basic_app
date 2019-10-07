import tornado.ioloop
import tornado.web
from tornado.web import RequestHandler
import os

class loanValueRequestHandler(tornado.web.RequestHandler):

    def set_default_headers(self):
        print( "setting headers!!!")
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "x-requested-with")
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')

    def get(self):
        value = int(self.get_argument("value"))
        def decision_maker(value):
            if value > 50000:
                return "Declined"
            elif value == 50000:
                return "Undecided"
            else:
                return "Approved"
        r = decision_maker(value)
        self.write(str(r))
        print( r )

def make_app():
    return tornado.web.Application([
        (r"/loan_response", loanValueRequestHandler)
    ], debug=True)

if __name__ == "__main__":
    app = make_app()
    port = int(os.getenv('PORT', 4200))
    app.listen(port, address='0.0.0.0')
    tornado.ioloop.IOLoop.current().start()