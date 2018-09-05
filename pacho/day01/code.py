import urllib.request
import sys
# 伪装


'''
可接收类型  Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
可接收压缩类型，做爬虫不发送这条   Accept-Encoding: gzip, deflate, br
语言   Accept-Language: zh-CN,zh;q=0.9
Cache-Control: max-age=0
连接  Connection: keep-alive
Cookie: BAIDUID=3EEFE982E25DABC6CA7336077CE5ECCF:FG=1; BIDUPSID=3EEFE982E25DABC6CA7336077CE5ECCF; PSTM=1524746754; delPer=0; BD_HOME=0; H_PS_PSSID=1453_21127_18560_26920_22157; BD_UPN=12314753
Host: www.baidu.com
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36
'''

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    # "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh,en;q=0.9,zh-CN;q=0.8",
    "Cache-Control": "max-age=0",
    "Connection": "keep-alive",
    "Cookie": "BIDUPSID=BCD315DCE8F7FF6947455A0DE12663EB; PSTM=1501484586; MCITY=-%3A; BAIDUID=2F5F2F9E96D78C3CB5613B1F94327B12:FG=1; BD_UPN=12314753; delPer=0; ispeed_lsm=26; BDRCVFR[mkUqnUt8juD]=mk3SLVN4HKm; BD_HOME=0; BDRCVFR[Elku9xRgn_n]=azWxGYybh8Rfjb3njDznj63g1NxuAT; H_PS_PSSID=",
    "Host": "www.baidu.com",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
}


# 构造一个请求体
req = urllib.request.Request('http://www.baidu.com/', headers=headers)
# 打开请求体
response = urllib.request.urlopen(req)


print(response.read().decode('utf-8'))

__version__ = '%d.%d' % sys.version_info[:2]
print(__version__)



