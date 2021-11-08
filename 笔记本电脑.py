class computer:
    __pmdx=None
    __jiage=None
    __cup=None
    __neicun=None
    __daijidate=None

    def dazi(self):
        print("正在打字")

    def dayouxi(self):
        print("正在打游戏")

    def kanshipin(self):
        print("正在看视频")

    def setPmdx(self,pmdx):
        self.__pmdx=pmdx

    def getPmdx(self):
        return self.__pmdx

    def setJiage(self,jiage):
        self.__jiage=jiage

    def getJiage(self):
        return self.__jiage

    def setCup(self,cup):
        self.__cup=cup

    def getCup(self):
        return self.__cup

    def setNeicun(self, neicun):
        self.__neicun = neicun

    def getNeicun(self):
        return self.__neicun

    def setDaijidate(self, daijidate):
        self.__daijidate = daijidate

    def getDaijidate(self):
        return self.__daijidate

c=computer()
c.setNeicun("8G")
c.setDaijidate("72小时")
c.setCup("i3-2350m")
c.setJiage(1500)
c.setPmdx(0.3)
c.dayouxi()
c.dayouxi()
c.dazi()