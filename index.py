# -- coding: utf-8 --
from pojie import pojie
from QYWX_Notify import QYWX_Notify
import os

pj_cookie = os.getenv('PJ_COOKIE').strip()
corpid = os.getenv("QYWX_CORPID").strip()
corpsecret = os.getenv("QYWX_CORPSECRET").strip()
agentid = os.getenv("QYWX_AGENTID").strip()

if pj_cookie:  # 吾爱破解签到
    pj_msg = pojie(pj_cookie)
    pj_notify = QYWX_Notify(corpid, corpsecret, agentid)
    pj_notify.send('吾爱破解签到信息', pj_msg)
