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


dema = Hero("亚索", 3000, 200)
# # dema.info()
dema.name = "盖伦"
dema.Hp = 4000
dema.attack = 210
print("%s的生命值为%d" % (dema.name, dema.Hp))
print("%s的攻击值为%d" % (dema.name, dema.attack))
print("%s来自%s" % (dema.name, dema.origin))
















