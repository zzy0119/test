# -*- coding:utf-8 -*-

import urllib.request
import requests

#f = urllib.request.urlopen('http://www.baidu.com/')
#print(f.read(500))

z = requests.get('http://www.baidu.com/')

print(z.text)