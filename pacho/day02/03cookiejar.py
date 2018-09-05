import requests

def getHtml():
    '''
    获取网页源码
    :param  url
    :return: tml源码
    '''

def getUrl():
    '''
    筛选url
    :param:url上一层url
    :return:
    '''
    getHtml()




def deepSpider(url,depth):
    '''
    深度爬虫
    :param starturl: 起始url
    :param depth: 深度
    :return:
    '''
    print('\t\t\t'*depthDict[url],"已经抓取了第%d层：%s"% (depthDict[url]))

    if depthDict[url] > depth:
        return

    sonUrlList = getUrl(url)
    deepSpider(url, depth)

if __name__ == '__main__':
    # 起始url
    staturl = ""
    # 层级控制{"url": "层级"}
    depthDict = {}

    depthDict[staturl] = 1
    deepSpider(staturl,4)
