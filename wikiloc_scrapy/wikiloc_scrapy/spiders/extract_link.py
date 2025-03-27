# -*- coding: utf-8 -*-
import scrapy
import json
import re
from scrapy.http import Request

class WikilocSpiderSpider(scrapy.Spider):
    name = 'wiki'
    allowed_domains = ['wikiloc.com']
    start_urls = ['https://www.wikiloc.com/trails/outdoor/germany/bremen']   #your link
    #liste = [] # NM: not used?
    def parse(self, response):
        # NM: for ul added [1] to only get city filters (and not activity type filters)
        villes = response.xpath('//div[@id="filters"]/ul[1]/li/a/@href').extract()
        for v in villes :
            yield Request(v, self.parse_detail)
    def parse_detail(self, response):
        #NM: hard-code base URL
        base = 'https://www.wikiloc.com/trails/outdoor/germany/bremen' #your link
        trails = response.xpath('//ul[@class="trail-list"]/li')
        # NM: changed xpath from '//a[@class="next"]/@href'
        next = response.xpath('//a[@rel="next"]/@href').extract_first()
        for t in trails:
            # NM: changed xpath from './div/div/h3/a/@href'
            link = t.xpath('./article/div[1]/h2/a/@href').extract_first()
            if link is not None:
                item={}
                item["Link"] = link
                yield item
        if next is not None:
            # NM: adjust to use hard-coded base URL 
            next_page = base + next
            yield Request(next_page, self.parse_detail)