# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy_demo.jianshu_spider.jianshu_spider.items import ArticleItem

class JsSpider(CrawlSpider):
    name = 'js'
    allowed_domains = ['jianshu.com']
    start_urls = ['https://www.jianshu.com/']

    rules = (
        Rule(LinkExtractor(allow=r'.*/p/[0-9a-z]{12}.*'), callback='parse_detail', follow=True),
    )

    def parse_detail(self, response):
        title = response.xpath("//h1[@class='title']/text()").get()
        avatar = response.xpath("//a[@class='avather']/img/@src").get()
        author = response.xpath("//span[@class='name']/a/text()").get()
        pub_time = response.xpath("//span[@class='publish-time']/text()").get().replace("*","")
        url = response.url
        url1 = url.split("?")[0]
        article_id = url1.split('/')[-1]
        content = response.xpath("//div[@class='show-content']").get()
        word_count = response.xpath("//span[@class='wordage']/text()").get()
        comment_count = response.xpath("//span[@class='comments-count']/text()").get()
        like_count = response.xpath("//span[@class='likes-count']/text()").get()
        read_count = response.xpath("//span[@class='views-count']/text()").get()
        subjects = ",".join(response.xpath("//div[@class='include-collection']/a/div/text()").getall())

        item = ArticleItem(title=title,avatar=avatar,pub_time=pub_time,
                           origin_url=response.url,article_id =article_id,
                           author=author,content=content,
                           word_count=word_count,like_count=like_count,
                           read_count=read_count,comment_count=comment_count,
                           subjects=subjects)
        yield item