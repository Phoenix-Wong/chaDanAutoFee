# -*- coding:utf-8 -*-
__author__ = 'Administrator'

import time
from selenium import webdriver

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
chrome.find_element_by_id("loginButton").click()
time.sleep(5)
chrome.get(url="http://chadan.cn/MOBILE")
while True:
    try:
        chrome.find_element_by_xpath(".//*[@id='takeOrder']/td[4]").click()
        time.sleep(0.5)
        chrome.find_element_by_class_name("sure-take-order").click()
        time.sleep(1)
        print("抢购成功并且已下单！！")
    except Exception:
        print("还未开始抢购！！")