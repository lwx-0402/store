import pymysql
host="localhost"
user="root"
password=""
database="money"

def updata(sql ,param):
    con=pymysql.connect(host=host,user=user,password=password,database=database)
    cursor=con.cursor()
    cursor.executemany(sql,param)
    con.commit()
    cursor.close()
    con.close()
sql="INSERT INto many (username,age,money) VALUES(%s,%s,%s)"
param=[["贾生",47,"50000"],
       ["马云",58,1000000],
       ["马化腾",57,1000202],
       ["付光旭",20,560304],
       ["穆子康",24,230023],
       ["杜会萌",25,204892]]
updata(sql,param)




def find(sql,param,mode="all",size="1"):

    con=pymysql.connect(host=host,user=user,password=password,database=database)
    cursor=con.cursor()
    cursor.execute(sql,param)
    con.commit()
    if mode=="all":
        return cursor.fetchall()
    elif mode=="one":
        return cursor.fetchone()
    elif mode=="many":
        return cursor.fetchmany(size)
    cursor.close()
    con.close()





sql="select money from many"
param=[]
data=find(sql,param,mode="many",size=6)
print(data)
a=0
for i in data:
    a=a+sum(i)
print ("资产总和为",a)





