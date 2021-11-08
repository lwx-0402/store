class Ren:
    __name=""
    __age=0
    __sex=""

    def setName(self,name):
        self.__name=name

    def getName(self):
        return self.__name

    def setAge(self,age):
        if age>120 or age<0:
            print("输入的年龄不合法！")
        else:
            self.__age=age

    def getAge(self):
        return self.__age

    def setSex(self,sex):
        self.__sex=sex

    def getSex(self):
        return self.__sex

class gongRen(Ren):

    def xingWei(self):
        print("我是工人可以干活")

class Student(gongRen): #工人是他爹

    def xingWei(self):
        print("我是学生我可以学习")

    def xingWei2(self):
        print("我是学生我会唱歌")

s=Student()
s.xingWei()
s.xingWei2()