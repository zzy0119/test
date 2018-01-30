# -*- coding:utf-8 -*-

import requests
import pandas as pd

# 爬出知乎廖雪峰所有的关注的人的信息

# 针对知乎的反爬
headers = {
    'authorization':'Bearer 2|1:0|10:1516980261|4:z_c0|92:Mi4xSU1HUEJBQUFBQUFBTUt6S0dUVUxEU1lBQUFCZ0FsVk5KWlpZV3dEOTNzZThDV2VPeEk0b1ZNVzlQUzB5NEtnUy1R|dfa73437167d4e93930014cbf15050e238127db54baae012e8a5b0a290db8459',
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
}

url = 'https://www.zhihu.com/api/v4/members/liaoxuefeng/followees?include=data%5B*%5D.answer_count%2Carticles_count%2Cgender%2Cfollower_count%2Cis_followed%2Cis_following%2Cbadge%5B%3F(type%3Dbest_answerer)%5D.topics&offset=20&limit=20'
r = requests.get(url, headers = headers).json()['data']

# 保存
df = pd.DataFrame.from_dict(r)
# print(df)
df.to_excel('lxf_fellows.xlsx')

