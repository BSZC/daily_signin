import requests
import json
import os


class QYWX_Notify:
    def __init__(self):
        self.corpid = os.getenv("QYWX_CORPID")
        self.corpsecret = os.getenv("QYWX_CORPSECRET")
        self.agentid = os.getenv("QYWX_AGENTID")
        self.access_token = self.__get_access_token()

    def __get_access_token(self):
        url = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken'
        params = {
            'corpid': self.corpid,
            'corpsecret': self.corpsecret
        }
        resp = requests.get(url, params=params)
        resp.raise_for_status()
        resp_json = resp.json()
        if 'access_token' in resp_json.keys():
            return resp_json['access_token']
        else:
            raise Exception('Please check if corpid and corpsecret are correct \n' + resp.text)

    def send(self, title, text):
        url = 'https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token=' + self.access_token
        data = {
            "touser": "@all",
            "agentid": self.agentid,
            "msgtype": "textcard",
            "textcard": {
                "title": title,
                "description": text,
                "url": "URL"},
            "safe": 0,
            "enable_id_trans": 0,
            "enable_duplicate_check": 0,
            "duplicate_check_interval": 1800
        }

        resp = requests.post(url, data=json.dumps(data))
        resp.raise_for_status()
        return resp.json()
