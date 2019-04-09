#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2019/4/9 10:21
#@Author: liuweilong
#@File  : capalibity.py
from appium import webdriver
from selenium.common.exceptions import NoSuchElementException

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['deviceName'] = '127.0.0.1:62029'
desired_caps['platforVersion'] = '5.1.1'

desired_caps['app'] = r'D:\360Downloads\kaoyanbang_3.3.6.242.apk'
desired_caps['appPackage'] = 'com.tal.kaoyan'
desired_caps['appActivity'] = 'com.tal.kaoyan.ui.activity.SplashActivity'

#中文字符配置
desired_caps['unicodeKeyboard'] = 'True'
desired_caps['resetKeyboard'] = 'True'

drised = webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
drised.implicitly_wait(5)
try:
    clickskin = drised.find_element_by_id('com.tal.kaoyan:id/tv_skip')
except NoSuchElementException:
    print('come on')
else:
    clickskin.click()










