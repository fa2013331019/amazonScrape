# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item, Field



class ScrapeamazonItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    asin = Field()
    title = Field()
    brand = Field()
    description = Field()
    price = Field()
    prime = Field()
    dimensions = Field()
    weight = Field()
    images = Field()
    categories = Field()
    similarProducts = Field()
    rating = Field()
    url = Field()
    project = Field()
    spider = Field()
    server = Field()
    date = Field()
    length = Field()
    width = Field()
    height = Field()
    categories_titles = Field()
    categories_nodes = Field()


    pass
