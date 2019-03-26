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
# # 装饰器函数
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

#