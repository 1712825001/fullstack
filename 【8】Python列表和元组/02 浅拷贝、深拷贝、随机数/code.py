# lst0 = list(range(4))
# lst1 = list(range(4))
# print(lst0 == lst1) # 比较内容
#
# lst2 = lst0
# lst2[2] = 200
# print(lst0, lst1, lst2)
# print(id(lst0), id(lst1), id(lst2))
#
# lst3 = []
# for i in lst0:
#     lst3.append(i)
#
# print(lst3 == lst0)
# print(lst3 is lst0)
# print(lst2 is lst0)
#
# lst4 = lst0.copy() # 内存中不一样
# print(id(lst4), id(lst0))
# print(lst4 == lst0)
# print(lst4, lst0)
# lst4.append([1,2])
# print(lst4 == lst0)
# print(lst4)
#
# lst5 = lst4.copy()
# print(lst5 == lst4)
# lst5[-1][1] = 2000
# print(lst5 == lst4)
# print(lst4, lst5)
#
# import copy # 深拷贝
# lst6 = copy.deepcopy(lst4)
# print(lst4, lst6)
# lst6[-1][1] = 3000
# print(lst4, lst6)

# 总结如下：
# 简单类型浅拷贝
# lst1 = [1,2,3,4]
# lst2 = lst1.copy()
# print(lst1, lst2)
# print(id(lst1), id(lst2))
# lst2.append(5)
# print(lst1, lst2)

# 简单类型深拷贝
# import copy
# lst1 = [1,2,3,4]
# lst2 = copy.deepcopy(lst1)
# print(lst1, lst2)
# print(id(lst1), id(lst2))
# lst2.append(5)
# print(lst1, lst2)
# print(id(lst1), id(lst2))

# 引用类型浅拷贝
# lst1 = [1,2,3,4,[5,6]]
# lst2 = lst1.copy()
# print(lst1, lst2)
# print(id(lst1), id(lst2))
# lst2[-1][1] = 1000
# print(lst1, lst2)
# print(id(lst1), id(lst2))

# 引用类型深拷贝
# import copy
# lst1 = [1,2,3,4,[5,6]]
# lst2 = copy.deepcopy(lst1)
# print(lst1, lst2)
# print(id(lst1), id(lst2))
# lst2[-1][1] = 1000
# print(lst1, lst2)

# 赋值浅拷贝
# lst1 = [1,2,3,4]
# lst2 = lst1
# print(id(lst1), id(lst2))
# lst2.append(5)
# print(lst1, lst2)
# print(id(lst1), id(lst2))

# 赋值深拷贝
# lst1 = [1,2,3,4,[5,6]]
# lst2 = lst1
# print(lst1, lst2)
# print(id(lst1), id(lst2))
# lst2[-1][1] = 1000
# print(lst1, lst2)
# print(id(lst1), id(lst2))

# 随机数
import random
print(random.randint(0,1)) # 闭区间[0,1]
print(random.randrange(0,1)) # [0,1)
print(random.randrange(0,100,2))
print(random.choice(range(10)))

lst = [1,2,3,4]
random.shuffle(lst)
print(lst)
print(random.sample(lst, 2))

