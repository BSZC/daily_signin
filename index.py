# -- coding: utf-8 --
import os
import re
from pojie import pojie_signin
from QYWX_Notify import QYWX_Notify
from csdn import csdn_signin
from tyyp import tyyp_signin

corpid = os.getenv("QYWX_CORPID").strip()
corpsecret = os.getenv("QYWX_CORPSECRET").strip()
agentid = os.getenv("QYWX_AGENTID").strip()
notify = QYWX_Notify(corpid, corpsecret, agentid)
pj_cookie = os.getenv('PJ_COOKIE').strip()
csdn_cookie = os.getenv('CSDN_COOKIE').strip()
tyyp_username = os.getenv('TYYP_USRNAME').strip()
tyyp_psw = os.getenv('TYYP_PSW').strip()

if pj_cookie:  # 吾爱破解签到
    pj_msg = pojie_signin(pj_cookie)
    notify.send('吾爱破解签到信息', pj_msg)

if csdn_cookie:  # CSDN签到
    csdn_msg = re.findall(r'UserNick=(.+?);', csdn_cookie)[0] + '\n' + csdn_signin(csdn_cookie)
    notify.send('csdn签到信息', csdn_msg)

if tyyp_username and tyyp_psw:  # 天翼云盘签到
    try:
        tyyp_username = tyyp_username.split('&')
        try:
            tyyp_psw = tyyp_psw.split('&')
        except:
            notify.send('天翼云盘签到错误', '密码数量为1或漏写&')
            raise Exception
        if len(tyyp_username) != len(tyyp_psw):
            notify.send('天翼云盘签到错误', '账号密码数量不匹配')
            raise Exception
        for i in range(len(tyyp_username)):
            tyyp_msg = f'账号{i + 1}:{tyyp_username[i]}\n' + tyyp_signin(tyyp_username[i], tyyp_psw[i])
            tyyp_msg += '\n'
    except:
        tyyp_msg = tyyp_username + '\n' + tyyp_signin(tyyp_username, tyyp_psw)
    notify.send('天翼云盘签到信息', tyyp_msg)
