class People:
    __userName=None #姓名
    __sex=None      #性别
    __age=None      #年龄
    __huaFei=None   #话费
    __brand = None  #品牌
    __dian = None   #电池容量
    __ping=None     #屏幕大小
    __daiJi=None    #待机时长
    __jiFen=None    #积分

    def duanXin(self,neiRong):
        print(neiRong)

    def setUserName(self,userName):
        self.__userName=userName

    def getUserName(self):
        return self.__userName

    def setSex(self,sex):
        self.__sex=sex

    def getSex(self):
        return self.__sex

    def setAge(self,age):
        self.__age=age

    def getAge(self):
        return self.__age

    def setHuaFei(self,huaFei):
        self.__huaFei=huaFei

    def getHuaFei(self):
        return self.__huaFei

    def setBrand(self,brand):
        self.__brand=brand

    def getBrand(self):
        return self.__brand

    def setDian(self,dian):
        self.__dian=dian

    def getDian(self):
        return self.__dian

    def setPing(self,ping):
        self.__ping=ping

    def getPing(self):
        return self.__ping

    def setDaiJi(self,daiJi):
        self.__daiJi=daiJi

    def getDaiJi(self):
        return  self.__daiJi

    def setjiFen(self,jiFen):
        self.__jiFen=jiFen

    def getJiFen(self):
        return self.__jiFen

    def daDianHua(self,id,THdate):
        if id!=None:
            if self.huaFei>1:
                if THdate<=10 and THdate>0:
                    self.__huaFei=self.__huaFei-THdate
                    self.__jiFen=self.__jiFen+(THdate*15)
                elif THdate>10 and THdate<=20:
                    self.__huaFei = self.__huaFei - (THdate*0.8)
                    self.__jiFen = self.__jiFen + (THdate * 39)
                else:
                    self.__huaFei = self.__huaFei - (THdate * 0.65)
                    self.__jiFen = self.__jiFen + (THdate * 48)
            else:
                print("您的话费余额不足！")
        else:
            print("没有此电话号码！")
