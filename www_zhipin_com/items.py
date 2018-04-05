# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class WwwZhipinComItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # pass

    # 职位ID
    pid = scrapy.Field()
    # 职位名称
    positionName = scrapy.Field()
    # 工作时间（年限）
    workYear = scrapy.Field()
    # 薪资
    salary = scrapy.Field()
    # 公司地址
    city = scrapy.Field()
    # 学历
    education = scrapy.Field()
    # 公司名称
    companyShortName = scrapy.Field()
    # 公司类型
    industryField = scrapy.Field()
    # 融资情况
    financeStage = scrapy.Field()
    # 公司规模
    companySize = scrapy.Field()
    # 职位标签 
    positionLables = scrapy.Field()
    # 发布日期
    time = scrapy.Field()
    # 更新时间
    updated_at = scrapy.Field()
    # 招聘简介
    introduction = scrapy.Field()
