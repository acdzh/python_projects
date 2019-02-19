try:
    import time
    import requests
    import json
    import os
    from contextlib import closing
except:
    print('请不要将此软件放在中文路径下，并安装好依赖包（RUN_ME_AT_THE_FIRST_TIME.bat）')
    print('错误：加载依赖库失败')
    exit()


class ProgressBar(object):

    def __init__(self, total):
        self._total = total
        self._count = 0
        self._full = 0

    def refresh(self, count):
        end_str = "\r"
        self._count += count
        if self._count >= self._total:
            if self._full == 0:
                self._count = self._total
                self._full = 1
                end_str = '\n'
            else:
                return
        precent = self._count / self._total
        info = "    进度: " + "■" * int(40 * precent) + "_" * (40 - int(40 * precent)) + "   {} / {}  {}%   ".format(
            self._count, self._total, int(100 * self._count / self._total))
        print(info, end=end_str)


class Konachan:
    def __init__(self, start_page=1, end_page=5, rating=['s']):
        self._headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36',
            'Host': 'konachan.net'
        }
        self._strat_page = start_page
        self._end_page = end_page
        self._url = 'https://konachan.net/post.json?page='
        self._rating = rating

    def get_list(self, page):
        r = requests.get(self._url + str(page), headers=self._headers)
        print(r.text)
        return json.loads(r.text)

    def get_pic(self, url, name):
        print("    获取文件大小...", end="\r")
        r = requests.get(url, headers=self._headers, stream=True)
        with closing(r) as response:
            chunk_size = 2048  # 单次请求最大值
            content_size = int(response.headers['content-length'])  # 内容体总大小
            progress = ProgressBar(content_size)
            with open(name, "wb") as f:
                for data in response.iter_content(chunk_size=chunk_size):
                    f.write(data)
                    progress.refresh(count=len(data))

    def size_format(self, sz):
        if sz < 1024:
            return (str(sz) + " B")
        if 1024 <= sz < 1048576:
            return (str(round(sz / 1024, 2)) + " KB")
        if 1048576 <= sz < 1073741824:
            return (str(round(sz / 1048576, 2)) + " MB")
        if sz >= 1073741824:
            return (str(round(sz / 1073741824, 2)) + " GB")
        return "ERROR SIZE"

    def url2name(self, url):
        url = url.split('/')[-1].replace('%20', ' ')
        url = url.replace('%28', '(').replace('%29', ')')
        return url

    def start(self):
        page = self._strat_page
        while page <= self._end_page:
            count = 0
            print("\n正在获取第{}页列表...".format(page))
            dic = self.get_list(page)

            for i in dic:
                if i["rating"] in self._rating:
                    count += 1
                    name = self.url2name(i["file_url"])
                    print("正在抓取第{}页, 第{}张:".format(page, count))
                    print("    文件名: {}".format(name))
                    print("    id: {}, 大小: {}, 尺寸: {} × {}".format(i["id"], self.size_format(int(i["file_size"])),
                                                                   i["width"], i["height"]))
                    name = "pics/" + name
                    self.get_pic(i["file_url"], name)
                    print("    下载完成!\n")
                else:
                    continue

            page += 1


if __name__ == "__main__":
    if 'pics' not in os.listdir(os.getcwd()):
        os.mkdir('pics')
    try:
        my_start_page = eval(input("请输入开始页码(不输入默认为1): "))
    except SyntaxError:
        my_start_page = 1
    try:
        my_end_page = eval(input("请输入结束页码(含该页, 不输入则默认为无结束限制): "))
    except SyntaxError:
        my_end_page = 100000

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
    print(my_rating)

    k = Konachan(start_page=my_start_page, end_page=my_end_page, rating=my_rating)
    k.start()
