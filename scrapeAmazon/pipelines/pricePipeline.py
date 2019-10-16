# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import json


class Price(object):
    def process_item(self, item, spider):

        if item.get("price"):
            try:
                item["price"] = float((''.join(item["price"])).strip("$")) * 100
            except:
                return item
        else:
            return item

        return item