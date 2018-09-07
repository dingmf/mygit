from django.shortcuts import render
from django.utils.deprecation import MiddlewareMixin

class MyMiddleWare(MiddlewareMixin):
    def process_request(self, req):
        ip = req.META.get("REMOTE_ADDR")
        # 白名单
        white_ips = [
            '61.144.96.111'
        ]
        if ip in white_ips:
            return render(req, 'home.html', {'data': []})

class MyWareA(MiddlewareMixin):
    def process_request(self, request):
        print("中间件1的请求")
    def process_response(self, req, response):
        print("中间件1的返回")
        return response

class My_MareB(MiddlewareMixin):
    def process_request(self, request):
        print("中间件2的请求")
    def process_response(self, request, response):
        print("中间件2的返回")
        return response

class My_Mare3(MiddlewareMixin):
    def process_request(self, request):
        print("中间件3的请求")
    def process_response(self, request, response):
        print("中间件3的返回")
        return response