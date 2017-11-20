# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ZhilianzpItem(scrapy.Item):
    # define the fields for your item here like:
    # 链接
    url = scrapy.Field()
    # 职位
    name = scrapy.Field()
    # 公司
    campany = scrapy.Field()
    # 公司链接
    campany_link = scrapy.Field()
    # 待遇
    treatment = scrapy.Field()
    # 月薪
    salary = scrapy.Field()
    # 工作地点
    area = scrapy.Field()
    # 详细地址
    area_detail = scrapy.Field()
    # 发布日期
    pup_time = scrapy.Field()
    # 经验
    experience = scrapy.Field()
    # 学历
    education = scrapy.Field()
    # 需求人数
    need_num = scrapy.Field()
    # 职位类别
    position_type = scrapy.Field()
    # 职位描述
    position_desc = scrapy.Field()
    # 公司介绍
    campany_desc = scrapy.Field()

    pass
