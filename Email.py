import smtplib
from email.mime.text import MIMEText
from email.header import Header
import time
import configparser



config = configparser.ConfigParser()
# 编码要设置成utf-8-sig而并不是utf-8
config.read('Setting.conf', encoding='utf-8-sig')
User = config.get('Email', 'User')
PassWord = config.get('Email', 'PassWord')
Purpose = config.get('Email', 'Purpose')

def mail(Content,Title):
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
    print('邮件发送成功email has send out !')



