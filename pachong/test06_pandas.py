# -*- coding:utf-8 -*-


# 获取数据
import requests

url = "https://book.douban.com/subject/1084336/comments/"
r = requests.get(url).text

# 解析数据
from lxml import etree
s = etree.HTML(r)
# print(s)地址
pth = s.xpath('//*[@id="comments"]/ul/li/div/p/text()')
#print(pth)

# 存储数据
import pandas as pd
#将包pandas起一个简写的别名

df = pd.DataFrame(pth)
df.to_excel('xiaowangzi.xlsx')

