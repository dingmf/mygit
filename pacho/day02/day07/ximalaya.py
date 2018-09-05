import requests
import lxml
from lxml import etree

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"
}


def getYeshu(url):
    '''
    获取页数
    :param url:
    :return:
    '''
    # url = "https://www.ximalaya.com/youshengshu/wenxue/p1/"
    response = requests.get(url, headers=headers).content.decode('utf-8')
    mytree = lxml.etree.HTML(response)

    totalYeshu = mytree.xpath('//*[@id="root"]/main/section/div/div/div[3]/div/div/div[3]/nav/ul/li[7]/a/span/text()')[0]
    print(totalYeshu)

    return totalYeshu

def getxima(url):
    response = requests.get(url, headers=headers)
    html = response.content.decode('utf-8')
    mytree = lxml.etree.HTML(html)

    ximaList = mytree.xpath('//*[@id="root"]/main/section/div/div/div[3]/div/div/div[2]/ul/li')
    for xmly in ximaList:
        ximashuming = xmly.xpath('./div/a[1]/@title')[0]
        ximashumingurl = "https://www.ximalaya.com" + xmly.xpath('./div/a[1]/@href')[0]


        print(ximashuming,ximashumingurl)
    return ximashumingurl

def getzhanghui(url):
    '''
    获取章回
    :param url:
    :return:
    '''
    response = requests.get(url, headers=headers).content.decode('utf-8')
    mytree = lxml.etree.HTML(response)

    # 书名
    shuming = mytree.xpath('//*[@id="root"]/main/section/div/div[2]/div[1]/div[1]/div[2]/div[2]/h1/text()')[0]
    # 简介
    jianjie = mytree.xpath('//article[@class="vd4u intro"]/p/text()')
    # jianjie = mytree.xpath('//*[@id="root"]/main/section/div/div[2]/div[1]/div[1]/div[3]/article/text()')
    # print(shuming, ','.join(jianjie))

    # 章回
    zhanghui = mytree.xpath('//div[@class="dOi2 sound-list"]/ul/li/div[2]/a')
    for zh in zhanghui:
        zhangjie = zh.xpath('./text()')[0]
        zhangjieurl = "https://www.ximalaya.com" + zh.xpath('./@href')[0]
        print(zhangjie,zhangjieurl)


    # # zhuanghuiList = mytree.xpath('//*[@id="root"]/main/section/div/div[2]/div[1]')
    # # for zh in zhuanghuiList:
    #     # 书名
    #     shuming = zh.xpath('//h1[@class="vd4u title xh-highlight"]/text()')[0]
    #     # 简介
    #     # jianjie = zh.xpath('//article[@class="vd4u intro"]/p[1]/text()') + zh.xpath('//article[@class="vd4u intro"]/p[1]/br/text()') + zh.xpath('//article[@class="vd4u intro"]/p[2]/text()') + zh.xpath('//article[@class="vd4u intro"]/p[3]/text()')
    #     # 章回
    #
    #     print(shuming)

if __name__ == '__main__':
    ximaUrl = 'https://www.ximalaya.com/youshengshu/wenxue/'
    for i in range(1, int(getYeshu(ximaUrl)) + 1):
        url = "https://www.ximalaya.com/youshengshu/wenxue/p%d/" % i
        newurl = getxima(url)
        print(newurl)
        getzhanghui(newurl)

