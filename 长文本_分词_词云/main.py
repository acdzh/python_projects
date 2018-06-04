#coding:utf-8

import matplotlib.pyplot as plt  
from wordcloud import WordCloud,STOPWORDS,ImageColorGenerator
import jieba
from os import path
import jieba.analyse as analyse

  
backgroup_Image = plt.imread('background.jpg') #笼罩图
d = path.dirname(__file__)
my_font = 'msyh.ttf'
text_path = 'input.txt' #设置要分析的文本路径

my_width = 5000
my_height = 5000

#text= open('order.log','r', encoding='UTF-8')
text = open(path.join(d, text_path), encoding='UTF-8').read()
seg_list = jieba.cut(text, cut_all=False, HMM=True)
out_text = " ".join(seg_list)
#print(out_text)  # 默认模式




  
#f = open(u'1.txt','r').read()  #生成词云的文档  
wordcloud = WordCloud(background_color = 'white',mask = backgroup_Image, font_path = my_font,width = my_width,  height = my_height,  margin = 2).generate(out_text) # generate 可以对全部文本进行自动分词  
#参数 width，height，margin分别对应宽度像素，长度像素，边缘空白处  
  
plt.imshow(wordcloud)  
plt.axis('off')  
plt.show()  
  
#保存图片：默认为此代码保存的路径  
wordcloud.to_file('out.jpg') 


