# 生成一个列表，元素0~9，对每一个元素自增1后求平方返回新列表
# 方法一
# lst = list(range(10))
# for i in lst:
#     print(pow((i+1),2), end=' ')
# 方法二

# old = list(range(10))
# new = []
# for i in old:
#     new.append((i+1)**2)
# print(new)

# 方法三
# new = [(i+1)**2 for i in range(10)]
# print(new)

# even = [x for x in range(10) if x % 2 == 0]
# print(even)
#
# newlist = [print(i) for i in range(10)]
# print(newlist)

# 获取20以内偶数，如果同时3的倍数也打印
# even = [i for i in range(20) if i%2 == 0 and i%3 == 0]
# print(even)

# even = [(i,j) for i in range(7) if i >4 for j in range(20,25) if j > 23]
# print(even)
#
# even = [(i,j) for i in range(7)  for j in range(20,25) if i > 4 if j > 23]
# print(even)
#
# even = [(i,j) for i in range(7)  for j in range(20,25) if i > 4 and j > 23]
# print(even)

# 列表解析练习
# 1、返回1-10平方的列表
# print([pow(i,2) for i in range(11)])

# 2、有一个列表lst=[1,4,9,16,2,5,10,15]生成一个新列表，要求新列表元素是lst相邻两项的和
# lst=[1,4,9,16,2,5,10,15]
# new = [lst[i] + lst[i+1] for i in range(len(lst) - 1)]
# print(new)

# 3、打印九九乘法表
# even = [print("{}*{}={:<3}".format(j,i,j*i),end='\n' if i==j else '') for i in range(1,10) for j in range(1,i+1)]
# print(even)

# 4、"0001.abcdicdws"是ID格式，要求ID格式是以点号分割，左边是4位从1开始的整数，右边是10位随机小写英文字母
# import random
# even = ["{:04}.{}".format(i,"".join(random.choices('abcdefghijklmnopqrstuvwxyz',k=10))) for i in range(1,101)]
# print(even)

# 列表打印2遍
# g = ["{:04}".format(i) for i in range(1,11)]
# for x in g:
#     print(x)
# print('~~~~~~~~~~~')
# for x in g:
#     print(x)

# 生成器打印1遍

g = ("{:04}".format(i) for i in range(1,11))
next(g)
for x in g:
    print(x)
print('~~~~~~~~~~~')
for x in g:
    print(x)