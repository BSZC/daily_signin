# -- coding: utf-8 --
import requests
import time
import json
import os
from QYWX_Notify import QYWX_Notify
from io import StringIO

requests.packages.urllib3.disable_warnings()
sio = StringIO()


def nga_signin():
    uid = os.getenv('NGA_UID')
    token = os.getenv('NGA_TOKEN')
    url = 'https://ngabbs.com/nuke.php'
    headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 10; YAL-AL00 Build/HUAWEIYAL-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.106 Mobile Safari/537.36 Nga_Official/90021",
        "X-Requested-With": "gov.pianzong.androidnga",
    }
    if uid and token:
        uid = uid.split('&')
        token = token.split('&')
        if len(uid) != len(token):
            msg = "签到失败，UID和token个数不相等"
            QYWX_Notify().send("NGA签到信息", msg)
            raise Exception
        else:
            for i in range(len(uid)):
                data = {"access_token": token[i],
                        "uid": uid[i],
                        "t": round(time.time()),
                        "access_uid": uid[i],
                        "sign": "",
                        "app_id": "1010",
                        "__act": "check_in",
                        "__lib": "check_in",
                        "__output": "12"}
                req = requests.post(url, headers=headers, data=data, verify=False).content
                res = json.loads(req)
                message = res["msg"]
                if '先登录' in message:
                    sio.write(f'账号{i+1}:签到失败，token已失效或uid与token不对应')
                elif '已经' in message:
                    sio.write(f'账号{i+1}:今日已签过到')
                elif res['code'] == 0:
                    sio.write(f'账号{i+1}:签到成功')
                else:
                    sio.write(f'账号{i+1}签到错误:未知错误')
            msg = sio.getvalue()
            QYWX_Notify().send("NGA签到信息", msg)


if __name__ == '__main__':
    nga_signin()
