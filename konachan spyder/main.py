import re
import time
import requests

wait_time = 1  # 爬取每一张图片的间隔时间，默认为一秒(建议调大点，给网站减轻些压力吧（过于频繁可能会被封禁ip（我没试过
start_page = 1  # 从第几页开始爬取
end_page = 2  # 爬取到第几页结束（不包含该页）

my_headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
    'Host': 'konachan.net'
}


def get_pic(url, name):
    r = requests.get(url, headers=my_headers)
    with open(name, 'wb') as f:
        f.write(r.content)


def get_pic_link(url):
    r = requests.get(url, headers=my_headers)
    if 'This image has' in r.text:
        result = re.search(
            'This image has been resized. Click on the <a class="highres-show" href="(.*?)">View larger version</a>',
            r.text, re.S)
    else:
        result = re.search('id="note-container".*?src="(.*?)" width', r.text, re.S)
    return result.group(1)


def get_page(url):
    r = requests.get(url, headers=my_headers)
    result = re.findall('<a class="thumb" href="(.*?)" >', r.text, re.S)
    return result


def main():
    page = start_page
    my_url = 'https://konachan.net'
    while page < end_page:
        pics = get_page(my_url + '/post?page=' + str(page))
        id = 0
        for i in pics:
            id += 1
            print('正在抓取第' + str(page) + '页第' + str(id) + '张图片')

            true_url = get_pic_link(my_url + i)
            name = 'net_pics/Konachan.net -' + i.replace('/', ' ').replace('-', ' ') + '.jpg'
            get_pic(true_url, name)

            print('等待中...')
            time.sleep(wait_time)

        page += 1


if __name__ == '__main__':
    main()
