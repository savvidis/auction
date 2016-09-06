# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AuctionsspItem(scrapy.Item):
        source = scrapy.Field()
        asset_type = scrapy.Field()
        debtor_name = scrapy.Field() 
        court = scrapy.Field() 
        auctioneer = scrapy.Field()
        dateTextField = scrapy.Field() 
        vat_number = scrapy.Field() 
        debtor_name = scrapy.Field() 
        vat_auctioneer = scrapy.Field() 
        offer_price = scrapy.Field()
        publishedDateField = scrapy.Field() 
        unique_code = scrapy.Field()
        auction_url = scrapy.Field()