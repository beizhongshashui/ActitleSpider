# -*- coding: utf-8 -*-
import scrapy
from scrapy.http.response import Request


class JobboleSpider(scrapy.Spider):
    name = "jobbole"
    allowed_domains = ["blog.jobbole.com"]
    start_urls = ['http://blog.jobbole.com/all-posts/']

    def parse(self, response):
    #抓取所有文章的题目，评论数，收藏数和点赞数

        # 一页的文章连接数
        article_link_list =response.css('#archive .floated-thumb a.archive-title::attr(href)').extract()
        next_page_link=response.css('.next.page-numbers::attr(href)').extract()[0]

        meta = {
            'data': 'parse_data'
        }
        for url in article_link_list:
            print('url = ',url)
            yield Request(url=url, callback=self.parse_detail,meta=meta)



        # 进行翻页功能
        # print('next_page_link',next_page_link)
        if next_page_link:
            yield Request(url=next_page_link,callback=self.parse)


    def parse_detail(self,response):
        article_title = response.css('div.entry-header h1::text').extract()[0]
        # print('题目:'+article_title)
        # 文章的点赞数
        praise_num = response.css('.post-adds span h10::text').extract()[0]
        data = response.meta['data']

        article＿data ={
            'article_title':article_title,
            'praise_num':praise_num,
            'data':data
        }

        print(article＿data)





