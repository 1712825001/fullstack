'''
高阶函数定义:
1.函数接收的参数是一个函数名
2.函数的返回值是一个函数名
3.满足上述条件任意一个,都可称之为高阶函数
'''
# 高级函数示例
def foo():
    print('我的函数名作为参数传给高阶函数')

def gao_jie1(func):
    print('我就是高阶函数1,我接收的参数名是%s' %func)
    func()

def gao_jie2(func):
    print('我就是高阶函数2,我的返回值是%s' %func)
    return func

gao_jie1(foo)
gao_jie2(foo)

# 函数当做参数
import time
# def foo():
#     print('from the foo')
#
# def timmer(func):
#     start_time = time.time()
#     func()
#     end_time = time.time()
#     print('函数%s 运行时间是%s' % (func, end_time - start_time))
#
# timmer(foo)

# 函数当做返回值
def foo():
    print('from the foo')

def timmer(func):
    start_time = time.time()
    return func
    end_time = time.time()
    print('函数%s 运行时间是%s' % (func, end_time - start_time))


foo = timmer(foo)
foo()
'''
高阶函数总结
1.函数接收的参数是一个函数名
　　作用:在不修改函数源代码的前提下,为函数添加新功能,
　　不足:会改变函数的调用方式
2.函数的返回值是一个函数名
　　作用:不修改函数的调用方式
　　不足:不能添加新功能
'''
def father(name):
    print('from father %s' %name)
    def son():
        print('from son')
        def grandson():
            print('from grandson')
        grandson()
    son()

father('林海峰')


# 以下为B站内容
# import time
#
# # 判断是否是质数
# def is_prime(num):
#     if num < 2:
#         return False
#     elif num == 2:
#         return True
#     else:
#         for i in range(2,num):
#             if num % i == 0:
#                 return False
#         return True
# # 装饰器函数，在不改变源码的情况下实现新增功能
# def display_time(func):
#     def wrapper(*args): # 代表运行函数的哪些内容
#         t1 = time.time()
#         result = func(*args)
#         t2 = time.time()
#         print('运行时间{:.4}秒'.format(t2 - t1))
#         return result
#     return wrapper
#
#
#
# @display_time
# def count_prime_nums(maxnum):
#     count= 0
#     for i in range(2,maxnum):
#         if is_prime(i):
#             print(i)
#             count += 1
#     return count
# print('质数个数', count_prime_nums(1000))

# 变量作用域
# 块级作用域，python里没有块级作用域概念
# num = int(input('请输入一个整数： '))
# if num % 2 == 0:
#     info = '偶数'
# else:
#     info = '奇数'
# print(info)

# 局部作用域：函数内部定义的变量，函数外部不能访问到
# def fn():
#     name = 'a'
# fn()
# print(name)

# 直接顶格写的是全局
# name = 'aa'
# def f():
#     print(name)
# f()
#
# def f():
#     print(name)
#
# name = 'a'
# f()

# def f():
#     print(name)
#
# f()
# name = 'a'

# name = 'aa'
# def f():
#     name = 'bb'
#     print(name)
# f()
# print(name)

# name = 'aaa'
# def f():
#      name = 'bbb'
#
#      def inner():
#          name = 'ccc'
#          print(name)
#      inner()
#
#
# f()
# print(name)

# 作用域链：函数在运行的时候查找变量的规则，从内往外依次查找
# name = 'aaa'
#
# def f():
#     print(name)
#
# def f2():
#     name = 'green'
#     f()
#
# f2()

# global nolocal

# name = 'aaa'
#
# def f():
#     global name
#     name = 'bbb'
#     print(name)
#
# f()
# print(name)

# global:代表全局变量 nonlocal代表外层变量
# name = 'aaa'
#
# def f():
#     name = 'bbb'
#
#     def inner():
#         nonlocal name
#         name = 'ccc'
#
#     inner()
#     print(name)
# f()

# 闭包
# x = 0
# def outer():
#     x = 1
#     def inner():
#         x = 2
#         print('inner', x)
#
#     inner()
#     print('outer', x)
#
# outer()
# print('global', x)

# nonlocal
# x = 0
# def outer():
#     x = 1
#
#     def inner():
#         nonlocal x
#         x = 2
#         print('inner', x)
#
#     inner()
#     print('outer', x)
#
#
# outer()
# print('global', x)

# global

# x = 0
# def outer():
#     x = 1
#
#     def inner():
#         global x
#         x = 2
#         print('inner', x)
#
#     inner()
#     print('outer', x)
#
#
# outer()
# print('global', x)

# 闭包：内层函数引用了外层函数的自由变量，内层函数会将外层函数的变量封装到函数里，直到内层函数被调用才会被释放
# def f():
#     name = 'aaa'
#
#     def inner():
#         print(name)
#     return inner
# a = f()
# a()

# def f():
#     temp = []
#     for i in range(10):
#         def inner():
#             print(i)
#         temp.append(inner)
#     return temp
#
# funcs = f()
# funcs[0]()

import time

def timer(function):
    def wrapper(*args):
        start_time = time.time()
        function(*args)
        end_time = time.time()
        print("花费时间：{}秒".format(end_time - start_time))
    return wrapper

@timer
def Time(s):
    time.sleep(s)

if __name__ == '__main__':
    Time(2)