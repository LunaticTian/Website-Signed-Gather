# -*- coding: utf-8 -*-
import smtplib
from email.mime.text import MIMEText
from email.header import Header
import time
import configparser
import requests
import os

parent_dir = os.path.dirname(os.path.abspath(__file__))
config = configparser.ConfigParser()
# 编码要设置成utf-8-sig而并不是utf-8
config.read(parent_dir+'/Setting.conf', encoding='utf-8-sig')
push = config.get('Setting', 'Push')
# 邮箱推送
if push == '0':
    User = config.get('Email', 'User')
    PassWord = config.get('Email', 'PassWord')
    Purpose = config.get('Email', 'Purpose')
# 微信推送
if push == '1':
    SCKEY = config.get('wechat', 'SCKEY')

def mail(Content,Title):
    if push == '1':
        url = "https://sc.ftqq.com/"+SCKEY+".send?text="+time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())+" : "+Title+"&desp="+Content
        print(url)
        requests.get(url)
        print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())+" 微信推送")
    if push == '0':
        msg = MIMEText(Content, 'plain', 'utf-8')
        msg['Subject'] = Header(time.strftime('%Y-%m-%d ', time.localtime())+' : '+Title, 'utf-8')
            # 报错原因是因为“发件人和收件人参数没有进行定义
        msg['from'] = User
        msg['to'] = Purpose
        smtp = object
        import platform
        if(platform.python_version() < '3.7'):
            # 阿里云封了25端口，改为其他端口
            smtp = smtplib.SMTP_SSL()
            smtp.connect('smtp.126.com',465)
        else:
            #python 3.7
            smtp = smtplib.SMTP_SSL(host='smtp.126.com',port=465)
            smtp.connect(host='smtp.126.com', port=465)
        smtp.login(User, PassWord)
        smtp.sendmail(User, Purpose, msg.as_string())
        smtp.quit()
        print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()) + ': 邮件发送成功email has send out !')



