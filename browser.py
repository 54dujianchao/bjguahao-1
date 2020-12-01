#!/usr/bin/env python
# -*- coding: utf-8


import pickle
import requests


class Browser(object):
    """
    浏览器
    """

    def __init__(self):
        self.session = requests.Session()
        self.session.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36',
            'Content-Type': 'application/json; charset=UTF-8',
            'Accept': 'application/json, text/plain, */*',
            'Accept-Encoding': 'gzip,deflate,br',
            'Accept-Language': 'zh-CN, zh;q = 0.9',
            'Connection': 'keep-alive',
            'Host': 'www.114yygh.com',
            'Referer': 'https://www.114yygh.com/',
            'Request-Source': 'PC',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin'
        }

    def load_cookies(self, path):
        with open(path, 'rb') as f:
            self.session.cookies = requests.utils.cookiejar_from_dict(pickle.load(f))

    def save_cookies(self, path):
        with open(path, 'wb') as f:
            cookies_dic = requests.utils.dict_from_cookiejar(self.session.cookies)
            pickle.dump(cookies_dic, f)

    def get(self, url, data):
        """
        http get
        """
        pass
        response = self.session.get(url)
        if response.status_code == 200:
            self.session.headers['Referer'] = response.url
        return response

    def post(self, url, data):
        """
        http post
        """
        response = self.session.post(url, json=data)
        if response.status_code == 200:
            self.session.headers['Referer'] = response.url
        return response
        