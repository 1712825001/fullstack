# def foo(xyz=[1]):
#     xyz.append(1)
#     print(xyz)
#
# print(foo()) # [1,1]
# print(foo()) # [1,1,1]
# print(foo()) # [1,1,1,1]

# def foo(xyz=[1]):
#     xyz.append(1)
#     print(xyz)
#
# print(foo([2])) # [2,1]
# print(foo()) # [1,1]
# print(foo()) # [1,1,1]

# def bar(xyz=1):
#     xyz += 1
#     print(xyz)
#
# print(bar.__defaults__) # (1,)
# print(bar()) # 2
# print(bar.__defaults__) # (1,)
# print(bar()) # 2
# print(bar.__defaults__) # (1,)
# print(bar()) # 2

# def foo(xyz=[1]):
#     xyz += [1]
#     print(xyz)
#
# print(foo.__defaults__) # ([1],)
# print(foo()) # [1,1]
# print(foo.__defaults__) # ([1,1],)
# print(foo()) # [1,1,1]
# print(foo.__defaults__) # ([1,1,1],)
# print(foo()) # [1,1,1,1]

# def bar(xyz,a=2,b='abc',c=(4,),*args,m=5,n=[],**kwargs):
#     pass
# print(bar.__defaults__) # 顺序(2, 'abc', (4,))
# print(bar.__kwdefaults__) # 关键字{'m': 5, 'n': []}


# 函数地址没有变，即函数这个对象没有变，xyz是引用类型，引用类型的元素变化，并不是元组的变化
# def foo(xyz=[],u='abc',z='123'):
#     xyz.append(1)
#     return xyz
# print(foo.__defaults__) # ([], 'abc', '123')
# print(foo(), id(foo)) # [1] 2727554985768
# print(foo.__defaults__) # ([1], 'abc', '123')
# print(foo(), id(foo)) # [1, 1] 2727554985768
# print(foo.__defaults__) # ([1, 1], 'abc', '123')

# 非引用类型例子
# def foo(w, u='abc', z=123):
#     u = 'xyz'
#     z = 789
#     print(w,u,z)
# print(foo.__defaults__) # ('abc', 123)
# print(foo('magedu')) # magedu xyz 789
# print(foo.__defaults__) # ('abc', 123)

# __defaults使用元组保存所有位置参数默认值
# __kwdefaults使用字典保存所有keyword-only参数的默认值
# def foo(w,u='abc',*,z=123,zz=[456]):
#     u = 'xyz'
#     z = 789
#     zz.append(1)
#     print(w,u,z,zz)
# print(foo.__defaults__) # ('abc',)
# print(foo('magedu')) # magedu xyz 789 [456, 1]
# print(foo.__kwdefaults__) # {'z': 123, 'zz': [456, 1]}

# def foo(xyz=[],u='abc',z=123):
#     xyz = xyz[:]
#     xyz.append(1)
#     print(xyz)
#
# print(foo()) # [1]
# print(foo.__defaults__) # ([], 'abc', 123)
# print(foo()) # [1]
# print(foo.__defaults__) # ([], 'abc', 123)
# print(foo([10])) # [10, 1]
# print(foo.__defaults__) # ([], 'abc', 123)
# print(foo([10,5])) # [10, 5, 1]
# print(foo.__defaults__) # ([], 'abc', 123)

def foo(xyz=None,u='abc',z=123):
    if xyz is None:
        xyz = []
    xyz.append(1)
    print(xyz)

print(foo()) # [1]
print(foo.__defaults__) # (None, 'abc', 123)
print(foo()) # [1]
print(foo.__defaults__) # (None, 'abc', 123)
print(foo([10])) # [10, 1]
print(foo.__defaults__) # (None, 'abc', 123)
print(foo([10,5])) # [10, 5, 1]
print(foo.__defaults__) # (None, 'abc', 123)


