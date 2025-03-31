# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request

class WikilocSpiderSpider(scrapy.Spider):
    name = 'wiki'
    allowed_domains = ['wikiloc.com']
    start_urls = ['https://www.wikiloc.com/trails/outdoor/germany/bremen']   #your link
    def parse(self, response):
        villes = response.xpath('//div[@id="filters"]/ul[1]/li/a/@href').extract() #updated xpath 27/03/2025
        for v in villes :
            yield Request(v, self.parse_detail)
    def parse_detail(self, response):
        trails = response.xpath('//ul[@class="trail-list"]/li')
        next = response.xpath('//a[@rel="next"]/@href').extract_first() #updated xpath 27/03/2025      
        for t in trails:
            link = t.xpath('./article/div[1]/h2/a/@href').extract_first() #updated xpath 27/03/2025
            if link is not None:
                item={}
                item["Link"] = response.urljoin(link) #edited from link 
                yield item
        if next is not None:
            #base = response.url.split('?')[0] 
            next_page = response.urljoin(next) #edited from base + next
            yield Request(next_page, self.parse_detail)
