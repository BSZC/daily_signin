# -- coding: utf-8 --
import json
import requests


def csdn_signin(cookie):
    headers = {
        'cookie': cookie,
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4421.0 Safari/537.36 Edg/90.0.810.1'}
    signurl = "https://me.csdn.net/api/LuckyDraw_v2/signIn"
    resp = requests.post(signurl, headers=headers).content.decode(
        "unicode_escape")
    res = json.loads(resp)  # 将json转化为数组形式
    message = res['message']  # 返回签到的结果
    issign = res['data']['isSigned']
    if message == '成功' and issign:
        t = res['data']['msg']
        url = "https://me.csdn.net/api/LuckyDraw_v2/signInfo?product=&&type="
        resp1 = requests.get(url, headers=headers).content.decode("unicode_escape")
        resp1 = json.loads(resp1)  # 将json转化为数组形式
        msg = t + '\n' + resp1['data']['msg']
        signdays = resp1['data']['star']
        if signdays == 5:
            sign = requests.post("https://me.csdn.net/api/LuckyDraw_v2/goodLuck", headers=headers).content.decode(
                "unicode_escape")
            option = json.loads(sign)['data']['msg']
            msg = msg + '\n' + option
    else:
        msg = '签到失败，请检查cookies'
    return msg
