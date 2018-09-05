import urllib
from urllib import request,parse

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"
}

loginurl = 'http://www.renren.com/PLogin.do'

data = {
    'email':'18879007132',
    'password':'dmf978228'
}

data = urllib.parse.urlencode(data).encode('utf-8')
req = urllib.request.Request(loginurl, data=data, headers=headers)

response = urllib.request.urlopen(req)

print(response.read().decode('utf-8'))