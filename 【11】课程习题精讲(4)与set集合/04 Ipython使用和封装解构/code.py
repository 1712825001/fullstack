t = (1,2)
t1 = 1,2
t2 = [1,2]
t = t1
t = t2
print(type(t1))

t3 = 1,2,3,'ab'
print(t3)
t1,t2,t3,t4 = t3
print(t1,t2,t3,t4)

t1,t2,*t3,tail = set(range(100000))
print(t1,t2,tail)

# 丢弃变量
for _ in range(5):
    print('a')

# 练习
# 取出第二个、第四个、倒数第二个
lst = list(range(10))
_,a,_,b,*_,c,_ = lst
print(a,b,c)

# 从lst = [1,(2,3,4),5]提取4出来
lst = [1,(2,3,4),5]
_,(*_,c),_ = lst
print(c)

# JAVA_HOME=/usr/bin,返回变量名和路径
s = "JAVA_HOME=/usr/bin"
env,path = s.split('=', 1)
print(env,path)

# 对列表[1,9,8,5,6,7,4,3,2]使用冒泡排序，要求使用封装和解构来交互数据
lst = [1,9,8,5,6,7,4,3,2]
count = len(lst)
for i in range(0, count):
    for j in range(i+1, count):
        if lst[i] > lst[j]:
            lst[i],lst[j] = lst[j],lst[i]
print(lst)

