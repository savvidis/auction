#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pprint
from auctionsSp.items import *
import urlparse
import re
import scrapy.Spider

class MyPrettyPrinter(pprint.PrettyPrinter):
    def format(self, object, context, maxlevels, level):
        if isinstance(object, unicode):
            return (object.encode('utf8'), True, False)
        return pprint.PrettyPrinter.format(self, object, context, maxlevels, level)
pp = MyPrettyPrinter()


class CourtAuctionsSpider(scrapy.Spider):
    name = "CourtAuctions"
    allowed_domains = ["deltio.tnomik.gr"]
    start_urls = [
        "https://deltio.tnomik.gr",
    ]
   
    def parse(self, response):
        for i in range(1000):
            url = urlparse.urljoin(response.url,'/details?id='+ str(i))
            yield scrapy.Request(url, callback=self.parse_dir_contents)
   
    def parse_dir_contents(self, response):
        REstring = r'(error)'
        if re.findall(REstring, response.request.url):
            return
        else:
            item = AuctionsspItem()
            item['source'] = "deltio.tnomik.gr"

            for option in response.xpath('//select[@id="select_asset_type"]//option'):
                if not option.xpath('@selected') == []:
                    item['asset_type'] = option.xpath('text()').extract_first(default='')

            for option in response.xpath('//select[@id="select_court"]//option'):
                if not option.xpath('@selected') == []:
                    item['court'] = option.xpath('text()').extract_first(default='')

            item['auctioneer'] = response.xpath('//*[@id="auctioneer"]/@value').extract_first(default='')
            item['debtor_name'] = response.xpath('//*[@id="debtor_name"]/@value').extract_first(default='')
            item['dateTextField'] = response.xpath('//*[@id="dateTextField"]/@value').extract_first(default='')
            item['vat_number'] = response.xpath('//*[@id="vat_number"]/@value').extract_first(default='')
            item['vat_auctioneer'] = response.xpath('//*[@id="vat_auctioneer"]/@value').extract_first(default='')
            item['offer_price'] = response.xpath('//*[@id="offer_price"]/@value').extract_first(default='')
            item['publishedDateField'] = response.xpath('//*[@id="publishedDateField"]/@value').extract_first(default='')
            item['unique_code'] = response.xpath('//*[@id="guid"]/@value').extract_first(default='')
            item['auction_url'] = response.request.url

            yield item



