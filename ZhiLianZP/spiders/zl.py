# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ZhiLianZP.items import ZhilianzpItem
from scrapy_redis.spiders import RedisCrawlSpider

class ZlSpider(RedisCrawlSpider):
    name = 'zl'
    # allowed_domains = ['zhaopin.com']
    # jl参数为：地址，kw参数为：职位
    # start_urls = ['http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E6%B7%B1%E5%9C%B3&kw=%E6%95%B0%E6%8D%AE%E6%8C%96%E6%8E%98&p=1']
    def __init__(self,*args,**kwargs):
        domain = kwargs.pop('domain','')
        self.allowed_domains = list(filter(None,domain.split(',')))
        super(ZlSpider,self).__init__(*args,**kwargs)

    # 加入redis_key值
    redis_key = 'zhaopin'
    redis_encoding = 'utf-8'

    rules = (
        Rule(LinkExtractor(allow=r'jobs/searchresult.ashx\?jl=.+?&kw=.+?&sg=.+?&p=\d+'), follow=True),
        Rule(LinkExtractor(allow=r'jobs.zhaopin.com/\d+.htm|xiaoyuan.zhaopin.com/job/\w'), callback='parse_item'),
    )

    def parse_item(self, response):
        item= ZhilianzpItem()
        item['url'] =response.url
        item['name'] = response.xpath('//div[@class="inner-left fl"]/h1/text()').extract_first()
        item['campany'] = response.xpath('/html/body/div[5]/div[1]/div[1]/h2/a/text()').extract_first()
        item['campany_link'] = response.xpath('/html/body/div[5]/div[1]/div[1]/h2/a/@href').extract_first()
        item['treatment'] =''.join(response.xpath('//div[@class="welfare-tab-box"]/span/text()').extract())
        item['salary'] = response.xpath('//div[@class="terminalpage-left"]/ul/li[1]/strong/text()').extract_first().replace('\xa0','')
        item['area'] = response.xpath('//div[@class="terminalpage-left"]/ul/li[2]/strong/text()').extract_first()
        item['pup_time'] = response.xpath('//div[@class="terminalpage-left"]/ul/li[3]/strong/text()').extract_first()
        item['experience'] = response.xpath('//div[@class="terminalpage-left"]/ul/li[5]/strong/text()').extract_first()
        item['education'] = response.xpath('//div[@class="terminalpage-left"]/ul/li[6]/strong/text()').extract_first()
        item['need_num'] = response.xpath('//div[@class="terminalpage-left"]/ul/li[7]/strong/text()').extract_first()
        item['position_type'] = response.xpath('//div[@class="terminalpage-left"]/ul/li[8]/strong/text()').extract_first()
        item['position_desc'] = ''.join(response.xpath('//div[@class="tab-cont-box"]/div[1]/p/text()').extract()).replace('\u2028','').replace('\xa0','').strip()
        item['campany_desc'] =''.join(response.xpath('//div[@class="tab-cont-box"]/div[2]/p/text()').extract()).replace('\r\n','').strip()
        yield item


