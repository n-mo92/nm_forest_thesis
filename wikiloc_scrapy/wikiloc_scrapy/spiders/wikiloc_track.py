# -*- coding: utf-8 -*-
import scrapy
import json
import re
import pandas as pd


class WikilocSpiderSpider(scrapy.Spider):
    name = 'wiki_track'
    allowed_domains = ['wikiloc.com']
    start_urls = list(pd.read_csv("crawling_outputs\link-bremen.csv")["Link"])

    def parse(self, response):
        item = {}
        item['track_name'] = response.xpath('//h1/text()').extract_first().strip().replace(";",',') #updated xpath 31/03/2025
        item['url_track'] = response.url 
        #item['track .gpx'] = ""	#needed?
        item['track_type'] = response.xpath('//div[@class="view__header__breadcrumb"]/a/@title').extract_first() #updated xpath 31/03/2025
        
        js = json.loads(response.xpath('//script[@type="application/ld+json"]').extract()[1].replace('\n','').replace('\t','').replace('<script type="application/ld+json">','').replace('</script>',''))    
        item['date_published'] = js['datePublished'] 
        item['date_recorded'] = response.xpath('//dl[@class= "more-data"]/div[5]/dd/text()').extract_first() #NM added 'date_recorded' item on 31/03/2025 (sometimes returns null)
        
        item['description text'] = response.xpath('//div[@class="description dont-break-out "]/text()').extract_first() #xpath updated 31/03/2025

        # NM: extract photo captions - title and body (31/03/2025)
        # Note photos are also waypoints (ie they have coordinates on the map)
        photo_container = response.xpath('//div[@id="cointainer-simplecard"]/div[@class="wpcard"]')
        caption_list = []
        for photo in photo_container:
            caption_title = photo.xpath('./div[@class="wpcard__body"]/h3/text()').extract_first()
            caption_body = photo.xpath('./div[@class="wpcard__body"]/p/text()').extract_first()
            if caption_title is not None:
                caption_list.append(caption_title)
            if caption_body is not None:
                caption_list.append(caption_body)
        item['photo_captions'] = caption_list if caption_list else ["None"]

        # NM: extract comments (31/03/2025)
        comment_section = response.xpath('//div[@id="comments"]/ul[@id="comment-list"]/li')
        comment_list = []
        for c in comment_section:
            comment = c.xpath('./div[@class="body dont-break-out"]/p/text()').extract_first()
            if comment is not None:
                comment_list.append(comment)
        item['comments'] = comment_list if comment_list else ["None"]        
        
        yield item



# Everything below has been updated, but it is not needed for my analysis
# NOTE: I removed author scraping completely (not needed and avoids any privacy issues)
# To add it back in, make sure if comes before the "yield item" command 
"""
        item['difficulty'] = response.xpath('//div[@class="d-item big"]/dd/text()').extract_first() #updated xpath 31/03/2025
        
        vd = response.xpath('//div[@class="trail-hits"]/p/text()').extract()
        item['viewed'] = ''.join(re.findall(r'\d+',vd[0]))	
        item['downloaded'] = ''.join(re.findall(r'\d+',vd[1]))
        
        Distance = response.xpath('//div[@class="d-item"]/dd/text()').extract_first() #updated xpath 31/03/2025
        # The following converts all distances to km 
        # (usually stored in miles or nautical miles)
        # and removes unit from value (NM added km to item name for clarity)
        if '.' in Distance:
            if "nautical" not in Distance:
                conv_fac = 0.621371
                d = re.findall("\d+\.\d+", Distance)[0]
                item['distance_km'] = "{:.2f}".format(float(d) / float(conv_fac))
            elif "nautical" in Distance:
                conv_fac = 0.539957
                d = re.findall("\d+\.\d+", Distance)[0]
                item['distance_km'] = "{:.2f}".format(float(d) / float(conv_fac))
        else:
            if "nautical" not in Distance:
                conv_fac = 0.621371
                d = re.findall("\d+", Distance)[0]
                item['distance_km'] = "{:.2f}".format(int(d) / float(conv_fac))
            elif "nautical" in Distance:
                conv_fac = 0.539957
                d = re.findall("\d+", Distance)[0]
                item['distance_km'] = "{:.2f}".format(int(d) / float(conv_fac))
"""
        
