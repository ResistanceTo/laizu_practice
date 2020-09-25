#!/usr/bin/python3
# -*- encoding: utf-8 -*-
'''
@File               :tornado_test_1.py
@Instructions       :
@Date               :2020/09/25 15:25:26
@Author             :LaiZu
@Version            :
@Desc               :
'''

import tornado.ioloop
import tornado.web

PROT = 1234

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        # self.write("Hello, world")
        message = {
            "code": 200
        }
        self.finish(message)
    
    # def post(self):
    #     self.finish(message)

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])


def main():
    app = make_app()
    app.listen(PROT)
    print('监听端口：{}   http://127.0.0.1:{}/'.format(PROT, PROT))
    tornado.ioloop.IOLoop.current().start()


if __name__ == "__main__":
    main()
