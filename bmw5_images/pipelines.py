# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.pipelines.images import ImagesPipeline
import os


class Bmw5ImagesPipeline(object):
    def process_item(self, item, spider):
        return item


class BMWImagesPipeline(ImagesPipeline):
    # 绑定item
    def get_media_requests(self, item, info):
        '''这个方法在发送下载请求之前调用'''
        request_objs = super(BMWImagesPipeline, self).get_media_requests(item, info)
        for request_obj in request_objs:
            request_obj.item = item
        return request_objs

    def file_path(self, request, response=None, info=None):
        '''这个方法在图片将要被存储的时候调用，来获取这个图片存储的路径'''
        path = super(BMWImagesPipeline, self).file_path(request, response, info)
        category = request.item.get('category')
        category_path = category
        image_name = path.replace('full/', '')
        image_path = os.path.join(category_path, image_name)
        return image_path