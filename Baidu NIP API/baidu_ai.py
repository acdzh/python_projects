from aip import AipNlp
import json

APP_ID = '修改'
API_KEY = '修改'
SECRET_KEY = '修改'
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
	if a == 1:
		return outs
	if a == 0:
		return out


    
