# -*- coding: utf-8 -*-
import requests


cookies = {}

def init(cookie):
    c = cookie
    for line in c.split(';'):
    #其设置为1就会把字符串拆分成2份
        name,value=line.strip().split('=',1)
        cookies[name]=value

headers = {
    'Host': 'vip.kingdee.com',
    'Connection': 'keep-alive',
    'Content-Length': '2',
    'Accept': 'application/json, text/plain, */*',
    'Origin': 'https://vip.kingdee.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
    'Content-Type': 'application/json;charset=UTF-8',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Referer': 'https://vip.kingdee.com/',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,zh-TW;q=0.8,en;q=0.7'
}




# https://vip.kingdee.com/
def play(cookie):
    init(cookie)
    headers['X-CSRF-TOKEN']= cookies['CSRF-TOKEN']
    headers['Cookie'] = cookie
    data = '{}'
    cont = requests.post(url='https://vip.kingdee.com/api/checkins',headers=headers,data=data)
    res = cont.text.encode('utf-8').decode('unicode_escape')
    print(res)
    return res

# if __name__ == '__main__':
#     play()

