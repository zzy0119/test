# -*- coding:utf-8 -*-


import requests
import pandas as pd
import time

# 爬取多页

# 知乎反爬
headers = {
'authorization':'Bearer 2|1:0|10:1516980261|4:z_c0|92:Mi4xSU1HUEJBQUFBQUFBTUt6S0dUVUxEU1lBQUFCZ0FsVk5KWlpZV3dEOTNzZThDV2VPeEk0b1ZNVzlQUzB5NEtnUy1R|dfa73437167d4e93930014cbf15050e238127db54baae012e8a5b0a290db8459',
'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
}

# 定义一个函数 爬取指定页
user_data = []
def getPage(page):
    for i in range(page):
        url = "https://www.zhihu.com/api/v4/members/louis-zheng/followers?include=data%5B*%5D.\
answer_count%2Carticles_count%2Cgender%2Cfollower_count%2Cis_followed%2Cis_following%2C\
badge%5B%3F(type%3Dbest_answerer)%5D.topics&offset=60&limit=20".format(i*20)
        reponse = requests.get(url, headers = headers).json()['data']
        user_data.extend(reponse)
        print('正在爬取第%d页' % i)
        time.sleep(1)

if __name__ == '__main__':
# 保存
    getPage(10)
    df = pd.DataFrame.from_dict(user_data)
    df.to_csv('more_page.csv')
