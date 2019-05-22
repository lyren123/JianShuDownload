# -*- coding: utf-8 -*-
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Rule
from JianShuDownload.jianshu import JianshubookItem,JianshuuserItem
from scrapy_redis.spiders import RedisCrawlSpider



class JsSpider(RedisCrawlSpider):
    name = 'js'
    allowed_domains = ['jianshu.com']
    # start_urls = ['http://jianshu.com/']
    redis_key = "jianshu"

    rules = (
        # 链接提取器提取书本详情页
        Rule(LinkExtractor(allow=r'/p/[a-b0-9]*'), callback='parse_item', follow=True),
        # 链接提取器提取作者个人信息页
        Rule(LinkExtractor(allow=r'/u/[a-b0-9]*'), callback='parse_author'),

    )

    def parse_item(self, response):
        item = JianshubookItem()
        item["title"] = response.xpath("//h1/text()").extract_first()
        item["book_url"] = response.url.split("?")[0]
        item["author"] = response.xpath("//div[@class='author']/div/span/a/text()").extract_first()
        item["author_url"] = response.xpath("//div[@class='author']/div/span/a/@href").extract_first()
        item["content"] = response.xpath("//div[@class='show-content-free']//p//text()").extract()
        yield item

    def parse_author(self,response):
        item = JianshuuserItem()
        item["author"] = response.xpath("//div[@class='title']/a/text()").extract_first()
        item["follow"] ="".join([i.strip() for i in response.xpath("//div[@class='info']/ul/li[1]/div/a/p/text()").extract_first()])
        item["fans"] = response.xpath("//div[@class='info']/ul/li[2]/div/a/p/text()").extract_first()
        item["book_sum"] = response.xpath("//div[@class='info']/ul/li[3]/div/a/p/text()").extract_first()
        item["book_names"] = response.xpath("//ul[@class='note-list']/li/div/a/text()").extract()
        yield item
