# -*- coding: utf-8 -*-
import scrapy


class MysinaSpider(scrapy.Spider):
    name = 'mysina'
    allowed_domains = ['sina.com.cn']
    start_urls = ['http://roll.news.sina.com.cn/news/gnxw/gdxw1/index.shtml']

    def parse(self, response):

        # 新闻列表
        newsList = response.xpath('//ul[@class="list_009"]/li')
        for news in newsList:
            # 字符串 获取真实数据
            # newsTitle = news.xpath('./a/text()').extract_first()
            # 标题
            newsTitle = news.xpath('./a/text()').extract() # 列表
            # url
            newsUrl = news.xpath('./a/@href').exteact()[0]


            print(newsTitle)
