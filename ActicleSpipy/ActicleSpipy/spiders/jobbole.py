# -*- coding: utf-8 -*-
import scrapy
from scrapy.http.response import Request


class JobboleSpider(scrapy.Spider):
    name = "jobbole"
    allowed_domains = ["http://blog.jobbole.com/"]
    start_urls = ['http://blog.jobbole.com/all-posts/']

    def parse(self, response):
    #抓取所有文章的题目，评论数，收藏数和点赞数

        # 一页的文章连接数
        article_link_list =response.css('#archive .floated-thumb a.archive-title::attr(href)').extract()
        next_page_link=response.css('.next.page-numbers::attr(href)').extract()

        for url in article_link_list:

            yield Request(url=url, callback=self.parse_detail)

        meta ={
            'data':'parse_data'
        }

        # 进行翻页功能
        if next_page_link:
            yield Request(url=next_page_link,callback=self.parse,meta=meta)


    def parse_detail(self,response):
        article_title = response.css('div.entry-header h1::text').extract()[0]
        # 文章的点赞数
        praise_num = response.css('.post-adds span h10::text').extract()[0]


        data = response.meta['data']




