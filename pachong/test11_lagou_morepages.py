# -*- coding:utf-8 -*-

from pymongo import MongoClient
import requests
from fake_useragent import UserAgent
import time

client = MongoClient()
db = client.lagou_pages
my_set = db.job



headers = {
    'Cookie':'JSESSIONID=ABAAABAACDBABJBC411A395F2F598FD2583C03460911334; user_trace_token=20180130142257-e862b646-3cb9-40b3-9c8a-cbb2eb44975a; _ga=GA1.2.1857781099.1517293379; _gid=GA1.2.471563096.1517293379; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1517293379; LGSID=20180130142258-0428897f-0586-11e8-abd5-5254005c3644; LGUID=20180130142258-04288b4b-0586-11e8-abd5-5254005c3644; SEARCH_ID=02dfd75039e34cef97da72784be3d18e; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1517295188; LGRID=20180130145307-3a6df5e5-058a-11e8-abd5-5254005c3644',
    'Referer':'https://www.lagou.com/jobs/list_%E7%88%AC%E8%99%AB?labelWords=&fromSearch=true&suginput=',
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
}


# 定义一个函数，pages爬取的页数, kd职位
def get_more_pages(pages, kd):
    for i in range(pages):
        url = 'https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false&isSchoolJob=0'
        payload = {
            'first': 'true',
            'pn': i,
            'kd': kd
        }

       # ua = UserAgent()
        #headers['User-Agent'] = ua.random  # 使用fake-Agent随机生成User-Agent，添加到headers
        response = requests.post(url, data=payload, headers=headers)
        if response.status_code == 200:

            job_json = response.json()['content']['positionResult']['result']

            my_set.insert(job_json)

        else:

            print('Something Wrong!')

        print('正在爬取' + str(i + 1) + '页的数据...')

        time.sleep(3)


if __name__ == '__main__':
    get_more_pages(3, 'PHP')
