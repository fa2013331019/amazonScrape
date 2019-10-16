# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import json


class Dimensions(object):
    def process_item(self, item, spider):

        json_dimensions = {}

        if item.get("dimensions"):
            try:
                leng = float((''.join(item["dimensions"][0]).split(" "))[0])
                json_dimensions['length'] = leng
            except:
                return item

            try:
                wid = float((''.join(item["dimensions"][0]).split(" "))[2])
                json_dimensions['width'] = wid
            except:
                return item

            try:
                hei = float((''.join(item["dimensions"][0]).split(" "))[4])
                json_dimensions['height'] = hei
            except:
                return item

            try:
                wei = float((''.join(item["dimensions"][1]).split(" ", 1))[0])
                json_dimensions['weight'] = wei
            except:
                return item

            json_dimensions = json.dumps(json_dimensions)
            item["dimensions"] = json_dimensions
        else:
            return item

        return item