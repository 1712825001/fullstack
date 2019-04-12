# 生成一个列表，元素0~9，对每一个元素自增1后求平方返回新列表
# 方法一
# lst = list(range(10))
# for i in lst:
#     print(pow((i+1),2), end=' ')
# 方法二

# old = list(range(10))
# new = []
# for i in old:
#     new.append((i+1)**2)
# print(new)

# 方法三
new = [(i+1)**2 for i in range(10)]
print(new)

