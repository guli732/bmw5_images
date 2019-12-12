# -*- coding: utf-8 -*-
import scrapy
from bmw5_images.items import Bmw5ImagesItem


class Bmw5Spider(scrapy.Spider):
    name = 'bmw5'
    allowed_domains = ['car.autohome.com.cn']
    start_urls = ['https://car.autohome.com.cn/pic/series/202.html']

    def parse(self, response):
        uiboxs = response.xpath("//div[@class='uibox']")[1:]
        for uibox in uiboxs:
            category = uibox.xpath(".//div[@class='uibox-title']/a[1]/text()").get()
            urls = uibox.xpath(".//ul/li/a/img/@src").getall()
            urls = list(map(lambda url:response.urljoin(url), urls))
            item = Bmw5ImagesItem(category=category, image_urls=urls)
            yield item