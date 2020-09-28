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
        message = {
            "code": 200,
            "text": "get"
        }
        print(self.request)
        self.write(message)
    
    def post(self):
        print(self.request)
        # params
        print(self.request.query_arguments)
        # data
        print(self.request.body_arguments)
        message = {
            "code": 200,
            "text": "post"
        }
        self.finish(message)

def make_app():
    settings = {
        # 给cookie添加一个秘钥
        # Tornado 支持通过 set_secure_cookie 和 get_secure_cookie 方法对cookie签名
        "cookie_secret": "__TODO:_GENERATE_YOUR_OWN_RANDOM_VALUE_HERE__",
        "login_url": "/login",
        "xsrf_cookies": True
    }

    return tornado.web.Application([
        (r"/", MainHandler),
    ], **settings)


def main():
    app = make_app()
    app.listen(PROT)
    print('监听端口：{}  http://127.0.0.1:{}/'.format(PROT, PROT))
    tornado.ioloop.IOLoop.current().start()


if __name__ == "__main__":
    main()
