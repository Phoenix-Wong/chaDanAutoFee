# -*- coding:utf-8 -*-
__author__ = 'Administrator'

import requests
import time

url = "http://chadan.cn/order/getOrderdd623299"
s = requests.Session()
headers = {
        "Host": "chadan.cn",
        "Connection": "keep-alive",
        "Content-Length": "105",
        "Pragma": "no-cache",
        "Cache-Control": "no-cache",
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Origin": "http://chadan.cn",
        "X-Requested-With": "XMLHttpRequest",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Referer": "http://chadan.cn/orderPool",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Cookie": ""}
data = {
    "JSESSIONID": "",
    "faceValue": 100,
    "amount": 1,
    "operator":"MOBILE",
    "channel":1
}


flag = True
while flag:
    time.sleep(3)
    try:
        r = s.post(url, data=data, headers=headers)
        content = r.text
        if(content.__getitem__("data")):
            flag = False
            print("success")
        else:
            print(content)
    except Exception as e:
        print("ERROR{} > loginbyPWD():".format(time.ctime()) + str(e))
        print("error")

