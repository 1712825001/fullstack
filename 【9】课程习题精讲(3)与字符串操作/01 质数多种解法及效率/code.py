# 算法一
# count = 0
# primenumbers = []
# for x in range(2,100):
#      for i in range(2, int(x ** 0.5) + 1): # 奇偶数
#          if x % i == 0:
#              break
#      else:
#          count += 1
#          primenumbers.append(x)
# print(count)
# print(primenumbers)

# 算法二
# count = 1
# primenumbers = []
# for x in range(3,100,2):
#      for i in range(3, int(x ** 0.5) + 2): # 奇数
#          if x % i == 0:
#              break
#      else:
#          count += 1
#          primenumbers.append(x)
# print(count)
# print(primenumbers)

# 算法三
# count = 0
# primenumbers = []
# for x in range(2,100):
#      for i in primenumbers: # 质数列表
#          if x % i == 0:
#              break
#      else:
#          count += 1
#          primenumbers.append(x)
# print(count)
# print(primenumbers)
