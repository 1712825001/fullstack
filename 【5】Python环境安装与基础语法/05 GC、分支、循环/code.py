# 输入2个数字，输出最大值
# num1 = int(input('输入第一个数字:'))
# num2 = int(input('输入第二个数字:'))
# if num1 < num2:
#     print('最大的数字num2', num2)
# else:
#     print('最大的数字num1', num1)


# 给定一个不超过5位的正整数，判断其有几位
# val = int(input('请输入一个不超过5位的正整数: '))
# if val >= 10000:
#     print('五位数')
# elif val >= 1000:
#     print('四位数')
# elif val >= 100:
#     print('三位数')
# elif val >= 10:
#     print('两位数')
# else:
#     print('个位数')

# while
# flag = 10
# while flag:
#     print(flag)
#     flag -= 1

#【计算10以内的偶数】
# for i in range(10):
#     if not i % 2:
#         print(i)
#
# for i in range(0,10,2):
#     print(i)
#
# # 按位与
# for i in range(0,10):
#     if i & 1:
#         continue
#     print(i)

# 计算1000以内的被7整除的前20个数
count = 0
for i in range(0,1000,7):
    print(i)
    count += 1
    if count >= 20:
        break