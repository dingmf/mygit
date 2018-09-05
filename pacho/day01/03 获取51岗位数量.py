import re
import urllib
from urllib import request, parse

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.5712.400 QQBrowser/10.2.1957.400'
}


# https://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E6%B7%B1%E5%9C%B3&kw=python
def getJobNum(jl, kw):
    '''
    获取岗位数量
    :param jl: 地区
    :param kw: 关键字
    :return: 岗位数量
    '''

    # url编码
    search = {'jl': jl, 'kw': kw}
    search = urllib.parse.urlencode(search)

    url = 'http://sou.zhaopin.com/jobs/searchresult.ashx?' + search
    req = urllib.request.Request(url, headers=headers)

    response = urllib.request.urlopen(req)

    html = response.read().decode('utf-8')
    # print(html)

    jobre = '<em>(\d+)</em>'
    jobnum = re.findall(jobre, html)[0]
    print(jobnum)


if __name__ == '__main__':
    getJobNum(jl='广州', kw='python')