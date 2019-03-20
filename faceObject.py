# Python内存回收机制
'''
1.引用计数：当对象被删除时，如果该对象的引用计数不为1，那么该对象的引用计数-1.
当被删除的对象的引用计数为1的时候，那么该对象的内存被回收

'''
# del()方法:用来删除对象的引用计数，销毁对象，每删除一个引用计数-1
# del
# 面向过程：根据业务逻辑从上到下写代码
# 面向对象：将具有共同特征的属性和行为(方法)进行类的封装
# 面向对象的三大特征：封装、继承和多态
# Python面向对象的特征：封装和继承
"""
1.class(object)为新式类
2.object是Python里所有类的父类(相当于根节点)
3.类的命名规范:大驼峰命名法
4.def在类中叫做方法 info是实例方法
5.def中的第一个参数一般是self，表示实例对象的本身。self可以重新命名，作用和变量一样，用来存储对象的内存地址(内存引用)
"""

class Hero(object):
    # Q = "审判"
    origin = "英雄联盟"

    def __init__(self, name, Hp, attack):
        """
        1.python中类里提供的以两个下划线开始，两个下划线结束的方法叫做python的魔法方法
        2.如果类中没有写__init__方法，python会自动创建，但是不执行。
        3.可以重写__init__方法，给对象初始化(initialize)属性
        4.__init__方法在对象被创建的时候，会自动调用
        5.__init__方法中，默认的参数是self(实例化对象)，后面的为形参
        6.如果实例方法是所有对象共享的，类是通过self判断哪个对象调用的实例方法

        """
        self.name = name
        self.Hp = Hp
        self.attack = attack

    def info(self):
        # print("%s的生命值为%d" % (self.name, self.Hp))
        # print("%s的攻击值为%d" % (self.name, self.attack))
        # print("%s来自%s" % (self.name, self.origin))
        # print("我在测试")
        pass


# dema = Hero("亚索", 3000, 200)
# # # dema.info()
# dema.name = "盖伦"
# dema.Hp = 4000
# dema.attack = 210
# print("%s的生命值为%d" % (dema.name, dema.Hp))
# print("%s的攻击值为%d" % (dema.name, dema.attack))
# print("%s来自%s" % (dema.name, dema.origin))



# 2.__str__()魔法方法 作用修改对象默认打印的输出信息(实例化对象的描述)

class Hero2(object):
    def __init__(self, name, hp, attack, armor):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.armor = armor

    def __str__(self):
        # 1.必须有返回值(且为字符串数据类型)
        # 2.尽量返回这个对象的描述信息
        return "它来自英雄联盟，它叫%s" %self.name

fox = Hero2("狐狸", 1000, 80, 100)
print(fox)

'''
1.在创建一个对象的时候Pyhton解释器默认调用__init__()方法
2.在销毁对象的时候Python解释器默认调用__del__()方法
3.意义:当对象在使用时被不小心杀死，用来提示开发者重新创建对象

'''

class Test(object):
    def __init__(self):
        print("对象创建时调用__init__方法")

    def __del__(self):
        print("对象被销毁时调用__del__方法")


t = Test()

a = t
b = a
del(a)
del(b)
# del(t)
# while 1:
#     print(11111)

'''
生熟等级 cookedLevel 0-3 表示生的 3-5 表示半生不熟 5-8 烤好了 >8变成灰
'''

class SweetPotato(object):
    def __init__(self):
        self.cookLevel = 0
        self.cookedString = "生的"
        self.condiments = []


    def __str__(self):
        if self.cookLevel <= 8:
            if self.condiments:
                formula = ",".join(self.condiments)
                return "地瓜是%s, 配方有：%s" % (self.cookedString, formula)
        return "地瓜是%s" % self.cookedString


    def cook(self, time):
        self.cookLevel += time
        if 0 < self.cookLevel <= 3:
            self.cookedString = "生的"
        elif 3 < self.cookLevel < 5:
            self.cookedString = "半生不熟"
        elif 5 <= self.cookLevel <= 8:
            self.cookedString = "熟的"
        elif self.cookLevel > 8:
            self.cookedString = "灰"



    def addCondiment(self, condiment):
        self.condiments.append(condiment)

digua = SweetPotato()
digua.cook(2)
print(digua)
digua.cook(4)
digua.addCondiment("糖")
print(digua)
digua.cook(3)
digua.addCondiment("盐")
print(digua)

"""
1.继承描述的是多个类之间的所属关系
2.B类继承了A类，A类就是基类，父类  B类就是子类、派生类。
3.多继承可以继承多个父类，也继承了所有父类的属性和方法
4.如果多个父类中有同名的属性和方法，则默认使用第一个父类的属性和方法(使用类的魔法方法__mro__的顺序可以查看使用哪个父类的属性和方法)
5.多个父类中，不重名的属性和方法，不会受到影响
"""

class A(object):
    def __init__(self):
        self.num = 10

    def print_num(self):
        print(self.num)

class B(A):
    pass

b = B()
b.print_num()

class Master(object):
    def __init__(self):
        self.kungfu = "古代手法"

    def make_cake(self):
        print("使用[%s]制作了煎饼果子" % self.kungfu)


class School(object):
    def __init__(self):
        self.kungfu = "现代手法"

    def make_cake(self):
        print("使用[%s]制作了高大上的煎饼果子" % self.kungfu)

class Prentice(School, Master):
    def __init__(self):
        self.kungfu = "自创手法"

    def make_cake(self):
        print("使用[%s]制作了巨无霸的煎饼果子" % self.kungfu)
    def old_make_cake(self):
        # 通过使用父类的类名 使用父类中的属性和方法
        print("未更新制作工艺前使用[%s]制作了巨无霸煎饼果子" % self .kungfu)
        Master.__init__(self)
        print("更新古代制作工艺后使用[%s]制作了煎饼果子" % self.kungfu)
    def new_make_cake(self):
        print("未更新制作工艺前使用[%s]制作了煎饼果子" % self.kungfu)
        School.__init__(self)
        print("更新现代制作工艺后使用[%s]制作了高大上的煎饼果子" % self.kungfu)

xiaoming = Prentice()
xiaoming.make_cake()
xiaoming.old_make_cake()
xiaoming.new_make_cake()
print(Prentice.__mro__)


class A(object):
    pass
class B(object):
    pass
class C(B):
    pass
class D(C):
    pass
class E(C, B):
    pass
class F(A, E):
    pass

# C3算法的使用 --> 推算继承顺序MRO
# F -> A -> E-> C -> B
# 从做到右 入度为0 没有指向
# 从上到下
