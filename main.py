import aiohttp
import asyncio
import time
import pickle
from path  import *
import re

from pajs import *
#设置递归深度，为了解决数据存储问题
import sys
sys.setrecursionlimit(10000)

from bs4 import BeautifulSoup

ans = []
num = 1761
from var import *





async def SingleDM(DM):
    async with aiohttp.ClientSession() as session:
        async with session.get(DM['url']) as resp:
            print(resp.status)
            html = await resp.text(encoding='ISO-8859-1')
            
            ans = html
            ans = ans.encode('ISO-8859-1')
            ans = ans.decode('gb2312','ignore')


            
            soup = BeautifulSoup(ans, 'html.parser')
            #print(ans)

            scripts = soup.find_all('script')
            for script in scripts:
                #print(script)

                ans = re.match('<script src="/playdata/*',str(script))
                #print(ans)
                if ans!=None:
                    #print(ans)
                    url = script.get('src')
                    url ='http://www.imomoe.in'+ url
                    print(url)
                    pJS = paJs()
                    pJS.url = url
                    pJS.start()
                    DM['video'] = pJS.list
                    DM['text'] = pJS.text
            #print(DM)
            global num
            print(num)
            #num = num +1 
            output = open(FileDir+'/dm/data' +str(num)+'.pkl', 'wb')
            num = num +1
            # Pickle dictionary using protocol 0.
            pickle.dump(DM, output)
            









#一页一页爬去动漫链接
async def spider(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            print(resp.status)
            html = await resp.text(encoding='ISO-8859-1')
            
            ans = html
            ans = ans.encode('ISO-8859-1')
            ans = ans.decode('gb2312','ignore')
            soup = BeautifulSoup(ans, 'html.parser')
            #print(ans)
            ul = soup.find_all(attrs={'class':'pics'})
            ul = ul[0]
            ul = ul.find('ul').find_all('li')

            DMlist = []


            for i in ul:

                ans = {}    



                tmp = i.find_all(attrs={ 'target':"_blank"})[0]


                href= tmp.get('href')
                href = href.replace('.html', '')
                href = href.replace('/view', '')
                href ='http://www.imomoe.in/player' + href + '-0-0.html'
                ans['url'] = href

                img = tmp.find('img')
                ans['name'] = img.get('alt')
                ans['imgUrl'] = img.get('src')

                #print(ans)
                DMlist.append(ans)

            #print(DMlist)

            #await SingleDM(DMlist[0])
                        #将变量存储到本地
            global num
            print(num)
            #num = num +1 
            output = open(FileDir+'/data' +str(num)+'.pkl', 'wb')
            num = num +1
            # Pickle dictionary using protocol 0.
            pickle.dump(DMlist, output)
            


            
            print(f"finished at {time.strftime('%X')}")


#批量处理动漫的源页面
async def ProDmTask(tasks):
    for task in tasks:
        await asyncio.wait(task)
        await asyncio.sleep(30)

#更具原页面，批量处理动漫的js，播放源


async def proDmJsT(data):
    for d in data:
        tasks = []
        for i in d:
            print(i)
            tmpT = SingleDM(i)
            tasks.append(tmpT)
        await asyncio.wait(tasks)
        await asyncio.sleep(6)
            



if __name__=="__main__":


    # DM={}
    # DM['url'] = 'http://www.imomoe.in/player/7898-0-0.html'
    # t = SingleDM([DM])

    step = 2

    # 第一步 进行基本所有动漫信息查询
    if step ==1:
        head = 'http://www.imomoe.in/so.asp?page='

        end = '&fl=0&pl=time'
        tasks = []
        for i in range(17, 61):
            task = []
            for j in range(i*10, (i+1)*10):
                print(j)
                url = head + str(j) + end

                print(url)
                t = spider(url)
                task.append(t)
            tasks.append(task)

            t = ProDmTask(tasks)


    # 第二步 进行单个动漫解析
    if step ==2:
        datas = []
        for i in range(120, 609):
            try:
                output = open(FileDir+'/dmList/data'+str(i)+'.pkl', 'rb')
                data=pickle.load(output)



                output.close()
                datas.append(data)
            except:
                print('error')
        print(len(datas))
        t = proDmJsT(datas)

            
                

    asyncio.run(t)