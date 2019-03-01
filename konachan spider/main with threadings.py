try:
    import time
    import requests
    import json
    import os
    import threading
    import queue
    from contextlib import closing
except:
    print('请不要将此软件放在中文路径下，并安装好依赖包（RUN_ME_AT_THE_FIRST_TIME.bat）')
    print('错误：加载依赖库失败')
    exit()

my_headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36',
            'Host': 'konachan.net'
    }
my_url = 'https://konachan.net/post.json'
my_queue = queue.Queue()
my_ratings = ['s']
page = 1
final_page = 999

class pic():
    def __init__(self, number, name, mid, size, dimension, url, rating):
        self.number = number
        self.name = name
        self.id = mid
        self.size = size
        self.dimension = dimension
        self.url = url
        self.rating = rating

class myThread(threading.Thread):
    def __init__(self, _threadID, ):
        threading.Thread.__init__(self)
        self.threadID = _threadID

    def run(self):
        global page
        print("线程 {} 开始运行...".format(self.threadID))
        while 1:
            threadLock.acquire()
            if my_queue.empty():
                page += 1
                add_queue(page)
                print("开始抓取第 {} 页...".format(page))
            img = my_queue.get()
            threadLock.release()
            if img.rating in my_ratings:
                print("线程 {} 正在抓取第 {} 页, 第 {} 张".format(self.threadID, page, img.number))
                print("    文件名: {}".format(img.name))
                print("    id: {}, 大小: {}, 尺寸: {}".format(img.id, img.size, img.dimension))
                get_pic(img.url, "pics/" + img.name)
                print("线程 {} 下载完成!\n".format(self.threadID))
        print("线程 {} 退出...".format(self.threadID))

def size_format(sz):
    if sz < 1024:
        return (str(sz) + " B")
    if 1024 <= sz < 1048576:
        return (str(round(sz / 1024, 2)) + " KB")
    if 1048576 <= sz < 1073741824:
        return (str(round(sz / 1048576, 2)) + " MB")
    if sz >= 1073741824:
        return (str(round(sz / 1073741824, 2)) + " GB")
    return "ERROR SIZE"

def url2name(url):
    url = url.split('/')[-1].replace('%20', ' ')
    url = url.replace('%28', '(').replace('%29', ')')
    return url

def add_queue(page):
        my_data = {'page': page}
        r = requests.get(my_url, headers=my_headers, data = my_data)
        dic = []
        count = 0
        for i in json.loads(r.text):
            count += 1
            name = url2name(i["file_url"])
            mid = i["id"]
            size = size_format(int(i["file_size"]))
            dimension = "{} × {}".format(i["width"], i["height"])
            my_queue.put(pic(count, name, mid, size, dimension, i["file_url"], i["rating"]))




def get_pic(url, name):
        print("    获取文件大小...", end="\r")
        r = requests.get(url, headers=my_headers, stream=True)
        with closing(r) as response:
            chunk_size = 2048  # 单次请求最大值
            content_size = int(response.headers['content-length'])  # 内容体总大小
            #progress = ProgressBar(content_size)   # 取消了进度条显示
            with open(name, "wb") as f:
                for data in response.iter_content(chunk_size=chunk_size):
                    f.write(data)
                    #progress.refresh(count=len(data))


def start(start_page = 1, ratings = ['s'], ants = 0):
    global page, my_ratings
    page = start_page
    my_ratings = ratings
    myThreads = []
    for i in range(0, ants):
        myThreads.append(myThread(i + 1))
    for i in myThreads:
        i.start()
    for i in myThreads:
        i.join()
    print("抓取结束.")




if __name__ == "__main__":
    print("""
        这只是个对程序的改进版本, 加入了多线程下载, 下载速率增加, 但是架构也变得更加混乱.\n
        如无速度要求, 建议使用原程序.\n
        该脚本有很大的可能中途崩掉.\n
        谢谢茄子\n
        """)

    threadLock = threading.Lock()
    if 'pics' not in os.listdir(os.getcwd()):
        os.mkdir('pics')
    try:
        my_start_page = eval(input("请输入开始页码(不输入默认为1): "))
    except SyntaxError:
        my_start_page = 1
    try:
        ants = eval(input("请输入同时运行的线程数(默认为5): "))
    except SyntaxError:
        ants = 5
    str_rating = input("请输入图片分级(要获取关于分级的建议请输入'h', 不输入则默认为仅s级): ")
    if str_rating == '':
        str_rating = 's'
    if str_rating == 'h':
        print("  k站图片分级有三级, 按照暴露程度由高至低可分为三级: e, q, s;")
        print("  其中, s是最安全的等级. 下面是三种等级的示例, 具体划分方式不再用文字阐述: ")
        print("    s: https://konachan.com/post/show/278859 ;")
        print("    q: https://konachan.com/post/show/278861 ;")
        print("    e: https://konachan.com/post/show/278857 ;")
        print("  直接输入自己想要的分级即可, 如想要s和q分级的图片, 请输入'sq'或者'qs';")
        str_rating = input("请输入图片分级(默认为仅s级): ")
        if str_rating == '':
            str_rating = 's'
    my_rating = []
    for i in str_rating:
        if i not in my_rating:
            my_rating.append(i)
    start(start_page = my_start_page, ratings = my_rating, ants = ants)
    
    
    
    
    
    