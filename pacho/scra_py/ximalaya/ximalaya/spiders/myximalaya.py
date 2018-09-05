# -*- coding: utf-8 -*-
import scrapy


class MyximalayaSpider(scrapy.Spider):
    name = 'myximalaya'
    allowed_domains = ['ximalaya.com/']
    start_urls = ['https://www.ximalaya.com/youshengshu/wenxue/']

    def parse(self, response):
        xima = response.xpath('//ul[@class="xh-highlight"]')
        for xm in xima:
            ximashuming = xm.xpath('//a[@class="u0jN album-title lg xh-highlight"]/text()').extract()[0]
            print(ximashuming)
        pass
