# 可变位置参数
'''
def add(nums):
    print(type(nums))
    sum = 0
    for x in nums:
        sum += x
    return sum

print(add([1,3,5]))
'''

'''
def add(*nums):
    print(type(nums))
    sum = 0
    for x in nums:
        sum += x
    return sum
print(add(1,3,5))
'''
