import operator as op
import json

class CalRelationship:
    def __init__(self):
        self.relationships = []

    #得到txt文件内容
    def get_content(self, txtfile):
        with open(txtfile, 'r', encoding='utf-8') as f:
            content = f.read()
        return content

    #计算关系值的基础方法
    def cal_relationship(self,name1,name2,value):
        # 设置两个好友同时是否存在于三元组的标志
        flag = False
        for relationship in self.relationships:
            # 如果两个人都在那么改变其关系值，并改变标记值
            if name1 in relationship and name2 in relationship:
                #存储关系图在三元组 [ [name1,name2,value], [name3,name4,vaule]....]
                relationship[2] += value
                flag = True
        # 如果两好友中一者或都不在三元组内，那么添加
        if flag == False and op.eq(name1, name2) == False:
            # 第一次进去就有个初值
            self.relationships.append([name1, name2, value])


    #通过评论和点赞计算关系值
    def cal_relationship_by_data(self,datas,value):
        count = 0
        data_list = datas.split('\n')
        for element in data_list:
            count += 1
            data = element.split('$|$')
            #最后一个是空
            if data[0] == '':
                return 0
            self.cal_relationship(data[0],data[1],value)
            #print('已经分析了 '+ str(count)+' 行数据')

    def to_html(self):
        name_to_ids = {}
        nodes = []
        links = []
        for relationship in self.relationships:
            for i in range(0, 2):
                if relationship[i] not in name_to_ids.keys():
                    name_to_ids[relationship[i]] = str(len(name_to_ids) + 1)
                    nodes.append({
                        "id": name_to_ids[relationship[i]], 
                        "name": relationship[i],
                        "symbolSize": 10,
                        "draggable": True
                    })
            links.append({
                "id": str(len(links) + 1),
                "source": name_to_ids[relationship[0]],
                "target": name_to_ids[relationship[1]],
                "lineStyle": {
                    "width": 1 if relationship[2] < 20 else relationship[2] / 20 # 这个20控制线的粗细对应, 自行调节
                }
            })
        with open('./temp/template.html', 'r', encoding='utf-8') as f:
            html = f.read()
        html = html.replace('{text=data}', json.dumps(nodes, ensure_ascii=False)).replace('{text=links}', json.dumps(links, ensure_ascii=False))
        with open('./index.html', 'w', encoding='utf-8') as f:
            f.write(html)
        print("请打开 index.html")

    def start(self):
        comments = self.get_content('./temp/comment.txt')
        likes = self.get_content('./temp/like.txt')
        #开始计算
        #评论好友关系+3,点赞好友关系+1
        self.cal_relationship_by_data(comments,3)
        self.cal_relationship_by_data(likes,1)

if __name__ == '__main__':
    # 将关系设置为全局变量以供方便调用
    cal = CalRelationship()
    cal.start()
    cal.to_html()

