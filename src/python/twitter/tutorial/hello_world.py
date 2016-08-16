from twitter.common import app

import psutil
import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
  def get(self):
    ##self.write('<pre>Running pids:\n%s</pre>' % '\n'.join(map(str, psutil.get_pid_list())))
    self.write('Hello world')

def main():
    application = tornado.web.Application([
      (r"/", MainHandler)
    ])
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()

app.main()
