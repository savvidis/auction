# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field


class AuctionsspItem(Item):
        source = Field()
        asset_type = Field()
        debtor_name = Field()
        court = Field()
        auctioneer = Field()
        dateTextField = Field()
        vat_number = Field()
        debtor_name = Field()
        vat_auctioneer = Field()
        offer_price = Field()
        publishedDateField = Field()
        unique_code = Field()
        auction_url = Field()


class GeneralSpider(Item):
        source = Field()
