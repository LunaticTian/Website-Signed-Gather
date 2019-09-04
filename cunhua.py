import requests,re,time
from Email import mail


def main(User,PassWord):
    r = requests.Session()
        # 进入官网获取cookies
    r.get(url='https://cunhua.me')
        # 加入x-www-form-urlencoded头信息
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        # 账号密码
    data = 'fastloginfield=username&username='+User+'&password='+PassWord+'&quickforward=yes&handlekey=ls'
        # 获取登陆后的账号
    c = r.post(url='https://www.cunhua.me/member.php?mod=logging&action=login&loginsubmit=yes&infloat=yes&lssubmit=yes&inajax=1',data=data,headers=headers)
        # 获取formhash
    c2 = r.get(url='https://www.cunhua.me/plugin.php?id=dc_signin')

    a = re.findall('formhash=(.*?)"',c2.text)
        # a[0]：formhash
        # 签到
    data2 = 'formhash='+a[0]+'&signsubmit=yes&handlekey=signin&emotid=8&referer=https%3A%2F%2Fwww.cunhua.cc&content=%E6%AF%8F%E5%A4%A9%E8%90%8C%E8%90%8C%E5%93%92%7E%7E'
    c3 = r.post(url='https://www.cunhua.me/plugin.php?id=dc_signin:sign&inajax=1',data=data2,headers=headers)
    mail(Content=str(c3.text),Title='村花签到情况')
    for i in range(0,4320):
        c1 = r.get(url='https://cunhua.me')
        time.sleep(20)
    r.close()



