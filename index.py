import tornado.web
import tornado.ioloop


class basicRequestHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello World, this is my first backend for my first python web app")


if __name__ == "__main__":
    app=tornado.web.Application([
        (r"/",basicRequestHandler)
    ])

    port=8888
    app.listen(port)
    print(f"Application is listening on port{port}")

    tornado.ioloop.IOLoop.current().start()