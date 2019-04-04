# 给一个半径，求圆的面积和周长
# pi = 3.14
# r = float(input('>>'))
#
# area = pi * (r ** 2)
# cr = 2 * pi * r
# print(area, cr)

# 输入两个数，比较大小后，从小到大升序打印
# num1 = int(input('请输入第一个数字： '))
# num2 = int(input('请输入第二个数字： '))
# if num1 < num2:
#     print(num1, num2)
# else:
#     print(num2, num1)

# 三目运算符
# num1 = int(input('请输入第一个数字： '))
# num2 = int(input('请输入第二个数字： '))
# print(num2, num1) if num1 > num2 else print(num1, num2)

# 依次输入若干个整数，打印最大值。如果输入为空，退出程序
# module = int(input('Input first number >>>'))
# while True:
#     c = input('Input a number >>>')
#     if c:
#         n = int(c)
#         if n > module:
#             max = n
#         print('max is', module)
#     else:
#         break

# 输入n个数，求每次输入后的算术平均数
# n = 0
# sum = 0
# while True:
#     i = input('>>>')
#     if i == 'quit':
#         break
#     n += 1
#     sum += int(i)
#     avg = sum / n
#     print(avg)

# 九九乘法表
# for i in range(1, 10):
#     for j in range(1, i+1):
#         print(str(j) + '*' + str(i) + '=' + str(i * j), end=' ')
#     print()

# for i in range(1,10):
#     for j in range(1,i+1):
#         product = i * j
#         if j > 1 and product < 10:
#             product = str(product) + ' '
#         else:
#             product = str(product)
#         print(str(j) + '*' + str(i) + '=' + product, end=' ')
#     print()

# for i in range(1,10):
#     for j in range(1,i+1):
#         print(str(j) + '*' + str(i) + '=' + str(j * i) + '\t', end=' ')
#     print()

# for i in range(1,10):
#     for j in range(1,i+1):
#         if j < 2:
#             print('{}*{}={:<2}'.format(j, i, i * j), end='')
#         else:
#             print('{}*{}={:<3}'.format(j,i,i*j), end='')
#     print()
