# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request

class WikilocSpiderSpider(scrapy.Spider):
    name = 'wiki_large'
    allowed_domains = ['wikiloc.com']
    start_urls = ['https://www.wikiloc.com/directory/H28cj2']   # link to place list WITHIN region
    # Loop through the towns in the region
    def parse(self, response):
        towns = response.xpath('//div[@class="directory__item__list__item"]/a/@href').extract() #updated xpath 06/06/2025
        for t in towns:
            t_url = response.urljoin(t)
            yield Request(t_url, self.parse_town_page)

    # Check for activities, if present use parse_activity_trails, if not extract directly
    def parse_town_page(self, response):
        # Check if there are activity filters in the town page
        activities = response.xpath('//div[@class="activities__carousel__container"]/ul[1]/li/a/@href').extract()
        if activities:
            for a in activities:
                a_url = response.urljoin(a)
                yield Request(a_url, self.parse_activity_trails)
        else:
            # Formatting for when there only a few trails
            trails = response.xpath('//ul[@class="geo-landing__body__canonical-trails__list"]/li[@class="geo-landing__body__canonical-trails__list__items geo-landing__body__canonical-trails__list__item--other"]') #updated xpath 17/06/2025 
            for t in trails:
                link = t.xpath('./article/@data-prettyurl').extract_first() #updated xpath 17/06/2025
                if link is not None:
                    item={}
                    item["Link"] = response.urljoin(link) #edited from link 
                    yield item
            # Formatting for when there many trails
            trails_more = response.xpath('//ul[@class="landing__body__trails__list"]/li') #updated xpath 17/06/2025 
            for t in trails_more:
                link = t.xpath('./article/div[1]/h3/a/@href').extract_first() #updated xpath 17/06/2025
                if link is not None:
                    item={}
                    item["Link"] = response.urljoin(link) #edited from link 
                    yield item
            # Pagination
            next = response.xpath('//a[@rel="next"]/@href').extract_first() #updated xpath 17/06/2025
            if next is not None:
                #base = response.url.split('?')[0] 
                next_page = response.urljoin(next) #edited from base + next
                yield Request(next_page, self.parse_town_page)

    # Extract trails when sorted per activtiy
    def parse_activity_trails(self, response):
        trails = response.xpath('//ul[@class="landing__body__trails__list"]/li') #updated xpath 17/06/2025 
        next = response.xpath('//a[@rel="next"]/@href').extract_first() #updated xpath 17/06/2025      
        for t in trails:
            link = t.xpath('./article/div[1]/h3/a/@href').extract_first() #updated xpath 17/06/2025
            if link is not None:
                item={}
                item["Link"] = response.urljoin(link) #edited from link 
                yield item
        if next is not None:
            #base = response.url.split('?')[0] 
            next_page = response.urljoin(next) #edited from base + next
            yield Request(next_page, self.parse_activity_trails)
    


