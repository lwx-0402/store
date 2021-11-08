'''考查知识点：继承的传递性
按要求定义类
要求：
1、定义厨师类，有姓名和年龄的属性，且属性私有化，提供相应的getXxx与setXxx方法，提供无返回值的无参数的蒸饭方法；
2、定义厨师的子类，该类中要求只能写一个无返回值的无参数的炒菜的方法，其他的方法不能写；
3、定义厨师的子类的子类，重写所有父类的方法，每个方法的内容只需打印一句话描述方法的功能即可；(蒸饭，炒菜)
4、定义测试类，创建厨师的子类的子类（厨师的孙子类）对象，使用该对象，对厨师类中的姓名和年龄属性赋值，并获取赋值后的属性值打印到控制台上；
5、使用厨师的孙子类对象调用该对象除了getXxx与setXxx以外的其他方法；'''
class Cook:
    __cName=""
    __cAge=0

    def setCName(self,cName):
        self.__cName=cName

    def getCName(self):
        return self.__cName

    def setCAge(self,cAge):
        self.__cAge=cAge

    def getCAge(self):
        return self.__cAge

    def steamed_rice(self):
        print("厨师会蒸饭")

class Cook_Zi(Cook):

    def chaoCao(self):
        print("会炒菜")

class Cook_Zi_Zi(Cook_Zi):

    def steamed_rice(self):
        print("我跟爷爷学会了蒸饭")

    def chaoCai(self):
        print("我跟爸爸学会了炒菜")

czz=Cook_Zi_Zi()
czz.setCAge(65)
czz.setCName("神厨小福贵")
print(czz.getCAge())
print(czz.getCName())
czz.steamed_rice()
czz.chaoCai()