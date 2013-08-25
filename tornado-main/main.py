import os.path
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from tornado.options import define, options
define("port", default=8000, help="run on the given port", type=int)
class IndexHandler(tornado.web.RequestHandler):
    def get(self):
		self.render('index.html')
		
class New_AdmissionHandler(tornado.web.RequestHandler):
    def get(self):
		self.render('new_admission.html')

class PoemPageHandler(tornado.web.RequestHandler):
    def post(self):
        n1 = self.get_argument('name')
        n2= self.get_argument('passw')
        self.render('home.html', usern=n1, passw=n2)
		
if __name__ == '__main__':
	tornado.options.parse_command_line()
	app = tornado.web.Application(
	handlers=[(r'/', IndexHandler), (r'/home', PoemPageHandler),(r'/new_admission', New_AdmissionHandler)],
	template_path=os.path.join(os.path.dirname(__file__), "templates"))
	http_server = tornado.httpserver.HTTPServer(app)
	http_server.listen(options.port)
	tornado.ioloop.IOLoop.instance().start()
