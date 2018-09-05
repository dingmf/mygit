import urllib.request
import urllib.parse

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
}
def getWD(wd):
    '''
    浏览器 可搜索
    :param wd:
    :return: 响应
    '''
    # url编码
    wd = urllib.parse.urlencode({"wd":wd})
    print(wd)
    # 解码
    print(urllib.parse.unquote(wd))


    url = 'https://www.baidu.com/s?' + wd

    requset = urllib.request.Request(url, headers=headers)
    response = urllib.request.urlopen(requset)

    print(response.read().decode('utf-8'))


if __name__ == '__main__':
    wd = input("请问你要查什么：")

    getWD(wd)