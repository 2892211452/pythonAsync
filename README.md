# pythonAsync

- 使用协程的一个典型开发流程，
- 这里我主要分层来开发，因为怕中间流程出异常，所以使用这种办法来开发，有利于掌握进度



## 目录

```
├── dataTest.py                            --测试本地数据， 加载与保存
├── dm                                     --单个动漫的数据存储
├── dmList                                 --动漫目录
├── dump-dm-202007091720.sql               --数据库
├── main.py                                --主程序
├── mysqlConect.py                         --将数据插入数据库
├── pajs.py                                --爬虫解析
├── path.py                                --路径包
├── __pycache__
├── range.py
├── README.md
└── var.py
```


## 说明 
关于数据， dm 里面有个text是樱花动漫得js接口得数据，里面蕴含了如何解析动漫数据得一些基本指标，有些是直接的mp4资源，有些是腾讯的播放源地址，但是还有很多是各种网站比如优酷的转载，所以这里只有解析的代码，我有将js存下来，但是具体解析我没做。
一个娱乐项目，乐一乐。

例如这样的数据格式
```
http://www.imomoe.in/player/257-0-0.html
怪盗小丑第四季
[]
以下是js数据接口 需要一个做资源解析的。
var VideoListJson=[['се©А',['\u7B2C01\u96C6$XMTc0NjY0NTM0MA==$youku','\u7B2C02\u96C6$XMTc1NDk2OTU4OA==$youku','\u7B2C03\u96C6$XMTc2MzQ4NDQyOA==$youku','\u7B2C04\u96C6$XMTc3MjU5MTIyNA==$youku','\u7B2C05\u96C6$XMTc4MTczMDAzNg==$youku','\u7B2C06\u96C6$XMTgwOTM0NjIxMg==$youku','\u7B2C07\u96C6$XMTgxODcwNzQ4NA==$youku','\u7B2C08\u96C6$XMTgyODUzMjIzMg==$youku','\u7B2C09\u96C6$XMTgzOTI5Nzc4MA==$youku','\u7B2C10\u96C6$XMTg1MDMxMDY0NA==$youku','\u7B2C11\u96C6$XMTg2MTA1NDQ2MA==$youku','\u7B2C12\u96C6$XMTg3MjM3MDA1Mg==$youku','\u7B2C13\u96C6$XMTg4NDE0ODM3Mg==$youku']],['qvod',['\u7B2C01\u96C6$10599404$bilibili','\u7B2C02\u96C6$10779283$bilibili','\u7B2C03\u96C6$10934046$bilibili','\u7B2C04\u96C6$11092110$bilibili','\u7B2C05\u96C6$11248871$bilibili','\u7B2C06\u96C6$11411491$bilibili','\u7B2C07\u96C6$11576176$bilibili','\u7B2C08\u96C6$11763797$bilibili','\u7B2C09\u96C6$11923380$bilibili','\u7B2C10\u96C6$12091435$bilibili','\u7B2C11\u96C6$12263907$bilibili','\u7B2C12\u96C6$12448119$bilibili','\u7B2C13\u96C6$12632396$bilibili']],['qvod',['\u7B2C01\u96C6$LTGxLpb8bKoNiaicM$pptv','\u7B2C02\u96C6$K3FU0zuhEUibyMJg$pptv','\u7B2C03\u96C6$fVg7uCCG9jSXFX0$pptv','\u7B2C04\u96C6$ScqtKpL4aKYJhib8$pptv','\u7B2C05\u96C6$micXXVDwvFlS3NZ0$pptv','\u7B2C06\u96C6$1YFj4Miajmtg7uSE$pptv','\u7B2C07\u96C6$9T0iaoYnia2xl8ibmI$pptv','\u7B2C08\u96C6$49mibPSU2L23QTrY$pptv','\u7B2C09\u96C6$namODfVmX50AfuY$pptv','\u7B2C10\u96C6$X3NT0LiazquhLyTE$pptv','\u7B2C11\u96C6$uaiaODfVmX50AfuY$pptv','\u7B2C12\u96C6$9cmwLxdIMWicSULg$pptv','\u7B2C13\u96C6$4UwrqJDLsvBT0Tk$pptv']]],urlinfo='http://'+document.domain+'/player/257-<from>-<pos>.html';
```