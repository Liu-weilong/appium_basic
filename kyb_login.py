#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2019/4/11 9:45
#@Author: liuweilong
#@File  : kyb_login.py
from app.capalibity import drised,NoSuchElementException
def login():
    drised.find_element_by_id('com.tal.kaoyan:id/login_email_edittext').clear()
    drised.find_element_by_id('com.tal.kaoyan:id/login_email_edittext').send_keys('测试数据')
    drised.find_element_by_id('com.tal.kaoyan:id/login_password_edittext').clear()
    drised.find_element_by_id('com.tal.kaoyan:id/login_password_edittext').send_keys('123456789')
    drised.find_element_by_id('com.tal.kaoyan:id/login_login_btn').click()
try:
    drised.find_element_by_id('com.tal.kaoyan:id/mainactivity_button_mysefl')
except NoSuchElementException:
    login()
else:
    drised.find_element_by_id('com.tal.kaoyan:id/mainactivity_button_mysefl').click()
    drised.find_element_by_id('com.tal.kaoyan:id/activity_usercenter_username').click()
    login()




































