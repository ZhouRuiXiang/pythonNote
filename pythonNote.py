# -*- coding:utf-8 -*- ,Author: XingChen
# 数据类型
# 整型：用于科学计算的进制数 包括：整数 浮点数 复数 布尔值 在python3对其无大小限制
# 浮点型： a = .5 b = 5.  都为浮点型数类型  简写模式 省略0；
# 科学计算法表示 2e5(2e+5) 表示  2 * 10^5  2e-5表示 2 * 10^-5
compute1 = 2e5
compute2 = 2e+5
print(compute1 == compute2) #返回True
# 复数 直接定义(i,j,I,J表示虚部) complex(x, y) 内建函数 x为实部，y为虚部
# None表示一个常量 就是没有值 为空
# 类型转换 浮点型转换为整型时 int转化的时候忽略小数部分(在PYTHON3.5中将此函数考虑四舍五入)
# 常用数学函数

"""
1.求一个数的绝对值 abs()
2.返回比较大小 max(x1,x2) min(x1,x2)
3.返回一个属于的多少次幂的结果 pow(x,y) x为底数 y为指数
4.返回浮点型的四舍五入的结果 round(x[, count]) count表示保留多少位小数 [ ]里的表示可选参数 默认值为0；

"""
# 字符串类型
# 字符串: 在计算机中表示文本 python中中的字符串 使用单引号、双引号、三引号。
# 下标 == 索引: 表示成员元素在当前这个数据类型的位置。
# 切片: 取出当前数据类型中的一段或者有固定间隔的一系列数据 当前数据类型: 字符串，列表，元组
# 例如：str[start_index:end_index :sep]
# 转义字符：在字符串中表示特殊含义的字符使用(\)表示
# 表示一个反斜杠(\\) 表示空格或者空(\000) 表示换行(\n) 表示回车Enter(\r): 删除前方字符串 表示水平制表符(\t)
# 原生字符串: 使转义字符失效 在字符串前加r/R 注意点：原生字符串只对单行字符串起作用
# 字符串的运算 1.表示拼接 + 2.重复生成字符串 * 3.成员运算 in,  not in
# 算数运算符 + - * / //取整 %取余 **幂运算  ** (*/)  (+-) 小括号最高
# 逻辑运算符 < > <= >= != or and not
# 字符串的内建函数
# ord() 返回字符串的ASCII的值 chr() 返回ASCII的值对应的字符 hex() 将数字转换为十六进制字符串 bin() 将数字转换为二进制字符串
# len() 获取字符串的长度
# 字符串的常见方法
# 生成以某个字符为分割点的字符串方法 "".join
# a = "人也是动物" a.find("是",[,start [, end] ]) 查找结果为非负数索引值 若未查找到 则返回-1
# index 方法 查询字符串存在 返回下标 不存在报错
# strip S.strip([chars]) chars : 成员字符串(子字符串)  将字符串的两端出现的指定的子字符串去掉 S.lstrip() S.rstrip() 指定去掉左右的字符串。
# S.count(sub [, start [,end]])
# 把所有的字母转换为大写字母 S.upper()
s = "abc"
s_upper = s.upper()
print(s_upper)
# 把所有的字母转换为小写字母 S.lower()
# S.replace(odr, new [, count])方法 将原来的字符串中的成员字符串替换成新的字符串  count 默认全部替换 count为替换次数

# 字符串首字符大写，其他小写
# S.capitalize()

# 字符串中每个单词首字符大写，其余小写
# S.title() 根据非字母进行划分单词

# 将原字符串居中，左右使用指定的字符串进行填充，默认为空格
# S.center(width [, fill]) width :给定产生新的字符串的长度，指定的长度尽量要大于原来的字符串
# fill: 填充的类型

# 把字符串的大小写互换
# S.swapcase()

# 将一个字符串分割为新的字符串或者列表
# S.split(str = "", num = string.count(str))

