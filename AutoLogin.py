# -*- coding:utf-8 -*-
__author__ = 'Administrator'

import time
from selenium import webdriver
# 用户名  密码
chadan_up={"ue":"","pd":""}
chrome = webdriver.Chrome()
chrome.get(url="http://chadan.cn/loginIn")
time.sleep(3)
User = chrome.find_element_by_id("account")
User.clear()
time.sleep(3)
User.send_keys(chadan_up["ue"])
Passwd = chrome.find_element_by_id("password")
Passwd.clear()
time.sleep(3)
Passwd.send_keys(chadan_up["pd"])
time.sleep(3)
# 登陆
chrome.find_element_by_id("loginButton").click()
time.sleep(5)
# 移动话费页面
chrome.get(url="http://chadan.cn/MOBILE")
while True:
    try:
        # 面值选择
        chrome.find_element_by_xpath(".//*[@id='takeOrder']/td[4]").click()
        time.sleep(0.5)
        # 动态提交订单
        chrome.find_element_by_class_name("sure-take-order").click()
        time.sleep(1)
        print("抢购成功并且已下单！！")
        chrome.quit()
    except Exception:
        print("还未开始抢购！！")