from aip import AipNlp
import json

APP_ID = '11343165'
API_KEY = 'xCatrDFmNOPB6vhVYqWInKR2'
SECRET_KEY = '8xEwAxortvHC03G0RavocPIimuzF4AUl'
client = AipNlp(APP_ID, API_KEY, SECRET_KEY)

def ai_get(content,a):
    text = content
    result=client.sentimentClassify(text)
    
    confidence = result['items'][0]['confidence']#可信度
    positive_prob = result['items'][0]['positive_prob']#积极度
    negative_prob = result['items'][0]['negative_prob']#消极度
    sentiment = result['items'][0]['sentiment']#情感倾向
    if sentiment == 0:
        str_sentiment = '负向'
    if sentiment == 1:
        str_sentiment = '中性'
    if sentiment == 2:
        str_sentiment = '正向'

    out = '积极度：' + str(positive_prob*100) + '%, 消极度:' + str(negative_prob*100) + '%， 情感倾向：' + str_sentiment + '， 情感判断可信度：' + str(confidence*100) + '%.'
    outs = 'text:' + text + ', ' + out
    o = text + '    ' + str(positive_prob) + '  ' + str(negative_prob) + '  ' + str(sentiment) + '  ' + str(confidence)
    if a == 1:
        return outs
    if a == 0:
        return out
    if a == 2:
        return o
    if a == 'n':
        return negative_prob
    if a == 'p':
        return positive_prob
    if a == 's':
        return sentiment
    if a == 'al':
        alert = ('您当前情绪负面因素较大，请冷静后再水群。（ ' + out)
        return alert
    if a== 'j':
        return result
    


    
