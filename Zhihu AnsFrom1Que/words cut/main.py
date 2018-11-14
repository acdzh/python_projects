#coding:utf-8

import matplotlib.pyplot as plt  
from wordcloud import WordCloud,STOPWORDS,ImageColorGenerator
import jieba
from os import path
import jieba.analyse as analyse

  
backgroup_Image = plt.imread('background.jpg') #笼罩图
d = path.dirname(__file__)
my_font = 'C:\\Windows\\Fonts\\msyh.ttc'
text_path = 'input.txt' #设置要分析的文本路径

my_width = 2400
my_height = 2408

#text= open('order.log','r', encoding='UTF-8')
text = open(path.join(d, text_path)).read()
seg_list = jieba.cut(text, cut_all=False, HMM=True)
out_text = " ".join(seg_list)
#print(out_text)  # 默认模式


stopwords = set(STOPWORDS)
stopwords.add("我们")
stopwords.add("他们")
stopwords.add("你们")
stopwords.add("然后")
stopwords.add("可以")
stopwords.add("还是")
stopwords.add("而且")
stopwords.add("大家")
stopwords.add("什么")
stopwords.add("更新")
stopwords.add("事情")
stopwords.add("但是")
stopwords.add("觉得")
stopwords.add("不过")
stopwords.add("自己")
stopwords.add("这么")
stopwords.add("有些")
stopwords.add("这样")
stopwords.add("那些")
stopwords.add("真的")
stopwords.add("这个")
stopwords.add("每个")
stopwords.add("首先")
stopwords.add("还有")
stopwords.add("的话")
stopwords.add("因为")
stopwords.add("认为")
stopwords.add("这些")
stopwords.add("就是")
stopwords.add("只是")
stopwords.add("之后")
stopwords.add("这不")
stopwords.add("这种")
stopwords.add("一样")

  
#f = open(u'1.txt','r').read()  #生成词云的文档  
wordcloud = WordCloud(background_color = 'white',stopwords=stopwords, max_words = 300, mask = backgroup_Image, font_path = my_font,width = my_width,  height = my_height,  margin = 2).generate(out_text) # generate 可以对全部文本进行自动分词  
#参数 width，height，margin分别对应宽度像素，长度像素，边缘空白处  
  
plt.imshow(wordcloud)  
plt.axis('off')  
plt.show()  
#plt.savefig("out.jpg",dpi=1024)  
wordcloud.to_file('out.jpg') 


