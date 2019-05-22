# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JianshubookItem(scrapy.Item):
    title = scrapy.Field()
    book_url = scrapy.Field()
    author = scrapy.Field()
    author_url = scrapy.Field()
    content = scrapy.Field()


class JianshuuserItem(scrapy.Item):
    # define the fields for your item here like:
    author = scrapy.Field()
    follow = scrapy.Field()
    fans = scrapy.Field()
    book_sum = scrapy.Field()
    book_names = scrapy.Field()

