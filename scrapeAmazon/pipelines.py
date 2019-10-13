# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exceptions import DropItem
import json


class ScrapeamazonPipeline(object):
    def process_item(self, item, spider):
        if item.get("title"):
            item["title"] = ''.join(item["title"])

        if item.get("price"):
            item["price"] = float((''.join(item["price"])).strip("$")) * 100
        if item.get("rating"):
            item["rating"] = float(((''.join(item["rating"][0])).split(" ", 1))[0])
        if item.get("description"):
            item["description"] = ''.join(item["description"])
        if item.get("brand"):
            item["brand"] = ''.join(item["brand"])
        if item.get("asin"):
            item["asin"] = ''.join(item["url"]).split("/")[-1]

        json_dimensions = {}

        if item.get("dimensions"):
            leng = float((''.join(item["dimensions"][0]).split(" "))[0])
            json_dimensions['length'] = leng

            wid = float((''.join(item["dimensions"][0]).split(" "))[2])
            json_dimensions['width'] = wid

            hei = float((''.join(item["dimensions"][0]).split(" "))[4])
            json_dimensions['height'] = hei

            wei = float((''.join(item["dimensions"][1]).split(" ", 1))[0])
            json_dimensions['weight'] = wei

            json_dimensions = json.dumps(json_dimensions)
            item["dimensions"] = json_dimensions

        node, title = [], []

        if item.get("categories_nodes"):
            node_len = len(item["categories_nodes"])

            for i in range(node_len):
                item["categories_nodes"][i] = ((''.join(item["categories_nodes"][i])).split("="))[-1]

            for i in item["categories_nodes"]:
                node.append(i)

        if item.get("categories_titles"):
            for i in item["categories_titles"]:
                title.append(i)

        categories = [{"node": n, "title": t} for n, t in zip(node, title)]

        json.dumps(categories)

        item["categories"] = []
        item["categories"].append(categories)

        del (item["url"])
        del (item["categories_nodes"])
        del (item["categories_titles"])

        return item



