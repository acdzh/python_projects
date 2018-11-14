from qqbot import QQBotSlot as qqbotslot, RunBot
import json
import baidu_ai as bd




@qqbotslot
def onQQMessage(bot, contact, member, content):
    print('get a msg: ' + content)
    txt = content
    if '@ME' in content:
        out = bd.ai_get(txt,1)
        bot.SendTo(contact,out)
        print (out)
        
    elif not '表情' in content:
        neg = bd.ai_get(txt,'n')
        sen = bd.ai_get(txt,'s')
        if (neg > 0.6) & (sen == 0):
            alert = bd.ai_get(txt,'s')
            bot.SendTo(contact, alert)
        else:
            print('not replay')
        

if __name__ == '__main__':
    RunBot()
    
