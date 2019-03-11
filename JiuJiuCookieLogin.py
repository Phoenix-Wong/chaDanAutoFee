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
    "facevalue": 100,
    # "provId": 3087,
    "receiveNum": 1,
    "channel[0]": 1
}
#{"id":"2753","name":"陕西省"},{"id":"1332","name":"河南省"},{"id":"1152","name":"山东省"},{"id":"1026","name":"内蒙古自治区"},{"id":"213","name":"上海"}
#"rtnData":[{"id":"2467","name":"黑龙江省"},{"id":"2753","name":"陕西省"},{"id":"3087","name":"重庆"},{"id":"2249","name":"辽宁省"},{"id":"1840","name":"福建省"},{"id":"2881","name":"甘肃省"},{"id":"1662","name":"湖南省"},{"id":"1529","name":"湖北省"},{"id":"100","name":"浙江省"},{"id":"1332","name":"河南省"},{"id":"684","name":"河北省"},{"id":"516","name":"江西省"},{"id":"2111","name":"广西壮族自治区"},{"id":"1944","name":"广东省"},{"id":"883","name":"山西省"},{"id":"1152","name":"山东省"},{"id":"374","name":"安徽省"},{"id":"663","name":"天津"},{"id":"3130","name":"四川省"},{"id":"2384","name":"吉林省"},{"id":"642","name":"北京"}]}
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