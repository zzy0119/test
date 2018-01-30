# -*- coding:utf-8 -*-


# 爬虫三步走
# 第一步 使用request获取数据
import requests


# 获取页码源码
r = requests.get('https://book.douban.com/subject/1084336/comments/').text

# 第二步 使用beautifulSoup4解析数据
# 1.导入bs
from bs4 import BeautifulSoup
import lxml
# 2.解析网页数据
soup = BeautifulSoup(r, 'lxml')
# 3.寻找数据
pattern = soup.find_all('p', 'comment-content')
# 4.打印数据
for item in pattern:
    print(item.string)

# 第三步 使用pandas保存数据
import pandas
comments = []
for item in pattern:
    comments.append(item.string)
df = pandas.DataFrame(comments)
df.to_csv('comments.cvs')


