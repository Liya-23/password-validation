import tornado.web
import tornado.ioloop

class BasicRequestHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("web/index.html")

    def post(self):
        password = self.get_argument("password")
        
        if len(password) < 12:
            self.write("Password is too short")
            
        elif not any(char.islower() for char in password):
            message ="Password should contain at least one lowercase letter"
            self.write("<p>%s</p>" % message)
            self.render("web/index.html", dynamic_content = message)
            
        elif not any(char.isupper() for char in password):
            message ="Password should contain at least one uppercase letter"
            self.write("<p>%s</p>" % message)
            self.render("web/index.html", dynamic_content = message, )
            
        elif not any(char.isdigit() for char in password):
            message ="Password should contain at least one digit"
            self.write("<p>%s</p>" % message)
            self.render("web/index.html", dynamic_content = message)
            
        elif not any(char in "!@#$%^&*()_-><.,?" for char in password):
            message ="Password should contain at least one special character"
            self.write("<p>%s</p>" % message)
            self.render("web/index.html", dynamic_content = message)
            
        else:
            message = "Password is valid"
            self.write("<p>%s</p>" % message)
            self.render("web/index.html", dynamic_content = message)

if __name__ == "__main__":
    app = tornado.web.Application([
        (r"/", BasicRequestHandler),
        (r"/web/static/(.*)", tornado.web.StaticFileHandler, {"path": "web/static"}),
        ])

    app.listen(9999)
    print("Listening on port 9999")
    tornado.ioloop.IOLoop.current().start()
