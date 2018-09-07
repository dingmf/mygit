from django.shortcuts import render
from django.utils.deprecation import MiddlewareMixin

class MyMiddleWare(MiddlewareMixin):
    def process_request(self, req):
        ip = req.META.get("REMOTE_ADDR")
        # 白名单
        white_ips = [
            # '61.144.96.111'
        ]
        if ip in white_ips:
            return render(req, 'home.html', {'data': []})

class MyWareA(MiddlewareMixin):
    def process_request(self, req):
        print("中间件1的请求")
    def process_response(self, req, response):
        print("中间件1的返回")
        print(float('10' * int(3)))
        return response

    def process_view(self, req, callback, callback_args, callback_kwargs):
        print("中间件1的view")


class MyWareB(MiddlewareMixin):
    def process_request(self, req):
        print("中间件2的请求")
    def process_response(self, req, response):
        print("中间件2的返回")
        return response
    def process_view(self, req, callback, callback_args, callback_kwargs):
        print("中间件2的view")

class MyWareC(MiddlewareMixin):
    def process_request(self, req):
        print("中间件3的请求")
    def process_response(self, req, response):
        print("中间件3的返回")
        return response
    def process_view(self, req, callback, callback_args, callback_kwargs):
        print("中间件3的view")