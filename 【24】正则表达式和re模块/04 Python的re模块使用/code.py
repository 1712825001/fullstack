# re.match
'''
尝试从字符串的起始位置匹配一个模式，如果不是起始位置匹配成功的话，match()就返回none。
'''
import re
print(re.match('www', 'www.runoob.com').span()) # (0, 3)在起始位置匹配
print(re.match('com', 'www.runoob.com')) # None

# re.search方法
'''
扫描整个字符串并返回第一个成功的匹配。
'''
print(re.search('www', 'www.runoob.com').span())  # (0, 3)在起始位置匹配
print(re.search('com', 'www.runoob.com').span()) # (11, 14)

# re.match与re.search的区别
'''
re.match只匹配字符串的开始，如果字符串开始不符合正则表达式，则匹配失败，函数返回None；而re.search匹配整个字符串，直到找到一个匹配。
'''
