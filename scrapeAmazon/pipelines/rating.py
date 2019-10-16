# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import json


class Rating(object):
    def process_item(self, item, spider):

        if item.get("rating"):
            item["rating"] = float(((''.join(item["rating"][0])).split(" ", 1))[0])
        else:
            return item
        return item