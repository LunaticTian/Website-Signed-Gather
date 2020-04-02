# -*- coding: utf-8 -*-
import random
import requests
import json
import time
from Email import mail
from itertools import product




# 斗鱼自动发送指定人员礼物

c = ''
# 斗鱼礼物接口
url = 'https://www.douyu.com/member/prop/send'
urlH5 = 'https://www.douyu.com/swf_api/h5room/9999'
cookies={}
# 存放cookie
list1 = []

def init(cookie):
    c = cookie
    for line in c.split(';'):
    #其设置为1就会把字符串拆分成2份
        name,value=line.strip().split('=',1)
        cookies[name]=value
    headers['Cookie'] = cookie


headers = {
            'Host': 'www.douyu.com',
            'Connection': 'keep-alive',
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Origin': 'https://www.douyu.com',
            'X-Requested-With':'XMLHttpRequest' ,
            'User - Agent': 'Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 65.0.3325.181Safari / 537.36',
            'Referer': 'https://www.douyu.com/9999',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9'
}

headersH5Rome = {
            'Host': 'www.douyu.com',
            'Connection': 'keep-alive',
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Origin': 'https://www.douyu.com',
            'X-Requested-With':'XMLHttpRequest' ,
            'User-Agent': 'Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 65.0.3325.181Safari / 537.36',
            'Referer': 'https://www.douyu.com/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
            'TE':'Trailers'
}
# 获取荧光棒数量/用以取代Selenium库相关代码
def getYGB():
    requests.get(url=urlH5,headers=headersH5Rome)
# 分发荧光棒
def mainApi(sum,idList,nubList):
    s = requests.Session()
    if sum == 0:
        for i in range(len(idList)):
            for nub in range(int(nubList[i])):
                data = 'dy=99b3bf61409e9782aee70daf00071501&prop_id=268&num=1&sid=' + cookies[
                    'acf_uid'] + '&did=204389&rid=' + idList[i] + '&is_jz=0'
                Result = s.post(url=url, data=data, headers=headers)
                k = Result.text
                json1 = json.loads(k)
                list1.append(json1['msg'])
                time.sleep(1)

    if sum != 0:
        si = 0
        for i ,id in product(range(999),idList):
            data = 'dy=99b3bf61409e9782aee70daf00071501&prop_id=268&num=1&sid=' + cookies['acf_uid'] + '&did=204389&rid=' + id + '&is_jz=0'
            Result = s.post(url=url, data=data, headers=headers)
            k = Result.text
            json1 = json.loads(k)
            list1.append(json1['msg'])
            si = si + 1
            if si == sum:
                break
            time.sleep(1)

def main(cookies,sum,idList,nubList):
    init(cookie=cookies)
    getYGB()
    mainApi(sum,idList,nubList)
    mail(str(list1),"斗鱼签到情况")









