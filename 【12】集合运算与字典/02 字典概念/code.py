# 定义字典
a = {'a':1,'b':2}
print(a)

a = dict(a=1,b=2)
print(a)

a = dict([('c',100),['d',200]],a=1,b=2)
print(a)

print(dict.fromkeys(range(5),'a'))

print(dict.fromkeys(range(5),[1]))

