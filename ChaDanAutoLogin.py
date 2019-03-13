# -*- coding:utf-8 -*-
__author__ = 'Administrator'

import requests
import time

url = "http://api.chadan.wang/order/getOrderdd623299"
s = requests.Session()
headers = {
        # "Host": "chadan.cn",
        # "Connection": "keep-alive",
        # "Content-Length": "105",
        # "Pragma": "no-cache",
        # "Cache-Control": "no-cache",
        # "Accept": "application/json, text/javascript, */*; q=0.01",
        # "Origin": "http://chadan.cn",
        # "X-Requested-With": "XMLHttpRequest",
        # "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36",
        # "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        # "Referer": "http://chadan.cn/orderPool",
        # "Accept-Encoding": "gzip, deflate",
        # "Accept-Language": "zh-CN,zh;q=0.9",
        # "Cookie": "_uab_collina=154813713116571233848926; shareCode=; logged=aad6582f-b6ed-4271-bd89-43468a2a6172; JSESSIONID=3C8C0DA25C98DDDE7EE93F0DBDA51E50"
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "Origin": "http://chadan.cn",
            "Referer": "http://chadan.cn/orderPool",
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36"
             }
data = {
    "JSESSIONID": "",
    "faceValue": 50,
    "amount": 1,
    "operator": "MOBILE",
    "channel": 1
}

flag = True
while flag:
    time.sleep(3)
    try:
        r = s.post(url, data=data, headers=headers)
        content = r.text
        # print(content)
        if content.__len__() > 70:
            flag = False
            print("success")
        else:
            print(content)
    except Exception as e:
        print("ERROR{} > loginbyPWD():".format(time.ctime()) + str(e))
        print("error")

