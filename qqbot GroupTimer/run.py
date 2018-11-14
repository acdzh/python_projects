from qqbot import QQBotSlot as qqbotslot, RunBot
import time
import os

while (1):
    localtime = time.asctime(time.localtime(time.time()))
    minu = time.strftime("%M",time.localtime())
    print(minu)
    if minu == '00':
        print('i am running')
        year = time.strftime("%y",time.localtime())
        mon = time.strftime("%m",time.localtime())
        day = time.strftime("%d",time.localtime())
        time_now = time.strftime("%H:%M:%S",time.localtime())
        msg = "现在是北京时间 20"+ year + "年" + mon+"月"+day+"日 "+time_now+"  ---来自三三的沙雕机器人"
        command = ('qq send group 官方地下组织 ' + msg)
        os.system(command)
        print(msg)
        time.sleep(80)


