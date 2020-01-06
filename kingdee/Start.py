import configparser
import os
import time

import kingdeeOne,kingdeeTwo,Email

parent_dir = os.path.dirname(os.path.abspath(__file__))


config = configparser.RawConfigParser()
# 编码要设置成utf-8-sig而并不是utf-8
config.read(parent_dir+'/kingdee.config', encoding='utf-8-sig')
clubCookie = config.get('Kingdee', 'club')
vipCookie = config.get('Kingdee', 'vip')

if __name__ == '__main__':
        # club.kingdee.com
        club = kingdeeOne.play(clubCookie)
        
        # vip.kingdee.com
        time.sleep(2)
        vip = kingdeeTwo.play(vipCookie)
        if '签到成功' in club or '用户已签到' in club:
                # 成功
                Email.mail("金蝶社区 签到成功！","金蝶社区")
        else:
                # 失败
                Email.mail("金蝶社区 签到失败！", "金蝶社区")
        if '20'  in vip:
                # 成功
                Email.mail("金蝶云社区 签到成功！", "金蝶云社区")
        else:
                # 失败
                Email.mail("金蝶云社区 签到失败！", "金蝶云社区")

