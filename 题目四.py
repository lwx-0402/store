#i.	定义了一个学生类：属性:学号，姓名，年龄，性别，身高，体重，成绩，家庭地址，电话号码。行为：学习（要求参数传入学习的时间），
# 玩游戏（要求参数传入游戏名），编程（要求参数传入写代码的行数），数的求和（要求参数用变长参数来做，返回求和结果）
class Student:
    __sid=None
    __sName=None
    __sSex=None
    __sHeight=None
    __tiZhong=None
    __chengJi=None
    __diZhi=None
    __dianHua=None

    def xueXi(self,date):
        print("在",date,"开始学习")

    def youXi(self,Gname):
        print("游戏名称为：",Gname)

    def bianCheng(self,hang):
        print("共编写了",hang,"代码")

    def qiuHe(self,*shu):
        he=0
        for i in shu:
            he=he+i
        return he

c=Student()
print(c.qiuHe(30,12,16,10))

#ii.	车类：属性：车型号，车轮数，车身颜色，车重量，油箱存储大小 。功能：跑（要求参数传入车的具体功能，比如越野，赛车）
#创建：法拉利，宝马，铃木，五菱，拖拉机对象

class Autombile:
    __aid=None
    __aLun=None
    __acolor=None
    __aZhongLiang=None
    __aSeiz=None

    def setAid(self,aid):
        self.__aid=aid

    def getAid(self):
        return self.__aid

    def Go(self,gongNeng):
        print(self.__aid,"可以",gongNeng)

# c=Autombile()
# c.setAid("法拉利")
# c.Go("装B，炫富和烧钱")
#
# c1=Autombile()
# c1.setAid("宝马")
# c1.Go("兜风")
#
# c2=Autombile()
# c2.setAid("铃木")
# c2.Go("干啥我也不知道")
#
# c3=Autombile()
# c3.setAid("五菱")
# c3.Go("飙车，漂移，品质值得保证")
#
# c4=Autombile()
# c4.setAid("拖拉机")
# c4.Go("拉货")

#iii.	笔记本：属性：型号，待机时间，颜色，重量，cpu型号，内存大小，硬盘大小。  行为：打游戏（传入游戏的名称）,办公。
class Notebook_Computer:

    __xingHao=None
    __date=None
    __color=None
    __zhongLiang=None
    __cup=None
    __ncSize=None
    __cpSize=None

    def daYouXi(self,Gname):
        print("现在玩的游戏是",Gname)

    def banGong(self):
        print("现在还是办公")

#iv.	猴子类：属性：类别，性别，身体颜色，体重。行为：造火（要求传入造火的材料：比如木棍还是石头），学习事物（要求参数传入学习的具体事物，
# 可以不止学习一种事物）
class Monkey:
    __mType=None
    __mSex=None
    __mColour=None
    __mWeight=None

    def zaoHuo(self,caoLiao):
        print("猴子使用",caoLiao,"造火")

    def study(self,xueXi):
        print("猴子学习{}".format(xueXi))

c=Monkey()
c.study("直立行走")






















