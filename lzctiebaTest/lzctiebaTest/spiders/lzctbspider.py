# -*- coding: utf-8 -*-
import scrapy
from lzctiebaTest.items import LzctiebatestItem


class LzctbspiderSpider(scrapy.Spider):
    name = 'lzctbspider'
    allowed_domains = ['tieba.baidu.com']
    start_urls = ['https://tieba.baidu.com/f?kw=%C1%FA%D6%E9%B3%AC&fr=ala0&tpl=5']
    #start_urls = ("http://www.itcast.cn/channel/teacher.shtml",)


    def parse(self, response):
        
        
        
        
        
        
        
        
        
        
        
        
        
# =============================================================================
#         node_list = response.xpath("//div[@class='li_txt']")
# 
#         # 用来存储所有的item字段的
#         #items = []
#         for node in node_list:
#             # 创建item字段对象，用来存储信息
#             item = LzctiebatestItem()
#             # .extract() 将xpath对象转换为 Unicode字符串
#             name = node.xpath("./h3/text()").extract()
#             title = node.xpath("./h4/text()").extract()
#             info = node.xpath("./p/text()").extract()
# 
#             item['name'] = name[0]
#             item['title'] = title[0]
#             item['info'] = info[0]
# 
#             # 返回提取到的每个item数据，给管道文件处理，同时还回回来继续执行后面的代码
#             yield item
#             #return item
#             #return scrapy.Request(url)
#             #items.append(item)
# 
#        # yield items
# =============================================================================
