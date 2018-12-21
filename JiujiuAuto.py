# -*- coding:utf-8 -*-
__author__ = 'Administrator'
import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select

jiujiu_up={"ue":"","pd":""}
chrome = webdriver.Chrome()
chrome.get(url="http://99shou.cn/login.jsp")
time.sleep(1)
User = chrome.find_element_by_id("signupform-username")
User.clear()
time.sleep(1)
User.send_keys(jiujiu_up["ue"])
Passwd = chrome.find_element_by_id("signupform-password")
Passwd.clear()
time.sleep(1)
Passwd.send_keys(jiujiu_up["pd"])
time.sleep(1)
chrome.find_element_by_name("signup-button").click()
time.sleep(2)
chrome.get(url="http://99shou.cn/charge/phone/table?type=doing")
while True:
    try:
        # 选择充值金额
        # print(chrome.find_element_by_xpath("layui-anim layui-anim-upbit"))
        Select(chrome.find_element_by_xpath(".//*[@class='layui-anim layui-anim-upbit']")).select_by_index(2)
        # Select()
        chrome.find_element_by_class_name("layui-btn layui-btn-danger layui-btn-sm").submit()
        time.sleep(2)
        print("抢购成功并且已下单！！")
        chrome.quit()
    except Exception:
        print("还未开始抢购！！")