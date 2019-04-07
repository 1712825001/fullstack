# 依次接受用户输入的3个数，排序后打印
# 1、转换int后，判断大小排序，使用分支结构
# nums = []
# out = None
# for i in range(3):
#     nums.append(int(input('{}='.format(i))))
#
# if nums[0] > nums[1]:
#     if nums[0] > nums[2]:
#         if nums[1] > nums[2]:
#             out = [2,1,0]
#         else:
#             out = [1,2,0]
#     else:
#         out = [1,0,2]
# else:
#     if nums[0] > nums[2]:
#         out = [2,0,1]
#     else:
#         if nums[1] < nums[2]:
#             out = [0,1,2]
#         else:
#             out = [0,2,1]
# for i in out:
#     print(nums[i], end=', ')
# 2、使用max函数
# nums = []
# for i in range(3):
#     nums.append(int(input('{}='.format(i))))
#
# while nums:
#     if len(nums) == 1:
#         print(nums[0])
#         break
#     m = max(nums)
#     print(m)
#     nums.remove(m)
# 3、sort方法
# nums = []
# for i in range(3):
#     nums.append(int(input('{}='.format(i))))
# nums.sort()
# print(nums)
# 4、冒泡法
lst1 = [1,9,8,5,7,4,3,2,6,10]
length = len(lst1)
for i in range(length):
    for j in range(length-i-1):
        if lst1[j] > lst1[j+1]:
            tmp = lst1[j]
            lst1[j] = lst1[j+1]
            lst1[j+1] = tmp
print(lst1)
