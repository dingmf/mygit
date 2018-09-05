# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class WeixiItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    # 微信公众号
    wecharPublicNum = scrapy.Field()
    # 昵称
    wecharNickname = scrapy.Field()
    # 文章标题
    articleTitle = scrapy.Field()
    # 发布日期
    pubTime = scrapy.Field()
    # 二维码
    QRcode = scrapy.Field()

    pass
