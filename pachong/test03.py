# -*- coding:utf-8 -*-

import requests

# 获取源码
r = requests.get('https://movie.douban.com/subject/22265634/?from=showing').text

# 解析数据
from bs4 import BeautifulSoup
import lxml
soup = BeautifulSoup(r, 'lxml')
pattern = soup.find_all('p', '')
for item in pattern:
    print(item.string)

# 保存数据
import pandas
comments = []
for item in pattern:
    comments.append(item.string)
df = pandas.DataFrame(comments)
df.to_csv('test03.cvs')

