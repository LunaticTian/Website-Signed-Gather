# Kingdee部署教程

## 前期准备
* python 3+ 
 
	[ptyhon3](https://www.python.org/)，注意此脚本需要python3以上。
	
	[Windows安装](https://www.cnblogs.com/weven/p/7252917.html)
	[Linux](https://blog.csdn.net/zhangdongren/article/details/82685932)

* 安装*request*依赖

	控制台输入：
	```
	pip install request
	```
* chome | Firefox | 其他主流浏览器

## 账号准备
	
1. 分别打开[https://club.kingdee.com/](https://club.kingdee.com/)以及[http://vip.kingdee.com/](http://vip.kingdee.com/)，登录需要自动签到的账号。

2. 打开浏览器控制台，找到Network，分别再次刷新[https://club.kingdee.com/](https://club.kingdee.com/)以及[http://vip.kingdee.com/](http://vip.kingdee.com/)，找到

3. 找到*cookie*，分别复制保存其值其值。
![](http://img.lunatic.wang/kingdee1.png)
![](http://img.lunatic.wang/kingdee2.png)

## 配置关键信息

### 配置Cookie
* 打开脚本文件夹中的kingdee.conf

```
[Kingdee]
# club.kingdee.com
club = 
# club.kingdee.com
vip = 
```

* 复制Cookie到club以及vip中


### 配置邮件

```
[Email]
User = kingdeecheck@126.com
PassWord = test2019
Purpose = 12345@qq.com
```

其中有内置的kingdeecheck@126.com邮件，只需更改Purpose为用户自己的邮件即可。


## 签到

	python3 Start.py

### linux
确认linux CRON为开启状态。 
	
	sudo crontab -e
	01 01 * * * python3 pwd/Start.py #pwd为脚本放置的目录
	
### Windows
	打开OnTimer.exe
	右键添加
	类型选择:DOS运行
	次数:999999999
	时间：每日
	内容：python3 pwd/Start.py #pwd为脚本放置的目录
	选择新创建的任务，右键执行测试是否正常执行

![](http://img.lunatic.wang/kingdee3.png)



## 错误代码

如若在自动签到中出现错误，错误代码以及解决办法如下。

在控制台中执行*start.py*，控制台会输出代码：

1.	

		{"result":false,"msg":"您目前未登录，无法使用此功能"}
		Traceback (most recent call last):
		  File ".\Start.py", line 22, in <module>
		    vip = kingdeeTwo.play(vipCookie)
		  File "C:\Users\Lovef\Desktop\kingdee\kingdeeTwo.py", line 35, in play
		    headers['X-CSRF-TOKEN']= cookies['CSRF-TOKEN']
		KeyError: 'CSRF-TOKEN'	

请检查复制的cookie，重新写入。


----------


2. 
		{"result":false,"msg":"您目前未登录，无法使用此功能"}
		{"errorCode":205,"message":"ç½é¡µä¿¡æ¯å¤±æï¼è¯·éæ°ç»å½ååè¯ï¼"}

登录已失效，重新登录kingdee，获取cookie，写入


----------

如果出现程序错误，请联系程序作者！


