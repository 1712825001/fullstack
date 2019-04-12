# pop用法
# d = dict(a=1,b=2,c=3,d=4)
# d.pop() # 什么都不加会出异常，并不是从尾部弹出，因为字典是非线性无序
# print(d)

d = dict(a=1,b=2,c=3,d=4)
d.pop('a')
print(d)

# popitem用法
d = dict(a=1,b=2,c=3,d=4)
d.popitem() # 返回一个元组类型，其实没有规律可循，随机弹出。
print(d)

# clear用法
d = dict(a=1,b=2,c=3,d=4)
d.clear()
print(d)

# 遍历
d = dict(a=1,b=2,c=3,d=4)
for i in d.keys():
    print(i)

d = dict(a=1,b=2,c=3,d=4)
for i in d.values():
    print(i)

d = dict(a=1,b=2,c=3,d=4)
for i in d.items():
    print(i)

d = dict(a=1,b=2,c=3,d=4)
for k,v in d.items():
    print(k, v)

d = dict(a=1,b=2,c=3,d=4)
for k in d.keys():
    print((k, d[k]))

d = dict(a=1,b=2,c=3,d=4)
for k in d.keys():
    print((k, d.get(k)))

# 字典移除
d = dict(a=1,b=2,c='abc')
keys = []
for k,v in d.items():
    if isinstance(v,str):
        keys.append(k)
for k in keys:
    d.pop(k)
print(d)