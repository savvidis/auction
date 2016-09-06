#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pprint
from auctionsSp.items import *
import urlparse


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
    # custom_settings = {
    #     'ITEM_PIPELINES': {'auctionsSp.pipelines.MongoPipeline': 300}
    # }
# JsonWriterPipeline
# MongoPipeline
    # def parse(self, response):
    #     for href in response.css("div#subcategories-div > section > div > div.cat-item > a::attr('href')"):
    #         url = response.urljoin(href.extract())
    #         yield scrapy.Request(url, callback=self.parse_dir_contents)
   
    def parse(self, response):
        for i in range(2):
            url = urlparse.urljoin(response.url,'/details?id='+ str(i))
            print url
            yield scrapy.Request(url, callback=self.parse_dir_contents)
   
    def parse_dir_contents(self, response):
        item = AuctionsspItem()
        item['source'] = "Court Auctions"
        select_item = response.css('#select_asset_type>option:nth-child(1)::attr(selected)').extract();
        select_item2 = response.css('#select_asset_type>option:nth-child(2)::attr(selected)').extract();
        if not len(select_item) == 0:
            if select_item[0] == 'selected':
                item['asset_type'] = "Ακινήτα"
        elif not len(select_item2) == 0:
            if select_item2[0] == 'selected':
                item['asset_type'] = "Κινητά"
        else:
            item['asset_type'] = ""
        print response.xpath('//*[@id="debtor_name"]').extract()
        item['debtor_name'] = response.xpath('//*[@id="debtor_name"]/@value').extract_first(default='')
        item['court'] = response.xpath('//*[@id="select_court"]/@value').extract_first(default='')
        item['auctioneer'] = response.xpath('//*[@id="auctioneer"]/@value').extract_first(default='')
        item['dateTextField'] = response.xpath('//*[@id="dateTextField"]/@value').extract_first(default='')
        item['vat_number'] = response.xpath('//*[@id="vat_number"]/@value').extract_first(default='')
        item['vat_auctioneer'] = response.xpath('//*[@id="vat_auctioneer"]/@value').extract_first(default='')
        item['offer_price'] = response.xpath('//*[@id="offer_price"]/@value').extract_first(default='')
        item['publishedDateField'] = response.xpath('//*[@id="publishedDateField"]/@value').extract_first(default='')
        item['unique_code'] = response.xpath('//*[@id="guid"]/@value').extract_first(default='')
        item['auction_url'] = response.request.url

        yield item



