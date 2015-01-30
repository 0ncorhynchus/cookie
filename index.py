from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app


def put_cookie(handler, **kwargs):
    """
    Cookieの登録
    """
    cookie = ""
    for k, v in kwargs.items():
        cookie += k + "=" + v + ";"
    handler.response.headers.add_header('Set-Cookie', cookie)
    return cookie

def get_cookie(handler, tag):
    """
    Cookieの取得
    """
    return handler.request.cookies.get(tag, '')

def del_cookie(handler, tag):
    """
    Cookieの削除
    """
    put_cookie(handler, **{tag:""})


class MainHandler(webapp.RequestHandler):
  def get(self):
      self.response.out.write("""
      <a href="./put">Cookieの登録</a><br/>
      <a href="./get">Cookieの取得</a><br/>
      <a href="./del">Cookieの削除</a><br/>
      """)

class PutHandler(webapp.RequestHandler):
    def get(self):
        cookie = put_cookie(self, name="myname")
        self.response.out.write("以下の内容で登録しました。<br/>" + cookie)

class GetHandler(webapp.RequestHandler):
    def get(self):
        name = get_cookie(self, "name")
        self.response.out.write('name='+name)

class DelHandler(webapp.RequestHandler):
    def get(self):
        del_cookie(self, "name")
        self.response.out.write('nameを削除しました。')


# Reference: "https://cloud.google.com/appengine/docs/python/tools/webapp/"

application = webapp.WSGIApplication([
        ('/put', PutHandler),
        ('/get', GetHandler),
        ('/del', DelHandler),
        ('/.*', MainHandler)
    ])

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
