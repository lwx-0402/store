import time


class air_conditioner:
    __brand=None
    __price=None

    def setBrand(self,brand):
        self.__brand=brand

    def getBrand(self):
        return self.__brand

    def setPrice(self, price):
        self.__price = price

    def getPrice(self):
        return self.__price

    def open(self):
        print("空调开机",end=" ")
        for i in range(3):
            time.sleep(1)
            print(". ", end="")

    def close(self,guanji):
        for i in range(guanji+1):
            print("空调将在", end="")
            if guanji>0:
                print(guanji, end="")
                print("分钟后自动关闭...")
                time.sleep(10)
                guanji -= 1
            else:
                print("此刻关机")

    def air(self):
        print("空调的品牌为：",self.__brand,end=" ")
        print("价格为：",self.__price)

c=air_conditioner()
c.setPrice(300)
c.setBrand("海尔")
c.air()
c.open()
c.close(3)