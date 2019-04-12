# 可变位置参数

# def add(nums):
#     print(type(nums))
#     sum = 0
#     for x in nums:
#         sum += x
#     return sum
#
# print(add([1,3,5]))
#
# def add(*nums):
#     print(type(nums))
#     sum = 0
#     for x in nums:
#         sum += x
#     return sum
# print(add(1,3,5))

def fn(*args, x, y, **kwargs):
    print(x)
    print(y)
    print(args)
    print(kwargs)
# fn(3,5)
# fn(3,5,7)
# fn(3,5,a=1,b='python')
fn(7,9,y=5,x=3,a=1,b='python')
