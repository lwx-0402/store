# 分析一个水杯的属性和功能，使用类描述并创建对象
# 高度，容积，颜色，材质
# 能存放液体

# class Glass:
#     __color=""
#     height=0
#     __volume=0
#     __material=""
#
#     def setvolume(self,volume):
#         if volume>500:
#             print("输入非法")
#         else:
#             self.__volume=volume
#     def getvolume(self):
#         return self.__volume
#
#     def setcolor(self,color):
#         self.__color=color
#     def getcolor(self):
#         return self.__color
#
#     def setmaterial(self,material):
#         self.__material=material
#     def getmaterial(self):
#         return self.__material
#
#     def water(self,name):
#         print(self.__color,self.__material,"材质的杯子盛放了",self.__volume,"ml的",name)
#
# g=Glass()
# g.setcolor("绿色")
# g.setmaterial("玻璃")
# g.setvolume(500)
# g.water("水")



# 有笔记本电脑（屏幕大小，价格price，cpu型号，内存大小，待机时长），行为（打字，打游戏，看视频）


class Computer:
    __size=0
    __price=0
    cpu=""
    __memory=0
    time=0

    def setsize(self,size):
        self.__size=size
    def getsize(self):
        return self.__size

    def setprice(self,price):
        self.__price=price
    def getprice(self):
        return self.__price

    def setmemory(self,memory):
        self.__memory=memory
    def getmemory(self):
        return self.__memory



    def typing(self):
        print("这个",self.__price,"块钱，",c.__size,"英寸，内存大小为",self.__memory,"G,的电脑正在打字")
    def playgames(self,game):
        print("这个",self.__price,"块钱，",c.__size,"英寸，内存大小为",self.__memory,"G,的电脑正在玩",game)
    def watchtv(self,tv):
        print("这个",self.__price,"块钱，",c.__size,"英寸，内存大小为",self.__memory,"G,的电脑正在看",tv)

c=Computer()
c.setsize(14)
c.setmemory(500)
c.setprice(10000)
c.typing()
c.playgames("植物大战僵尸")
c.watchtv("斗罗大陆")





