# def fn(*args, x):
#     print(x)
#     print(args)
#
# # fn(3,5) # 会报错
# fn(3,x=5)
# fn(3,5,x=7)


# def connect(host='localhost', port=3306, user='admin', password='admin', **kwargs):
#     print(host, port)
#     print(user, password)
#     print(kwargs)
#
# connect(db='cmdb')
# connect(host='192.168.1.1', db='cmdb')
# connect(host='192.168.1.1', db='cmdb', password='mysql')

# 参数解构，只能用在参数部分来用
# def add(x,y):
#     return x + y
#
# print(add(4,5))
# print(add((4,5)[0],(4,5)[1]))
# print(add(*[4,5]))
# print(add(*(4,5)))
# print(add(*{4,5}))
# print(add(*'45'))
#
# # a,b = *[1,2] # 做函数参数时才能用
# # print(a)
#
# print(add(*range(100,102)))
# #print(add(add(*{'a':100,'b':200}))) #字典可以看做是二维，先是key，然后value
# print(add(**{'x':100,'y':200}))

def add(*iterable):
    result = 0
    for x in iterable:
        result += x
    return result

print(add(1,2,3))
print(add(*[1,2,3]))
print(add(*range(1,4)))
