# -*- coding: utf-8 -*-
import requests,chardet
from Email import mail

def main(User,PassWord):
        # 加入session
    r = requests.Session()
        # 进入官网获取cookies
        # 加入x-www-form-urlencoded头信息
    headers = {'Host': 'ji-c.pw',
                'Connection': 'keep-alive',
                'Content-Length': '43',
                'Accept': 'application/json, text/javascript, */*; q=0.01',
                'X-Requested-With': 'XMLHttpRequest',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36',
                'Sec-Fetch-Mode': 'cors',
                'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'Origin': 'https://ji-c.pw',
                'Sec-Fetch-Site': 'same-origin',
                'Referer': 'https://ji-c.pw/signin',
                'Accept-Encoding': 'gzip, deflate, br',
                'Accept-Language': 'zh-CN,zh;q=0.9'
    }
        # 账号密码
    data = 'email='+User+'&passwd='+PassWord+''
        # 获取登陆后的账号
    c = r.post(url='https://ji-c.pw/signin',data=data,headers=headers,verify=False)
        # 获取formhash
    print(chardet.detect(c.content))
    # ascii 解码
    headers1 = {'Host': 'ji-c.pw',
                'Connection': 'keep-alive',
                'Content-Length': '0',
                'Accept': 'application/json, text/javascript, */*; q=0.01',
                'X-Requested-With': 'XMLHttpRequest',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36',
                'Sec-Fetch-Mode': 'cors',
                'Origin': 'https://ji-c.pw',
                'Sec-Fetch-Site': 'same-origin',
                'Referer': 'https://ji-c.pw/user?ran=0.21882620098942573',
                'Accept-Encoding': 'gzip, deflate, br',
                'Accept-Language': 'zh-CN,zh;q=0.9'
                }
        # 签到
    c3 = r.post(url='https://ji-c.pw/user/checkin',headers=headers1,verify=False)
    Content = c3.content.decode('unicode_escape')
    mail(Content=Content,Title="几鸡流量签到情况")
    r.close()

