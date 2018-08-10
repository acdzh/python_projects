import itchat
import time
import os
itchat.login()

users = itchat.search_friends("acdzh")

userName = users[0]['UserName']

print(userName)

os.system("pause")
while (1):
    localtime = time.asctime(time.localtime(time.time()))
    mon = time.strftime("%m",time.localtime())
    day = time.strftime("%d",time.localtime())
    time_now = time.strftime("%H:%M:%S",time.localtime())
    msg = "现在是庆丰五年 "+mon+"月"+day+"日 "+time_now
    itchat.send(msg,toUserName=userName)
    #itchat.run()
    print(msg)
    time.sleep(2)


