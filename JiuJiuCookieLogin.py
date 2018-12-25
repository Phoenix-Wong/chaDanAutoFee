# -*- coding:utf-8 -*-
__author__ = 'Administrator'

import requests
import time

url = "http://99shou.cn/charge/phone/receive/info"
s = requests.Session()
headers = {
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Content-Length": "64",
    "Content-Type": "application/x-www-form-urlencoded",
    # cookie值不要泄露
    "Cookie": "",
    "Host": "99shou.cn",
    "Origin": "http://99shou.cn",
    "Pragma": "no-cache",
    "Referer": "http://99shou.cn/charge/phone/table?type=doing",
    "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Mobile Safari/537.36",
    "X-Requested-With": "XMLHttpRequest"}
data = {
    "facevalue": 30,
    "receiveNum": 1,
    "channel[0]": 1
}

flag = True
while flag:
    time.sleep(3)
    try:
        r = s.post(url, data=data, headers=headers)
        content = r.text
        if '000000' in content:
            print("success")
            flag = False
        else:
            print(content)
    except Exception as e:
        print("ERROR{} > loginbyPWD():".format(time.ctime()) + str(e))
        print("error")