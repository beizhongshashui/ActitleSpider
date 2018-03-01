# -*- coding: utf-8 -*-
import scrapy


class JobboleSpider(scrapy.Spider):
    name = 'jobbole'
    allowed_domains = ['bolg.jobbole.com']
    start_urls = ['http://bolg.jobbole.com/']

    def parse(self, response):
        pass
