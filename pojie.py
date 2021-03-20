# -- coding: utf-8 --
# 吾爱破解签到
import requests
from pyquery import PyQuery as pq


def pojie_signin(pj_cookie):
    url1 = 'https://www.52pojie.cn/home.php?mod=task&do=apply&id=2'
    url2 = 'https://www.52pojie.cn/home.php?mod=task&do=draw&id=2'
    headers = {'cookie': pj_cookie,
               "ContentType": "text/html;charset=gbk",
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4265.0 Safari/537.36 Edg/87.0.644.4'}
    requests.get(url1, headers=headers)
    req = requests.get(url2, headers=headers).text
    doc = pq(req)
    un = doc('.vwmy a').text()
    msg = doc('#messagetext p').text()
    if '不是进行中的任务' in msg:
        msg = '今日已签到'
    elif '恭喜' in msg:
        msg = '签到成功'
    msg = un + '\n' + msg
    return msg
