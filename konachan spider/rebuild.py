import re
import time
import requests
from lxml import etree


class Konachan:
    def __init__(self, start_page = 1, end_page = 10):
        self._headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36',
            'Host': 'konachan.net',
            'page': 3
        }
        self._strat_page = start_page
        self._end_page = end_page
        self._url = 'http://konachan.com/post.json'

    def get_json(self, page = 3):
        r = requests.get('https://konachan.com/post.json')
        print(r.json)

if __name__ == "__main__":
    kona = Konachan()
    kona.get_json()