# -*- coding: utf-8 -*-
from bmw5_images.items import Bmw5ImagesItem
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class Bmw5Spider(CrawlSpider):
    name = 'bmw5'
    allowed_domains = ['car.autohome.com.cn']
    start_urls = ['https://car.autohome.com.cn/pic/series/202.html']

    rules = (
        Rule(LinkExtractor(allow=r'https://car.autohome.com.cn/pic/series/202.+'), callback='parse_page', follow=True),
    )

    def parse_page(self, response):
        category = response.xpath("//div[@class='uibox']/div[@class='uibox-title']/text()").get()
        urls = response.xpath("//div[@class='uibox-con carpic-list03 border-b-solid']//li/a/img/@src").getall()
        urls = list(map(lambda url: response.urljoin(url.replace('240x180', '1024x0')), urls))
        item = Bmw5ImagesItem(category=category, image_urls=urls)
        yield item