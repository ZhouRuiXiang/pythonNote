class A(object):
    name = "父类"
    __date = "2019"

    def __init__(self):
        self.age = "18"
        self.__money = 1000

print(A.__dict__)
a = A()
print(a.age)
print(a.__dict__)
print(a._A__money)

print(A._A__date)
# python中的私有属性是假的私有(伪私有属性)：python的类通过加双下划线来设置"私有属性"，原理是Python解释器将加了双下划线的"属性名"自动转换为"_类名+私有属性名"
# 所以外部通过属性名获取不到,从而实现私有属性的特征


# 类方法是类对象拥有的方法，需要使用装饰器@classmethod来标识其为类方法，对于类方法，第一个参数必须是类对象，一般为cls作为第一个参数，能通过类对象和实例化对象来调用
class People(object):
    __country = "China"
    @classmethod
    def get_country(cls):
        # print(id(cls))
        # print(cls.country)
        return cls.__country
    @classmethod
    def set_country(cls, country):
        cls.__country = country


print(id(People))
People.get_country()

"""
类外部
类属性： 类名.属性 / 实例化对象.属性
类方法： 
"""

# 类方法和对象方法的区别  类方法只能访问类属性 对象方法只能访问属性
# 类方法的作用：修改或访问类属性
class People(object):
    name = "人类"
    doc = '这是一个实例化人类的对象'
    __hp = 100
    def __init__(self):
        self.hp = self.get_hp()
    @classmethod
    def get_hp(cls):
        return cls.__hp

    @classmethod
    def set_hp(cls, modify_hp):
        cls.__hp = modify_hp

    def  __str__(self):
        return "hp:%d" % self.hp

xiaoming = People()
People.set_hp(1000)
xiaohong = People()
print(xiaohong)
print(xiaoming)

# python是一门弱语言 更注重面向过程编程
'''
1.没有访问控制符
2.没有常量
3.定义变量不需要指定类型
4.没有多态的说法
5.没有绝对私有
'''
# python中的常量定义: 将变量名全部大写定义(可以被修改，规定不要修改)

# python中没有静态方法，对于python中的类假写了一个静态方法
# 需要通过装饰器@staticmethod来修饰，静态方法不需要定义参数，可以通过类对象和实例对象来访问
# 作用：为了符合高级语言特性，没有实际意义

# 静态方法使用类属性和对象属性
'''
1.使用类属性：类名.属性(注意无法访问私有属性，对于私有不去使用)
'''
class LOL(object):
    name = "Hero"
    __job = "Mid"
    def __init__(self):
        self.age = "18"
    @staticmethod
    def show():
        print(People.name)
        # 不要访问私有属性


"""
1.从类方法和实例方法以静态方法的定义形式可以看出，类方法的第一个
2.实例化对象的优先级最高
  实例化对象能使用本身的属性和方法，类的属性和方法，静态方法 类方法能使用本身的属性和方法，静态方法
  类对象能使用本身的属性和方法，静态方法
  静态方法没有cls, self
3.静态方法不需要定义额外参数，如果需要可以另加，调用类对象属性和方法不要定义额外参数

"""


"""
静态语言：实例化对象之后无法创建新的方法
动态语言：实例化对象之后可以添加额外的方法

"""


# 封装的意义
'''
1.将属性和方法放到一起作为一个整体(类)，然后通过实例对象处理
2.隐藏内部的实现细节(私有属性)，只需要对象及其属性和方法在内部交互(将方法或属性写进初始化函数中，对象被创建的时候就进行初始化)
3.对于类的属性和方法需要增加访问控制

'''
# 继承

# 多态
"""
多态即定义时的类型和运行时的类型不一样，此时为多态，多态概念经常用于强语言(java C#)
同一个事物的表现形态
多态触发条件：继承；重写；父类指向子类对象。
"""
# 在python中如果类中含有一个方法，我们称之为鸭子类型(但是可以不同事物)


# Summary:
"""
私有属性： 使用get_xx 和set_xx()方法 [人为规定]
常规操作：通过 _类名_私有属性名获取
类属性的对象属性
类属性：内部：cls.属性 / self.属性  外部：类对象名(类名) / 实例化对象名.属性 
对象属性(实例化属性)：内部：self.属性 外部： 实例化对象名.属性
"""

# 类三大方法：  1.对象方法：需要操控对象属性和类属性  2.类方法： 需要操控类属性 3.静态方法： (为了符合高级语言的特性)




















































































































