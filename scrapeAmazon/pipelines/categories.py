# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import json


class Categories(object):
    def process_item(self, item, spider):

        node, title = [], []

        if item.get("categories_nodes"):
            node_len = len(item["categories_nodes"])

            for i in range(node_len):
                item["categories_nodes"][i] = ((''.join(item["categories_nodes"][i])).split("="))[-1]

            for i in item["categories_nodes"]:
                node.append(i)
        else:
            return item

        if item.get("categories_titles"):
            for i in item["categories_titles"]:
                title.append(i)
        else:
            return item

        categories = [{"node": n, "title": t} for n, t in zip(node, title)]

        json.dumps(categories)

        item["categories"] = []
        item["categories"].append(categories)


        return item