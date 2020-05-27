# -*- coding: utf-8 -*-
import random
import requests,re,time
from Email import mail



def main(Cookie):
    r = requests.Session()
    # 进入官网获取cookies
    # 加入x-www-form-urlencoded头信息
    headers = {'Content-Type': 'application/x-www-form-urlencoded','Cookie':Cookie}
    # 账号密码
    # 获取登陆后的账号
    c = r.get(url="https://www.cunhua.nl/",headers=headers)
    # 获取formhash
    loginform = re.findall('name="formhash" value="(.*?)"', c.text)[0]
    print(loginform)
    qdUrl = "https://www.cunhua.nl/k_misign-sign.html?operation=qiandao&format=global_usernav_extra&formhash={}&inajax=1&ajaxtarget=k_misign_topb".format(loginform)
    # 签到
    c3 = r.get(url=qdUrl,headers=headers)
    print(c3.text)
    mail(Content=str(c3.text), Title='村花签到情况')
    # 挂机
    for i in range(0, 4320):
        c1 = r.get(url='https://cunhua.nl',headers=headers)
        time.sleep(20)
    r.close()



