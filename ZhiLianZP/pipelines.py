# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json


class ZhilianzpPipeline(object):
    def __init__(self):
        self.file = open('zhaopin.json','w',encoding='utf-8')


    def process_item(self, item, spider):
        data = json.dumps(dict(item),ensure_ascii=False) + ',\n'
        self.file.write(data)
        return item

    def close_file(self):
        self.file.close()
