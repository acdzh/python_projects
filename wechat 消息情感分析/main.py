import itchat
import json
import baidu_ai as bd



@itchat.msg_register(itchat.content.TEXT)
def print_content(msg):
    txt = msg['Text']
    print(txt)
    out = bd.ai_get(txt,1)
    print (out)
    itchat.send(out, 'filehelper')

        
itchat.auto_login(hotReload=True)
itchat.run()
