# -*- coding: utf-8 -*-
import scrapy
import re
from tianya.tianya.items import TianyaItem

class MytianyaSpider(scrapy.Spider):
    name = 'mytianya' #爬虫名 不能为空
    allowed_domains = ['bbs.tianya.cn'] # 允许爬取的域名
    start_urls = ['http://bbs.tianya.cn/post-140-393973-1.shtml'] #开始url

    # 爬虫逻辑
    def parse(self, response):

        # 邮箱正则
        emailRe = "[a-z0-9_]+@[a-z0-9]+\.[a-z]{2,4}"
        print("====================================================")
        # print(response.text)
        html = response.body.decode('utf-8')

        emailLsit = re.findall(emailRe, html, re.I)
        # print(emailLsit)

        item = TianyaItem() #实例
        # 当作字典
        item["email"] = emailLsit
        #返回你的存储对象
        for e in emailLsit:
            item["email"] = e.strip()
            yield item

        # 使用return 不会经过pipelines
        # return item