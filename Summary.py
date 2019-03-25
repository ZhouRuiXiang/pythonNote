# -*- coding:utf-8 -*-, Author:Chen

def is_prime(n):
    '''
    判断一个数是否为素数 是返回True 否返回False
    '''
    n = int(n)
    if n == 2:
        return True
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

x = is_prime(67)
print(x)
ls = [11, 67, 5, 22, 11, 6, 3, 7, 12, 4]
# 因为考虑到python边遍历边删除时候 删除一个元素后，后一个元素先前挪动了一个位置 导致准备删除的元素跳了过去
# 遍历深拷贝或倒着遍历
for i in ls[:]:
    if is_prime(i) == True:
        ls.remove(i)
print(ls)


ls = [11, 67, 5, 22, 11, 6, 3, 7, 12, 4]
# 利用filter返回迭代器对象 再转为可迭代对象list
def is_prime_1(n):
    '''判断一个数是否为素数 是返回True 否返回False '''
    n = int(n)
    if n == 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return True
    return False # 质数返回False 合数取出
ls2 = filter(is_prime_1, ls)
print(list(ls2))

def num_wan():
    '''
    某自然数除它本身之外的所有因子之和等于该数，则该数被称为完数。请输出1000以内的完数
    已知2除它本身之外的所有因子 只要1，即 1 != 2 所有2不是完数
    '''
    for i in range(2, 1001):
        s = i
        for j in range(1, i):
            if i % j == 0:
                s -= j
        if s == 0:
            print(i)
# num_wan()
print('-' * 100)
def greatCommonDivisor(a, b):
    c = 0
    while 1:
        if a < b:
            a, b = b, a
        c = a % b
        if c == 0:
            print("最大公约(因)数是:", b)
            break
        a = b
        b = c


greatCommonDivisor(9, 6)

def leastCommonMultiple(n1, n2):
    product = n1 * n2
    if n1 < n2:
        n1, n2, = n2, n1
    while True:
        n3 = n1 % n2
        if n3 == 0:
            print("最小公倍数是:", product // n2)
            break
        n1 = n2
        n2 = n3

leastCommonMultiple(9, 6)

# 带有Python思想的解法
def gcd(n1, n2):
    return gcd(n2, n1 % n2)if n2 > 0 else n1

def lcm(n1,n2):
    return n1 * n2 // gcd(n1, n2)

x = gcd(6, 9)
y = lcm(6, 9)
print("python解法：",x)
print("python解法：",y)


# 斐波那契数列 10000以内
# 1, 1, 2, 3, 5, 8, 13......
def fibonacciSeries(n):
    f, s = 0, 1
    print("FibonacciSeries:", end=" ")
    while f < n:
        print(f, end=" ")
        f, s = s, f + s

fibonacciSeries(10000)

print("-" * 100)
# 水仙花数：三位自幂数(各位数三次幂之和等于本身的数为自幂数)
def narcissisticNumber():
    """求三位数中的水仙花数并输出"""
    print("水仙花数为：", end="")
    for num in range(100, 1000):
        t = num // 100
        s = num // 10 % 10
        f = num % 10
        if t ** 3 + s ** 3 + f ** 3 == num:
            print(num, end=" ")

narcissisticNumber()