# 返回布尔值 True False
# 1. 判断字符串是否以给定的字符串开头
# S.startswith(str [,start [,end]] )
# 2. 判断字符串是否以给定的字符串结尾
# S.endswith(str, [,start [,end]] )

# 3. 判断字符串中所有的字母是否为小写
# S.islower()
# 4.判断字符串中所有的字母是否为大写
# S.isupper()

# 5.
# 判断字符串中每个单词的首字符是否为大写
# S.istitle()
# 6.
# 判断字符串中是否含有文字数字或者数字字符
# 不支持英文
# S.isnumeric()

# 列表：列表使python中一个内建的数据结构，用来有序的存储数据，且列表不变
# 使用内建系统函数 list() 接受可迭代对象 字符串 列表  元组
# list1 = ['a',  'b' , 'c']
# 怎么访问列表元素 下标  切片
# 添加
# L.append() 将元素添加到末尾
# L.insert(index, value) 添加到列表指定的位置
# L.extend() 将新的列表添加到要被添加的列表
# 删除
# L.pop([,index]) 默认删除最后一位
# del L[index] 根据下标删除的元素 下标要符合列表的长度 超出下标长度会报错
# L.remove(value)
# 根据值进行删除
# 如给定值不存在
# 则报错
# L.clear()
# 清空列表

# 查看
# L.index(value [, start [, end]])
# 返回此元素第一次出现的下标


# 其他
# L.sort() 将列表进行排序，默认从小到大 给reverse = True 从大到小排序
# L.reverse() 反转

# 列表的运算
# L1 + L2 列表的组合
# ["*"] * 10  复制列表中的元素
# range(start [, end [, sep]]) 和 for 循环联合使用产生数字列表

# 元组：python中的数据结构，用来有序的存储， 不可修改
# 创建元组  变量名 = ()  内建函数 tuple(可迭代对象) 字符串 列表 元组 字典
# 在唯一的一个元素后面加上英文的逗号 否则类型为元组之中的数据类型 (1) 即为整型
# reversed() 对元组的使用 得到一个反转的可迭代对象 可for循环遍历出其元素

# 元组的拆包
# a = (1, 2) print(*a, sep="-") 变量拆包 a,b = (1, 2)
# 可以进行切片操作


# 字典: 可变的容器，且可以存储任意数据类型 元素是以键值对存储
# key键: 不可变数据类型 元组 数字数据类型 字符串 不可变集合
# value值: 任意数据类型
# 创建字典
# 变量名 = {} 内建函数 dict()  print(dict(a = 1, b = 2, c = 3))
# 访问字典中的值
# 使用D[key]    D.get(key [, default])  default: 默认值对原字典没有影响
# 添加新的键值对 / 修改键值对
# D[新的key / 要修改的key] = 新的value

# 删除
# D.pop(key)
# D.popitem() 默认删除字典中的最后一个 (字典为无序)
# 清空字典 D.clear()

# 字典的常见操作
# len() 查看字典中有多少个键值对
# D.keys() 返回一个类似与类别的key的序列
# 字典的遍历 for i in D.keys() / for i in D.values() / for i in D.items()

# 集合数据类型
# 和列表元组的概念一样， 存储任意数据(列表和字典除外)， 且无序
# 特点：存储的数据不能重复  可以给列表 元组 字符串 去重
# 定义集合
# 1.直接定义 注意使用 { } 定义集合的时候一定要给上单一的数据，否则是空字典
# 2.使用内建函数定义 a = set(可迭代对象) 字符串 元组 列表 字典
# 集合的基本操作
# 添加
# Se.add(value) 若添加的元素存在不做任何操作
# Se.update(value) value 必须为可迭代对象
# 删除
# Se.remove(value) value必须存在于集合，否则报错
# Se.discard(value) value 即使不存在 解释器不会报错
# Se.pop() 随机删除某个元素 返回被删除元素
set_1 = {1, 2, 3}
print(set_1.pop())















