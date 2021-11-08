class Watercup:
    high=None
    capacity=None   #容量
    colour=None
    tm=None         #材质

    def guocheng(self):
        print(self.tm,"的水杯装满了水")

a=Watercup()
a.high=0.1
a.capacity=0.25
a.colour="白色"
a.tm="陶瓷"
a.guocheng()