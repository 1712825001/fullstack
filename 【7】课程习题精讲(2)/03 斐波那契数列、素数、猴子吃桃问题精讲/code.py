# 求100以内斐波那契数列
# print(0, 0)
# print(1, 1)
# a = 0
# b = 1
# i = 2
# while True:
#     c = a + b
#     if c >100:
#         break
#     a = b
#     b = c
#     print(i, c)
#     i += 1

# 求斐波那契数列第101项
# print(0, 0)
# print(1, 1)
# a = 0
# b = 1
# index = 2
# while True:
#     c = a + b
#     if index > 101:
#         break
#     a = b
#     b = c
#     print(index, c)
#     index += 1

# a = 0
# b = 1
# index = 1
# print('{0},{1}'.format(0,0))
# print('{0},{1}'.format(1,1))
#
# while True:
#     c = a + b
#     a = b
#     b = c
#     index += 1
#     print('{0},{1}'.format(index,c))
#     if index >= 101:
#         break

# 求10万以内所有质数 此题考查效率问题
# for x in range(2, 100):
#     for i in range(2, x):
#         if x % i == 0:
#             break
#     else:
#         print(x)

for x in range(3,100000,2):
    for i in range(3,int(x ** 0.5) + 1,2):
        if x % i == 0:
            break
    else:
        print(x)

# 猴子吃桃问题
# total = x
# 1 x/2 -1
# 2 d1/2 -1
# 3 d2/2 -1
# ...
# 9 d8/2 -1
# 10 1

# peach = 1
# for _ in range(9): # 当不被使用的时候可以用_
#    peach = 2 * (peach + 1)
# print(peach)