# import pymysql
# con=pymysql.connect(host="localhost",user="root",password="",database="销售数据库")
# cusor=con.cursor()
# sql="insert into article values (%s,%s,%s,%s)"
# param=["s006","冰箱",5000,10]
# num=cusor.execute(sql,param)
# print("影响了",num,"行数据")
# con.commit()
# con.close()
# cusor.close()


# import pymysql
# con=pymysql.connect(host="localhost",user="root",password="",database="销售数据库")
# cusor=con.cursor()
# sql="delete from article where 商品名=%s"
# param=["电冰箱"]
# num=cusor.execute(sql,param)
# print("影响了",num,"行数据")
# con.commit()
# con.close()
# cusor.close()

# import pymysql
# con=pymysql.connect(host="localhost",user="root",password="",database="销售数据库")
# cusor=con.cursor()
# sql="update  article set 单价=单价+200 where 商品名=%s"
# param=["洗衣机"]
# num=cusor.execute(sql,param)
# print("影响了",num,"行数据")
# con.commit()
# con.close()
# cusor.close()

import pymysql
con=pymysql.connect(host="localhost",user="root",password="",database="销售数据库")
cusor=con.cursor()
sql="select * from article "
# param=["电冰箱"]
num=cusor.execute(sql)
data=cusor.fetchall()
for i in data:
    print(i)
print("影响了",num,"行数据")
con.commit()
con.close()
cusor.close()