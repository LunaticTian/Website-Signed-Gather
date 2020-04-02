import cunhua,jiji,Douyu,configparser,hashlib,v2ex
from urllib import parse
import os, sys
from Email import mail

# mail("定时任务","Lunatic_Ubuntu")
parent_dir = os.path.dirname(os.path.abspath(__file__))
config = configparser.RawConfigParser()
config.read(parent_dir+'/Setting.conf', encoding='utf-8-sig')
# Setting
dDouyu = config.get('Setting','douyu')
cCunhua = config.get('Setting','cunhua')
jJiji = config.get('Setting','jiji')
V2ex = config.get('Setting','v2ex')

# cunhua
cunhuaUser = None
cunhuaPassWord = None
if cCunhua == '1':
    cunhuaUser = config.get('cunhua','User')
    cunhuaUser = parse.quote(cunhuaUser)
    cunhuaPassWord = config.get('cunhua','PassWord')
    m = hashlib.md5()
    m.update(cunhuaPassWord.encode())
    str_md5 = m.hexdigest()
    cunhuaPassWord = str_md5

# jiji
jijiUser = None
jijiPassWord = None
if jJiji == '1':
    jijiUser = config.get('jiji','User')
    jijiUser = parse.quote(jijiUser)
    jijiPassWord = config.get('jiji','PassWord')

# douyu
douyuCookie = None
douyuList = None
douyuNum = None
douyuSum = None
if dDouyu == '1':
    douyuCookie = config.get('douyu','cookie')
    oldlist = config.get('douyu','list')
    douyuList = str(oldlist).split('-')
    oldnum = config.get('douyu','num')
    douyuNum = str(oldnum).split('-')
    oldSum = config.get('douyu','sum')
    douyuSum = int(oldSum)

# v2ex
v2exC = None
if V2ex == '1':
    v2exC = config.get('v2ex','cookie')



if __name__ == '__main__':
    if dDouyu == '1':
        Douyu.main(cookies=douyuCookie,sum=douyuSum,idList=douyuList,nubList=douyuNum)
    if jJiji == '1':
        jiji.main(jijiUser, jijiPassWord)
    if V2ex == '1':
        v2ex.main(v2exC)
    if cCunhua == '1':
        cunhua.main(cunhuaUser,cunhuaPassWord)
    




