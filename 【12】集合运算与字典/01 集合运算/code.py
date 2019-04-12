# 并集
set1 = set(range(5))
set2 = set(range(4,9))

print(set1 | set2)

print(set2.union(set2))

print(set1 & set2)

# 随机生成2组各10个数字的列表，如下要求：
# 每个数字取值范围[10,20]
# 统计20个数字中，一共多少个不同的数字
# 2组之间进行比较，不重复的数字有几个
# 2组之间进行比较，重复的数字有几个
a = [1,9,7,5,6,7,8,8,2,6]
b = [1,9,0,5,6,4,8,3,2,3]
s1 = set(a)
s2 = set(b)
print(s1)
print(s2)
print(s1.union(s2))
print(s1.symmetric_difference(s2))
print(s1.intersection(s2))