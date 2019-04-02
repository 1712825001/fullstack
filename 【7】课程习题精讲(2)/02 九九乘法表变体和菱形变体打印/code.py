# 打印九九乘法表上半部分
# for i in range(1,10):
#     print(' ' * 7 * (i - 1),end='')
#     for j in range(i,10):
#         product = i * j
#         if product < 10:
#             end = '  '
#         else:
#             end = '  '
#         print(str(i) + '*' + str(j) + '=' + str(i * j),end=end)
#     print()

# for i in range(1,10):
#     s = ""
#     for j in range(i,10):
#         s += '{}*{}={:<{}}'.format(i,j,i * j,2 if j<4 else 3)
#     print('{:>66}'.format(s))

# 打印如下菱形
# for i in range(-3,4):
#     if i < 0:
#         prespace = -i
#     else:
#         prespace = i
#     print(' ' * prespace + '*' * (7 - prespace * 2))

# 打印对顶三角形
# n = 7
# e = n // 2
# for i in range(-e,n-e):
#     prespace = -i if i < 0 else i
#     print(' ' * (e - prespace) + '*' * (2 * prespace + 1))

# 打印闪电

for i in range(-3,4):
    if i < 0:
        print(' ' * (-i) + '*' * (4 + i))
    elif i > 0:
        print(' ' * 3 + '*' * (4 - i))
    else:
        print('*' * 7)