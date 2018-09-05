import requests
import lxml
from lxml import etree
import json
import time

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"
}


def getHouseInfo(url):
    '''
    获取房子信息
    :param url:页数url
    :return:
    '''
    # url = "https://gz.lianjia.com/ershoufang/pg1/"

    response = requests.get(url, headers=headers)
    # print(pesponse.text)

    mytree = lxml.etree.HTML(response.text)
    #房子列表
    hourseList = mytree.xpath('.//ul[@class="sellListContent"]/li')

    for hourse in hourseList:
        # 图片
        hourseImg = hourse.xpath('./a/img/@data-original')[0]
        # 标题
        houseAlt = hourse.xpath('./a/img/@alt')[0]
        # 位置
        houseAddress = hourse.xpath('./div[1]/div[2]/div/a/text()')[0] + hourse.xpath('./div[1]/div[2]/div/text()')[0]
        # 楼层 小区
        positionInfo = hourse.xpath('./div[1]/div[3]/div/text()')[0] + hourse.xpath('./div[1]/div[3]/div/a/text()')[0]
        # 关注 发布
        hoursefabu = hourse.xpath('./div[1]/div[4]/text()')[0]
        # 标签
        hoursebiaoqian = hourse.xpath('.//span[@class="subway"]/text()') + hourse.xpath('.//span[@class="taxfree"]/text()') + hourse.xpath('.//span[@class="haskey"]/text()')
        biaoqian = (''.join(hoursebiaoqian))
        # 总价
        totalPrice = hourse.xpath('./div[1]/div[6]/div[1]/span/text()')[0] + "万"
        # 单价
        unitPrice = hourse.xpath('./div[1]/div[6]/div[2]/span/text()')[0]
        print(hourseImg,houseAlt,houseAddress,positionInfo,hoursefabu,biaoqian,totalPrice,unitPrice)

def getPage(url):
    '''
    获取页数
    :param url: 城市url
    :return: 页数
    '''
    response = requests.get(url, headers=headers)
    mytree = lxml.etree.HTML(response.text)
    print(response.text)
    # 页数
    page = mytree.xpath('//div[@class="page-box house-lst-page-box"]/@page-data')[0]
    totaPage = int(json.loads(page)['totalPage'])
    print(totaPage)
    return totaPage

if __name__ == '__main__':
    time.clock()
    url = "https://gz.lianjia.com/ershoufang/pg1/"
    totalPage = getPage(url)

    for i in range(1,11):
        url = "https://gz.lianjia.com/ershoufang/pg%d/" % (i)
        getHouseInfo(url)
    print(time.clock())