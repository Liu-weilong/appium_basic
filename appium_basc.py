#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2019/4/8 14:51
#@Author: liuweilong
#@File  : appium_basc.py
from appium import webdriver

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['deviceName'] = '127.0.0.1:62026'
desired_caps['platforVersion'] = '7.1.2'

desired_caps['app'] = r'D:\360Downloads\kaoyanbang_3.3.6.242.apk'
desired_caps['appPackage'] = 'com.tal.kaoyan'
desired_caps['appActivity'] = 'com.tal.kaoyan.ui.activity.SplashActivity'

dirver = webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)

