# 求100内所有奇数的和
# sum = 0
# for i in range(1,100,2):
#     sum += i
# print(sum)

# 求1-5阶乘之和
# sum = 0
# value = 1
# for i in range(1,6):
#     value *= i
#     sum += value
# print(sum)

# 给一个数，判断是否是素数
x = 19477

for i in range(2,x):
    if x % i == 0:
        print(x,'不是素数')
        break
else:
    print(x,'是素数')