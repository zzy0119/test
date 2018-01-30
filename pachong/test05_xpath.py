# -*- coding:utf-8 -*-

import requests

from lxml import etree

url = 'https://www.douban.com/event/29968541/'
url_text = requests.get(url).text

# print(url_text)

# 解析html数据
s = etree.HTML(url_text)
# print(s)

print(s.xpath('//*[@id="edesc_s"]/text()'))
