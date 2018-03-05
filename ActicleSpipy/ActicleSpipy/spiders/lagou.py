# -*- coding: utf-8 -*-
import scrapy


class LagouSpider(scrapy.Spider):
    name = 'lagou'
    # allowed_domains = ['www.lagou.com/']
    # start_urls = ['http://www.lagou.com/jobs/list_python']
    allowed_domains = ['www.lagou.com']
    start_urls = ['https://www.lagou.com/zhaopin/Python/?labelWords=label']

    def parse(self, response):
        print(response.body)
        # print(response.stu)

        # print(response.css("salary", ".job_request .salary::text"))
        # print(response.xpath("job_city", "//*[@class='job_request']/p/span[2]/text()"))
        # print(response.xpath("work_years", "//*[@class='job_request']/p/span[3]/text()"))
        # response.xpath("degree_need", "//*[@class='job_request']/p/span[4]/text()")
        # response.xpath("job_type", "//*[@class='job_request']/p/span[5]/text()"
        pass
