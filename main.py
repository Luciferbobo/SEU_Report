from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import os
import json
import random
import time
import datetime
import traceback

def wait_element_by_class_name(drv, class_name, timeout):
    WebDriverWait(drv, timeout).until(lambda d: d.find_element_by_class_name(class_name))

def find_element_by_class_placeholder_keyword(drv, class_name, keyword):
    elements = drv.find_elements_by_class_name(class_name)
    for element in elements:
        if element.get_attribute('placeholder').find(keyword) >= 0:  
            return element
    return None

def find_element_by_class_keyword(drv, class_name, keyword):
    elements = drv.find_elements_by_class_name(class_name)
    for element in elements:
        if element.text.find(keyword) >= 0:  
            return element
    return None

def picker_click(drv, column, cnt):
    pickers = column.find_elements_by_class_name('mt-picker-column-item') 
    drv.execute_script("arguments[0].scrollIntoView();", pickers[cnt]) 
    pickers[cnt].click()  

def check_todays_report(drv):
    items = drv.find_elements_by_class_name('res-list') 
    latest = find_element_by_class_keyword(items[0], 'res-item-ele', '申请时间').text  
    latest = latest[latest.find(' ') + 1: latest.rfind(' ')]  
    latest_date = datetime.datetime.strptime(latest, '%Y-%m-%d').date() 

    if latest_date == date_of_today.date():  
        return True

    return False

def login(drv, cfg):
    username_input = drv.find_element_by_id('username') 
    password_input = drv.find_element_by_id('password') 
    login_button = find_element_by_class_keyword(drv, 'auth_login_btn', '登录') 
    if login_button is None:
        login_button = find_element_by_class_keyword(drv, 'auth_login_btn', 'Sign in') 
    username_input.send_keys(cfg['username'])
    password_input.send_keys(cfg['password'])
    login_button.click()  # 登录账户

def daily_report(drv, cfg):
    wait_element_by_class_name(drv, 'mint-loadmore-top', 30) 
    time.sleep(random.randint(1,3))
    add_btn = drv.find_element_by_xpath('//*[@id="app"]/div/div[1]/button[1]') 
    if add_btn.text == '退出':
        return
    else:
        add_btn.click() 
        time.sleep(random.randint(1,3)) 
    temp_input = find_element_by_class_placeholder_keyword(drv, 'mint-field-core', '请输入当天晨检体温')
    drv.execute_script("arguments[0].scrollIntoView();", temp_input) 
    temp_input.click() 
    temp = random.randint(34,35)  
    temp_input.send_keys(str(temp)) 
    time.sleep(random.randint(1,3))
    find_element_by_class_keyword(drv, 'mint-button--large', '确认并提交').click() 
    wait_element_by_class_name(drv, 'mint-msgbox-confirm', 5) 
    time.sleep(random.randint(1,3))
    find_element_by_class_keyword(drv, 'mint-msgbox-confirm', '确定').click()  

def run(profile):
    driver = webdriver.Chrome(executable_path="Chromedriver.exe")
    try:
        driver.get(daily_report_url)
        login(driver, profile)
        daily_report(driver, profile)
    except Exception:
        exception = traceback.format_exc()
    finally:
        time.sleep(random.randint(3,4))
        driver.quit()  

for i in range(1000000):
    date_of_today = datetime.datetime.now()
    daily_report_url = 'http://ehall.seu.edu.cn/qljfwapp2/sys/lwReportEpidemicSeu/*default/index.do#/dailyReport'
    config_file=open('config.json', encoding='UTF-8')
    j = json.load(config_file)
    print(date_of_today)
    for user in list(j.keys()):
        user=j[str(user)][0]
        print(user['username'], '开始填报')
        run(user)
        print(user['username'], '填报完成')
        time.sleep(random.randint(1,3))
    time.sleep(86400+random.randint(-120,120))

'''
1.默认填报体温为34°-35°随机生成
2.默认每24h执行一次填报，每次填报时间随机相差±2min，防止检测
3.默认操作之间随机延迟1-3s，防止检测
4.支持多人填报，按照格式在config.json中添加新信息即可
'''
















