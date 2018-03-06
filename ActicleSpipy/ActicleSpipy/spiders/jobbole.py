# -*- coding: utf-8 -*-
import scrapy
from scrapy.http.response import Request
import re


class JobboleSpider(scrapy.Spider):
    name = "jobbole"
    allowed_domains = ["blog.jobbole.com"]
    start_urls = ['http://blog.jobbole.com/all-posts/']

    def parse(self, response):
    #抓取所有文章的题目，评论数，收藏数和点赞数
        # 一页的文章连接数
        article_link_list =response.css('#archive .floated-thumb a.archive-title::attr(href)').extract()
        next_page_link=response.css('.next.page-numbers::attr(href)').extract()[0]
        # article_title = response.css('#archive .floated-thumb a.archive-title::attr(title)').extract()[0]


        meta = {
            'page_num': next_page_link[-2:-1]
        }
        for url in article_link_list:
            print('url = ',url)
            yield Request(url=url, callback=self.parse_detail,meta=meta)



        # 进行翻页功能
        # print('next_page_link',next_page_link)
        i =0
        if next_page_link:
            i = i+1
            yield Request(url=next_page_link,callback=self.parse)
            if i >4:
                # 先请求前三页
                return


    def parse_detail(self,response):
        article_title = response.css('div.entry-header h1::text').extract()[0]
        # print('题目:'+article_title)
        # 文章的点赞数
        cetate_time = response.css('.status-publish .entry-meta p::text').extract()[0].strip()
        cetate_time = cetate_time.replace('·','').replace('/','-')

        praise_num = response.css('.post-adds span h10::text').extract()[0]
        page_num = response.meta['page_num']
        article_content = response.css('div.entry p').extract()

        # 职场
        comment_num = response.css('.status-publish .entry-meta p a[href="#article-comment"]::text').extract_first()
        # 1 评论
        print(comment_num)
        if comment_num:
            comment_num = re.match(r'\d*? 评论',comment_num).group(1)
        else:
            comment_num = 0
        article＿data ={
            'cetate_time':cetate_time,
            'praise_num':praise_num,
            'article_title':article_title,
            'page_num':page_num,
            'article_content':article_content,
            'comment_num' :comment_num
        }

        print(article＿data)





