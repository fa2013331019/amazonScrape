# -*- coding: utf-8 -*-
import scrapy
from scrapeAmazon.items import ScrapeamazonItem
from scrapy.loader.processors import MapCompose, Join
from scrapy.loader import ItemLoader
from w3lib.html import replace_escape_chars, remove_tags
import json
import datetime
import socket
import urllib



class BasicSpider(scrapy.Spider):
    name = 'basic'
    allowed_domains = ['amazon']
    start_urls = ['https://www.amazon.com/dp/B004CNH98C']

    def parse(self, response):
        l = ItemLoader(item=ScrapeamazonItem(), response=response)

        l.default_output_processor = MapCompose(lambda v: v.strip(), replace_escape_chars)

        l.add_xpath('title', 'normalize-space(//span[@id="productTitle"]/text())')
        l.add_xpath('brand', '//a[@id="bylineInfo"]/text()')
        l.add_xpath('description', 'normalize-space(//div[@id="productDescription"]/p/text())')
        l.add_xpath('price', '//span[@id="priceblock_ourprice"]/text()')
        #l.add_xpath('dimensions', '//td[@class="a-size-base"][0]/text()')
        l.add_xpath('dimensions', '//td[@class="a-size-base"]/text()')
        l.add_xpath('images', '//span[@class="a-button-inner"]/span[@class="a-button-text"]/img/@src')
        l.add_xpath('categories_titles', '//li/span[@class="a-list-item"]/a[contains(@class,"a-color-tertiary")]/text()')
        l.add_xpath('categories_nodes', '//li/span[@class="a-list-item"]/a[contains(@class,"a-color-tertiary")]/@href')
        l.add_xpath('similarProducts', '//th/@data-asin')
        l.add_xpath('rating', '//span[@id="acrPopover"][1]/@title')


        #Housekeeping fields
        l.add_value('url', response.url)
        #l.add_value('project', self.settings.get('BOT_NAME'))
        #l.add_value('spider', self.name)
        #l.add_value('server', socket.gethostname())
        #l.add_value('date', datetime.datetime.now())

        data = l.load_item()

        data["price"] = float((''.join(data["price"])).strip("$")) * 100
        data["title"] = ''.join(data["title"])
        data["rating"] = float(((''.join(data["rating"][0])).split(" ", 1))[0])
        data["description"] = ''.join(data["description"])
        data["brand"] = ''.join(data["brand"])
        data["asin"] = ''.join(data["url"]).split("/")[-1]
        leng = float((''.join(data["dimensions"][0]).split(" "))[0])
        wid = float((''.join(data["dimensions"][0]).split(" "))[2])
        hei = float((''.join(data["dimensions"][0]).split(" "))[4])
        wei = float((''.join(data["dimensions"][1]).split(" ", 1))[0])
        json_dimensions = {}
        json_dimensions['weight'] = wei
        json_dimensions['length'] = leng
        json_dimensions['width'] = wid
        json_dimensions['height'] = hei
        json_dimensions = json.dumps(json_dimensions)
        data["dimensions"] = json_dimensions

        node_len = len(data["categories_nodes"])

        for i in range(node_len):
            data["categories_nodes"][i] = ((''.join(data["categories_nodes"][i])).split("="))[-1]

        node, title = [], []

        for i in data["categories_nodes"]:
            node.append(i)

        for i in data["categories_titles"]:
            title.append(i)

        categories = [{"node": n, "title": t} for n, t in zip(node, title)]

        json.dumps(categories)

        data["categories"] = []
        data["categories"].append(categories)

        del(data["url"])
        del(data["categories_nodes"])
        del(data["categories_titles"])

        return data
