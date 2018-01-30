# -*- coding:utf-8 -*-


from pymongo import MongoClient

client = MongoClient()
db = client.lagou2 #创建数据库 拉勾
my_set = db.job #创建job集合

import  requests
url = 'https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false&isSchoolJob=0'

# 通常，你想要发送一些编码为表单形式的数据——非常像一个 HTML 表单。\
# 要实现这个，只需简单地传递一个字典给 data 参数。你的数据字典在发出请求时会自动编码为表单形式
# 爬取单页不需要此参数
payload = {
    'first':'false',
    'pn':1,
    'kd':'爬虫'
}

headers = {
    'Cookie':'JSESSIONID=ABAAABAACDBABJBC411A395F2F598FD2583C03460911334; user_trace_token=20180130142257-e862b646-3cb9-40b3-9c8a-cbb2eb44975a; _ga=GA1.2.1857781099.1517293379; _gid=GA1.2.471563096.1517293379; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1517293379; LGSID=20180130142258-0428897f-0586-11e8-abd5-5254005c3644; PRE_UTM=; PRE_HOST=; PRE_SITE=; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2Fjobs%2Flist_%25E7%2588%25AC%25E8%2599%25AB%3FlabelWords%3D%26fromSearch%3Dtrue%26suginput%3D; LGUID=20180130142258-04288b4b-0586-11e8-abd5-5254005c3644; SEARCH_ID=46977a0612c84c58b48d6e8a01316c39; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1517293414; LGRID=20180130142334-196ac63b-0586-11e8-abd5-5254005c3644',
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
    'Referer':'https://www.lagou.com/jobs/list_%E7%88%AC%E8%99%AB?labelWords=&fromSearch=true&suginput='
}

response = requests.post(url, headers = headers)
print(response.json()) #失败，拉勾不让爬 加入头
#保存在数据库
my_set.insert(response.json()['content']['positionResult']['result'])


