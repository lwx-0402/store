class Student:
    __Sname=None
    __Age=None

    def setSname(self,Sname):
        self.__Sname=Sname

    def getSname(self):
        return self.__Sname

    def setAge(self,Age):
        if Age>120 or Age<0:
            print("输入非法！")
        else:
            self.__Age=Age

    def getAge(self):
        return self.__Age

    def showMe(self):
        print("大家好，我叫",self.__Sname,",今年",self.__Age,"岁了!，是DK的中单选手")

    def biJiao_Age(self,xuesheng):
        if self.__Age>xuesheng:
            cha=self.__Age-xuesheng
            return "我比同桌大",cha,"岁！"
        elif self.__Age<xuesheng:
            cha=xuesheng-self.__Age
            return "我比同桌小", cha, "岁！"
        elif self.__Age==xuesheng:
            return "我和我同桌一样大！"

c=Student()
c.setSname("许秀")
c.setAge(18)
c.showMe()
c1=Student()
c1.setSname("李相赫")
c1.setAge(25)
c1.showMe()
print(c.biJiao_Age(c1.getAge()))