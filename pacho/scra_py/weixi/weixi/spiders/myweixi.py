# -*- coding: utf-8 -*-
import scrapy


class MyweixiSpider(scrapy.Spider):
    name = 'myweixi'
    # allowed_domains = ['weixin.sogou.com/','mp.weixin.qq.com/']
    start_urls = ['http://weixin.sogou.com/pcindex/pc/pc_0/1.html']

    def parse(self, response):
        # print(response.text)

        publicNumList = response.xpath('//div[@class="txt-box"]')
        for wx in publicNumList:
            # 微信公众号
            # wecharPublicNum = wx.xpath('.//div[@class="s-p"]/a/text()').extract()[0]
            # 昵称
            wecharPublicNumurl = wx.xpath('.//div[@class="s-p"]/a/@href').extract()[0]

            # 构建请求
            yield scrapy.Request(url=wecharPublicNumurl,callback=self.get_weicharPublic)

            # # 文章标题
            # articleTitle = wx.xpath()
            # # 发布日期
            # pubTime = wx.xpath()
            # # 二维码
            # QRcode = wx.xpath()

            print(wecharPublicNumurl)

        pass

    def get_weicharPublic(self,response):
        '''
        获取公众号
        :param response:
        :return:
        '''
        # 公众号
        wecharPublicNum = response.xpath('//p[@class="profile_account"]/text()').extract()[0]

        # 昵称
        wecharPublicNickname = response.xpath('//strong[@class="profile_nickname"]').extract()[0]
        print(wecharPublicNum)