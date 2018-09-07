from django.shortcuts import render
from django.utils.deprecation import MiddlewareMixin

class MyMiddleWare(MiddlewareMixin):
    def process_request(self, req):
        ip = req.META.get('REMOTE_ADDR')
        white_ips = [
            # '61.144.97.176',
            '10.3.133.119'
        ]
        if ip in white_ips:
            return render(req, 'home.html', {'data':[]})










