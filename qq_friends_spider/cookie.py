from selenium import webdriver
from time import sleep
import json


#修改下一行里面的chromedrive地址，若已设环境变量可无视

#chromedriver = 'D:\Program Files (x86)\chromedriver\chromedriver_win32/chromedriver.exe' 
#driver = webdriver.Chrome(chromedriver)
driver = webdriver.Chrome()
driver.get('https://user.qzone.qq.com/这里改为你自己的qq号/main')
driver.switch_to.frame('login_frame')
#找到账号密码登陆的地方
driver.find_element_by_id('switcher_plogin').click()
driver.find_element_by_id('u').send_keys('这里填写你的qq号')
driver.find_element_by_id('p').send_keys('这里填写你的qq密码')
driver.find_element_by_id('login_button').click()
#保存本地的cookie
sleep(1)
cookies = driver.get_cookies()
cookie_dic = {}
for cookie in cookies:
    if 'name' in cookie and 'value' in cookie:
        cookie_dic[cookie['name']] = cookie['value']
    with open('cookie_dict.txt', 'w') as f:
        json.dump(cookie_dic, f)
