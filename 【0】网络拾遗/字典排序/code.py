dict1={'a':2,'b':3,'c':8,'d':4}
# 按key倒序['d', 'c', 'b', 'a']
print(sorted(dict1.keys(), reverse=True))

# 按value倒序[8, 4, 3, 2]
print(sorted(dict1.values(), reverse=True))

print(dict1.items()) # dict_items([('a', 2), ('b', 3), ('c', 8), ('d', 4)])

# x指元组，x[1]是值，x[0]是键
list1 = sorted(dict1.items(), key=lambda x:x[0], reverse=True)
print(list1) # [('d', 4), ('c', 8), ('b', 3), ('a', 2)]

list2 = sorted(dict1.items(), key=lambda x:x[1], reverse=True)
print(list2) # [('c', 8), ('d', 4), ('b', 3), ('a', 2)]