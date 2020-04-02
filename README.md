# Website-Signed-Gather
斗鱼(douyu)荧光棒自动赠送，粉丝牌保牌升级，村花(cunhua)自动签到/增加在线时间(挂机)，几鸡(SSR)流量签到，v2ex签到，金蝶签到(kingdee)。邮件提醒，微信推送查看签到情况！
陆续增加其他网站签到工具.....

## 适用范围
* 斗鱼(douyu.com)粉丝牌保牌
* 村花(cunhua.cc)自动签到领取金币，同时保持24小时在线，增加在线时间
* 几鸡(jj-b.pw)自动签到领取SS流量
* v2ex(v2ex.com)自动签到
* 金蝶社区签到(kingdee)
* 逐步增加

## 更新日志

* 2019/08/15 V0.1
* 2019/08/19 解决斗鱼签到未登录问题
* 2019/08/23 解决村花修改登录模块问题
* 2019/09/25 增加微信推送功能
* 2019/11/05 增加V2EX签到功能
* 2020/01/03 增加金蝶签到(kingdee)
* 2020/04/02 优化代码，去除Douyu Selenium模块
  * 通过分析[binux](https://github.com/binux/qiandao)代码优化，重写Douyu模块

## 相关依赖

* Python 3+
	* requests
* Douyu
	* ~~Chrome~~
	* ~~Selenium~~
	* ~~Webdriver~~
	

~~**说明：斗鱼粉丝牌签到部分涉及Selenium，用到此部分者需要安装相关依赖，如若不需，则安装requests即可。**~~

## 环境配置
### ~~Windows~~

* ~~[安装教程](https://www.cnblogs.com/eternal1025/p/8880245.html)~~
### ~~Linux~~
* ~~[安装教程](https://blog.csdn.net/zzzcl112/article/details/80470884)~~

### 以上环境配置通过4/2日更新已无意义。



## 准备步骤

* 准备几鸡，村花账号一个(账号，密码)
* (1/2)准备[Server酱](http://sc.ftqq.com)SCKEY码一个
* (2/2)或者准备126邮箱一个，且开启smtp，获得第三方登录密码
* 准备Douyu Cookie
	* 登录douyu，输入账号密码。
	* 呼出浏览器控制台，选择Network
	* 找到Name为rtpv的请求，复制Request Headers中的cookie部分
	* 记录需要签到粉丝牌的直接间号
## Setting.conf 参数说明


### Setting

**功能选择**

----------

#### 金蝶

<details>

<summary>金蝶</summary>



[金蝶使用部署方法](/kingdee)

ps:金蝶签到暂未合并与签到程序中，后续会进行合并。

</details>

----------


* push：选择推送方式 0为邮箱推送，1为微信推送 例:1

需要开启的功能，后置为1，不需要开启的功能后置为0

* cunhua：村花开关 例：1
* jiji:几鸡开关 例：1
* douyu:斗鱼开关 例：0
* v2ex:v2ex开关 例：1

### Email
* User:126邮箱账号
* PassWord:126第三方登录密码
* Purpose:绑定微信QQ邮箱提醒的邮箱

### cunhua/jiji

* User:网站账号
* PassWord:网站密码

### V2EX

* cookie:V2EX获取到的cookie，在网页控制台获得。

### 斗鱼

* cookie:从控制台中复制的cookie后面的内容，例：dy_did=dc7f6108031d3a0b34336338651501; acf_did=dc7f6108031d3a0b243240091501; smidV2   **后面还有很多，示例只是截取其中一部分**
* list：需要送荧光棒的主播间，输入格式为 123-65841-12354-78546

**斗鱼签到有两种方式**

1.指定房间赠送方式  2.平均保牌方式

两种方式的区别在于：方式一能够指定房间赠送指定数量荧光棒，有助于低等级升级。方式二则是平均粉丝牌给list中的直播间，保牌。

功能选择：1,sum必须填写0，且num中按照list中直播间的顺序写明送给每个直播间的数量，但总数不能超过荧光棒总数，如若我有100，我需要给“78546”直播间60荧光棒用于快速升级，“123”直播间20个荧光棒，其余直播间10个，则：20-10-10-60

2.num可不填写，默认为0，sum中填写自身荧光棒的总数。


* num：方式一的赠送数量，例：20-10-10-60，则sum填写0
* sum： 方式二中的总数，默认num为0，例：100

#### 实例 方式一

list = 123-321-32154</br>
num = 10-20-30</br>
sum = 0</br>

#### 实例 方式二

list = 123-321-32154</br>
num = 0</br>
sum = 60</br>




## 使用说明

配置好[Setting.conf]()，即可启动Start.py


**python Start.py**

签到无论成功失败，都会在邮件中说明成功，或者失败的原因。


## 结果返回

结果没有做处理，所以返回的是原生结果，后面应该会优化这部分，有兴趣的朋友也可以自己尝试修改。

## 效果图



### 微信推送
![](http://cdn.lunatic.wang/wecatpush.jpg)
![](http://cdn.lunatic.wang/wecat1.jpg)
![](http://cdn.lunatic.wang/wecat2.jpg)


### 邮箱提醒

![](http://img.lunatic.wang/qd1.jpg)
![](http://cdn.lunatic.wang/qd.jpg)

### 查看内容

![](http://img.lunatic.wang/qd2.jpg)
![](http://img.lunatic.wang/qd3.jpg)
![](http://img.lunatic.wang/qd4.jpg)
![](http://img.lunatic.wang/qd5.jpg)
![](http://img.lunatic.wang/qd6.jpg)
![](http://img.lunatic.wang/qf7.jpg)

