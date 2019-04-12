# 作用域
# def outer():
#     def inner():
#         print('内部')
#     print('外部')
#     inner()
#
# print(outer())
# print(inner())

# x = 5
# def foo():
#     print(x)
#
# print(foo()) # 内部可以看外部，外部不能看内部
#
# x = 5
# def foo():
#     x += 1 # 赋值即被重新定义
#     print(x)
#
# print(foo())

# x = 500
# def fn1():
#     x = 1
#     print(x)
# def fn2():
#     print(x)
#
# print(x)
# print(fn1())
# print(fn2())

# def outer1():
#     o = 65
#     def inner():
#         print("inner {}".format(o))
#         print(chr(o))
#     print("outer {}".format(o))
#     inner()
#
# print(outer1())

# def outer2():
#     o = 65
#     def inner():
#         print("inner {}".format(o))
#         print(chr(o))
#     print("outer {}".format(o))
#     inner()
#     print('outer position2 = ', o)
#
# print(outer2())

x = 5
def foo():
    x = 1
    x += 1
    print(x)

print(foo())