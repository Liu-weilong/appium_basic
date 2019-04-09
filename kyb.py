#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2019/4/8 15:37
#@Author: liuweilong
#@File  : kyb.py
from appium import webdriver
from selenium.common.exceptions import NoSuchElementException
desried_caps = {}
desried_caps['platformName'] = 'Android'
desried_caps['deviceName'] = '127.0.0.1:62029'
desried_caps['platforVersion'] = '5.1.1'

desried_caps['app'] = r'D:\360Downloads\kaoyanbang_3.3.6.242.apk'
desried_caps['appPackage'] = 'com.tal.kaoyan'
desried_caps['appActivity'] = 'com.tal.kaoyan.ui.activity.SplashActivity'

driver = webdriver.Remote('http://localhost:4723/wd/hub',desried_caps)
driver.implicitly_wait(5)
try:
    driver.find_element_by_id('com.tal.kaoyan:id/tv_skip')
except NoSuchElementException:
    print('come on')
else:
    driver.find_element_by_id('com.tal.kaoyan:id/tv_skip').click()




























