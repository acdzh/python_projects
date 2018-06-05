from qqbot import QQBotSlot as qqbotslot, RunBot
import json
import baidu_ai as bd




@qqbotslot
def onQQMessage(bot, contact, member, content):
    if '@ME' in content:
        result = ai_get(content)
        bot.SendTo(contact, '@' + member.name + ' '  + result)

        

if __name__ == '__main__':
    RunBot()
    
