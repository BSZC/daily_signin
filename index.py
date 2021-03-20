# -- coding: utf-8 --
from pojie import pojie_signin
from QYWX_Notify import QYWX_Notify
from csdn import csdn_signin
import os

corpid = os.getenv("QYWX_CORPID").strip()
corpsecret = os.getenv("QYWX_CORPSECRET").strip()
agentid = os.getenv("QYWX_AGENTID").strip()
pj_cookie = os.getenv('PJ_COOKIE').strip()
csdn_cookie = os.getenv('CSDN_COOKIE').strip()

# if pj_cookie and pj_cookie is not None:  # 吾爱破解签到
#     pj_msg = pojie_signin(pj_cookie)
#     pj_notify = QYWX_Notify(corpid, corpsecret, agentid)
#     pj_notify.send('吾爱破解签到信息', pj_msg)

if csdn_cookie and csdn_cookie is not None:
    csdn_msg = csdn_signin(csdn_cookie)
    csdn_notify = QYWX_Notify(corpid, corpsecret, agentid)
    csdn_notify.send('csdn签到信息', csdn_msg)