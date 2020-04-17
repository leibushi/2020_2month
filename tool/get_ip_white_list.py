# -*- coding: utf-8 -*-
# @Time    : 2020/4/13 9:55
# @Author  : Mqz
# @FileName: get_ip_white_list.py

import requests

url = 'http://wapi.http.cnapi.cc/index/index/save_white?neek=38118&appkey=e0b0871f0c31983540dd42f6135a105a&white=113.111.231.141'
res = requests.get(url)
print(res.text)