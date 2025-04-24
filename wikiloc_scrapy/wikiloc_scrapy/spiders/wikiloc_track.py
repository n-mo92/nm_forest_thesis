# -*- coding: utf-8 -*-
import scrapy
import json
import re
import pandas as pd


class WikilocSpiderSpider(scrapy.Spider):
    name = 'wiki_track'
    allowed_domains = ['wikiloc.com']
    start_urls = list(pd.read_csv("crawling_outputs\link-niedersachsen.csv")["Link"])

    def parse(self, response):
        # Original scraping from A.Chai-allah 
        # NM updated xpaths (31/03/2025)
        item = {}
        item['track_name'] = response.xpath('//h1/text()').extract_first().strip().replace(";",',') 
        item['url_track'] = response.url 
        item['track_type'] = response.xpath('//div[@class="view__header__breadcrumb"]/a/@title').extract_first() 
        js = json.loads(response.xpath('//script[@type="application/ld+json"]').extract()[1].replace('\n','').replace('\t','').replace('<script type="application/ld+json">','').replace('</script>',''))    
        item['date_published'] = js['datePublished']      
        item['description text'] = response.xpath('//div[@class="description dont-break-out "]/text()').extract_first() 
        Distance = response.xpath('//div[@class="d-item"]/dd/text()').extract_first() #updated xpath 31/03/2025
        # The following converts all distances to km (from miles/nautical miles)
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

        #NM: extract date recorded (08/04/2025)
        item['date_recorded'] = response.xpath('//dl[@class= "more-data"]/div[last()]/dd/text()').extract_first() 

        # NM: extract photo/waypoint captions - title and body (31/03/2025)
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
        
        # NM: Extract start coordinates and photo/waypoint coordinates (03/04/2025)
        wp_json_container = response.xpath('//div[@id="cointainer-simplecard"]')
        lat_list = []
        long_list = []
        # Extract/append trail start coordinates first so order is correct
        start_lat = js['mainEntity']['geo']['latitude']
        lat_list.append(float(start_lat))
        start_long = js['mainEntity']['geo']['longitude']
        long_list.append(float(start_long))
        # Now extract/append waypoint coordinates 
        for wp in wp_json_container:
            json_selector = wp.xpath('.//script[@type="application/ld+json"]').extract()
            for json_script in json_selector:
                wp_json = json.loads(json_script.replace('\n','').replace('\t','').replace('<script type="application/ld+json">','').replace('</script>',''))  
                lat = wp_json['geo']['latitude']
                long = wp_json['geo']['longitude']
                if lat is not None:
                    lat_list.append(float(lat))
                if long is not None:
                    long_list.append(float(long))
        # ALL lats/longs (from photo/waypoints and trail start)
        # Despite else stmnt, there should always be at least 1 lat and long (from the start coordinates)
        item['latitudes'] = lat_list if lat_list else ["None"]  
        item['longitudes'] = long_list if long_list else ["None"]  

        yield item



# Everything below has been updated, but it is not needed for my analysis
# NOTE: I removed author scraping completely (not needed and avoids any privacy issues)
# To add anything back in, make sure it comes before the "yield item" command 
"""
        item['difficulty'] = response.xpath('//div[@class="d-item big"]/dd/text()').extract_first() #updated xpath 31/03/2025
        
        vd = response.xpath('//div[@class="trail-hits"]/p/text()').extract()
        item['viewed'] = ''.join(re.findall(r'\d+',vd[0]))	
        item['downloaded'] = ''.join(re.findall(r'\d+',vd[1]))
        

"""
        
