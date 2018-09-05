import requests
import re

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"
}

def getHTML(url):
    '''
    获取网页源码
    :param url:
    :return: HTML 源码
    '''
    try:
        response = requests.get(url, headers=headers)
        return response.content.decode('utf-8', 'ignore')
    except Exception as e:
        return "123456"

def getUrl(url):
    '''
    筛选出url
    :param url: 上一层的url
    :return:
    '''
    html = getHTML(url)

    urlre = '<a .*href=\"(https?://.*?)\" .*>'
#     预编译
    urlc = re.compile(urlre)
    # 查找全部  findall
    urlList = urlc.findall(html)
    return urlList
def getEmail():
    pass


def getMovie(url):
    # re.search('tv', url)
    pass

def deepSpider(url, depth):
    '''
    深度爬虫
    :param url: 起始url
    :param depth: 深度
    :return:
    '''
    print('\t\t\t' * depthDict[url], "已经抓取了第%d层：%s" % (depthDict[url], url))
#     超出层级退出
    if depthDict[url] >=depth:
        return

    sonUrlList = getUrl(url)
    for newUrl in sonUrlList:
        #去重
        if newUrl not in depthDict:
            #层级+1
            depthDict[newUrl] = depthDict[url] + 1
            deepSpider(newUrl, depth)


if __name__ == '__main__':
    starturl = "https://www.baidu.com/s?wd=富二代"
    depthDict = {}
    depthDict[starturl] = 1
    deepSpider(starturl, 4)