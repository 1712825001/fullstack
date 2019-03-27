# 列表定义
lst = list()
lst = []
lst = [2,6,9,'ab']
lst = list(range(5))

# index 没有回抛异常
l = [[1,2],3,['a'],2,0,2]
print(l.index(3))
print(l.index(2), end='\n\n')

# count没有不抛异常
print(l.count(2))
print(l.count(4))

# len
print(len(l))

# append
print(l.append('朱素娥'))
print(l)

# insert
print(l.insert(1, '王书'))
print(l)