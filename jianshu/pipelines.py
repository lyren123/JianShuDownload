# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from pymongo import MongoClient
client = MongoClient()
collections = client["jianshu"]["js"]

class JianshuPipeline(object):
    def process_item(self, item, spider):
        # print(item)
        # 将数据存储到mongodb数据库中
        collections.insert_one(dict(item))
        print(item)
        return item
