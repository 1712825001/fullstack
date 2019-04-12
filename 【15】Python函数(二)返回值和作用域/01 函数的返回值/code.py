# def showplus(x):
#     print(x)
#     return x + 1
#     return x + 2
#     print('~~~~~~~~~~')
#
# print(showplus(6))

# def guess(x):
#     if x >3:
#         return '>3'
#     else:
#         return '<=3'
# print(guess(4))
#
# def guess(x):
#     if x > 3:
#         ret = '>3'
#     else:
#         ret = '<3'
#     return ret
# print(2)

# def fn(x):
#     for i in range(x):
#         if i >3:
#             return i
#     else:
#         print("{}is not greater than 3".format(x))
# print(fn(2))

def showlist(): # 没有任何办法返回多个值
    return 1,3,5
x,y,z = showlist()
print(x,y,z)