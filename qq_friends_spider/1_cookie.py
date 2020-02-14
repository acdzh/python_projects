from selenium import webdriver
from time import sleep
import json

your_qq_id = '填你的qq'
your_passwd = '你的密码'

#修改下一行里面的chromedrive地址，若已设环境变量可无视
#chromedriver = 'D:\Program Files (x86)\chromedriver\chromedriver_win32/chromedriver.exe' 
#driver = webdriver.Chrome(chromedriver)
driver = webdriver.Chrome()
driver.get(f'https://user.qzone.qq.com/{your_qq_id}/main')
driver.switch_to.frame('login_frame')
#找到账号密码登陆的地方
driver.find_element_by_id('switcher_plogin').click()
driver.find_element_by_id('u').send_keys(your_qq_id)
driver.find_element_by_id('p').send_keys(your_passwd)
driver.find_element_by_id('login_button').click()
i = input("等登陆完成后, 输入 Y 并回车: ")

#保存本地的cookie
cookies = driver.get_cookies()
cookie_dic = {}
for cookie in cookies:
    if 'name' in cookie and 'value' in cookie:
        cookie_dic[cookie['name']] = cookie['value']
    with open('./temp/cookie_dict.txt', 'w') as f:
        json.dump(cookie_dic, f)
