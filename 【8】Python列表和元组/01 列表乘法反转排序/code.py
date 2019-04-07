# type和ininstance
# print(type('abc'))
# print(type(1234))
# print(isinstance(6, str))
# print(isinstance(6, (str,bool,int)))

# 列表*重复的坑 简单类型和引用类型*3相当于复制了3份
newlist = [1,2] * 3
print(newlist)
newlist[3] = 400
print(newlist)

newlist = [[100,200]] * 3
print(newlist)
newlist[2] = 1000
print(newlist)
newlist[1][1] = 'a'
print(newlist)

lst = [[100,200],[100,200],[100,200]]
lst[1][1] = 'b'
print(lst)

# remove
lst1 = [1,2,1,4,1]
lst1.remove(1)
print(lst1)

# pop
lst1 = [1,2,3,4]
lst1.pop(1)
print(lst1)

# clear
lst1 = [1,2,3,4]
lst1.clear()
print(lst1)

# reverse
lst1 = [1,2,3,4]
lst1.reverse()
print(lst1)

# sort 默认升序
lst1 = [1,2,3,4]
lst1.sort(reverse=True)
print(lst1)

lst1 = [1,2,3,4,'a']
lst1.sort(key=str, reverse=True)
print(lst1)