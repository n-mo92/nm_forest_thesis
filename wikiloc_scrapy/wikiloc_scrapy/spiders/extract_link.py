# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request

class WikilocSpiderSpider(scrapy.Spider):
    name = 'wiki'
    allowed_domains = ['wikiloc.com']
    start_urls = ['https://www.wikiloc.com/trails/outdoor/germany/bavaria']   #your link
    # Loop through the activity types
    def parse(self, response):
        activities = response.xpath('//div[@class="activities__carousel__container"]/ul[1]/li/a/@href').extract() #updated xpath 06/06/2025
        for a in activities:
            yield Request(a, self.parse_detail)
    # Extract the trail links, allowing for pagination
    def parse_detail(self, response):
        trails = response.xpath('//ul[@class="landing__body__trails__list"]/li') #updated xpath 06/06/2025 
        next = response.xpath('//a[@rel="next"]/@href').extract_first() #updated xpath 06/06/2025      
        for t in trails:
            link = t.xpath('./article/div[1]/h3/a/@href').extract_first() #updated xpath 06/06/2025
            if link is not None:
                item={}
                item["Link"] = response.urljoin(link) #edited from link 
                yield item
        if next is not None:
            #base = response.url.split('?')[0] 
            next_page = response.urljoin(next) #edited from base + next
            yield Request(next_page, self.parse_detail)


