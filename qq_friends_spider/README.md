# qzone spider to find friends 
# qq空间爬虫生成好友关系网
----------------------

1.修改cookie.py里的chromrdriver地址（设置了环境变量的可不修改）。修改账号密码后运行，生成cookie_dict.txt

2.运行spider.py爬取数据,生成comment.txt(好友之间的评论关系)，like.txt（点赞记录），denied.txt（空间屏蔽你的好友名单）

3.运行show_relation目录下的analysis.py，得到好友关系值文件relationship.txt

4.将show_relation文件夹中的所有文件放置本地搭建的web服务器（远程服务器亦可）下，访问

5.enjoy it


##已知缺陷

1.若好友空间不可进或者他屏蔽了发过的说说，会造成遗漏

2.由于是通过互相评论和点赞的记录来计算关系，因此部分存在感弱的人会被遗漏

3.最终结果需要使用web服务器,以后有空再改吧（三分钟搭建一个本地服务器又不费事儿）

4.爬虫太慢了


##最终效果
[示例链接点我](http://118.25.100.134)（出于于隐私原因，我把好友昵称稍微做了一个小混淆）

![效果图](https://github.com/acdzh/python_projects/blob/master/qq_friends_spider/result_example/result.png)


![局部效果图](https://github.com/？/show_relation/result_partial.png)


##ps

制图时用到了[echats](http://echarts.baidu.com/)插件，感谢
