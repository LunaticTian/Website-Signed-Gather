# -*- coding: utf-8 -*-
import requests


cookies = {}

def init(cookie):
    c = cookie
    for line in c.split(';'):
    #其设置为1就会把字符串拆分成2份
        name,value=line.strip().split('=',1)
        cookies[name]=value

    headers['Cookie'] = cookie

headers = {
            'Host': 'club.kingdee.com',
            'Connection': 'keep-alive',
            'Accept': '*/*',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Origin': 'https://club.kingdee.com/',
            'X-Requested-With':'XMLHttpRequest' ,
            'User - Agent': 'Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 65.0.3325.181Safari / 537.36',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Referer': 'https://club.kingdee.com/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9,zh-TW;q=0.8,en;q=0.7'
}

def play(cookie):
    init(cookie)
    cont = requests.get(url='https://club.kingdee.com/club/new_checkin_reward',headers=headers)
    res = cont.text.encode('utf-8').decode('unicode_escape')
    print(res)
    return res




# if __name__ == '__main__':
#     play()