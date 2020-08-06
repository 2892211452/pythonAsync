
import pymysql
from path import *
from dataTest import *



# 打开数据库连接
db = pymysql.connect("localhost","root","156354","dm" )
 
# 使用cursor()方法获取操作游标 
cursor = db.cursor()
 
# SQL 插入语句

def insert(title, url, img, src):
    sql = """insert  into dm (title ,url , img ,src )
                        value('titleValue', 'urlValue','imgValue',"srcValue");"""
    sql = sql.replace('titleValue', title)
    sql = sql.replace('urlValue', url)
    sql = sql.replace('imgValue', img)
    sql = sql.replace('srcValue', src)

    try:
        # 执行sql语句
        cursor.execute(sql)
        # 提交到数据库执行
        db.commit()
    except:
        # 如果发生错误则回滚
        db.rollback()
        
        # 关闭数据库连接
        # db.close()



def select(name):
    sql = """
select * from dm where title  like '%name%';
"""
    sql = sql.replace('name', name)

    try:
        # 执行sql语句
        cursor.execute(sql)
        # 提交到数据库执行
        results = cursor.fetchall()
        res =[]
        for row in results:
            title = row[0]
            print(title)
            url = row[1]
            image = row[2]
            src = row[3]
            res.append({
                'title':title,
                'url':url,
                'image':image,
                'src':src,
            })
        return res
       # 打印结果
            # print(row)
    except:
        # 如果发生错误则回滚
        db.rollback()
        
        # 关闭数据库连接
        # db.close()




if __name__ =="__main__":
    for i in range(1, 7266):
        try:
            output = open(FileDir+'/dm/data'+str(i) +'.pkl', 'rb')


            data=pickle.load(output)
            src = str(data['video'])
            title = data['name']
            url = data['url']
            img = data['imgUrl']
            insert(title, url, img, src)
            if i % 10 ==0:
                print(i)
        except:
            print('error')
    

    #select('海贼')

