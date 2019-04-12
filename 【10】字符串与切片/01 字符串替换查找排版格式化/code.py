# 字符串大小写
print('aaaa'.upper())
print('AAAA'.lower())

# 大小写互相转换
print('aBCdwa'.swapcase() )

# 字符串排版
print('www magedu com'.title())

print('www magedu com'.capitalize())

print('www magedu com'.center(20, '@'))

print('www magedu com'.zfill(20))

print('www magedu com'.ljust(20, '#'))

print('www magedu com'.rjust(20, '#'))

# replace
print('www.magedu.com'.replace('w', 'p'))

print('www.magedu.com'.replace('w', 'p', 2))

print('www.magedu.com'.replace('w', 'p', 3))

print('www.magedu.com'.replace('www', 'python', 2))

# strip
print('    \t\r\nabc d efg very very \t'.strip())

print('    \t\r\nabc d efg very very \t'.lstrip())

print('    \t\r\nabc d efg very very \t'.rstrip())

print('    \t\r\nabc d efg very very \t'.strip(' '))

print('    \t\r\nabc d efg very very \t'.strip(' \t'))

print('    \t\r\nabc d efg very very \t'.strip(' \t\n'))

print('    \t\r\nabc d efg very very \t'.strip(' \t\r\n'))

print('    \t\r\nabc d efg very very \t'.strip(' \t\r\ny'))

print('    \t\r\nabc d efg very very \t'.strip(' \t\r\nry'))

print('    \t\r\nabc d efg very very \t'.strip(' \t\r\nvery'))

print('abc abc ab ac'.strip('abc'))

print('abc abc ab ac'.strip('abc '))

print("\r \n \t Hello Python \n \t".strip())

print(" I am very very very sorry ".strip('Iy'))

print(" I am very very very sorry ".strip('Iy '))

# find
print('www magedu com'.find('w'))

print('www magedu com'.rfind('w'))

print('www magedu com'.find('ww'))

print('www magedu com'.find('wwww'))

print('www magedu com'.find('a', 5))

print('www magedu com'.find('a', 6))

print('www magedu com'.find('a', 6, -1))

print("I am very very very sorry".find('very'))

print("I am very very very sorry".find('very', 5))

print("I am very very very sorry".find('very', 6, 13))

print("I am very very very sorry".rfind('very', 10))

print("I am very very very sorry".rfind('very', 10, 15))

print("I am very very very sorry".rfind('very', -10, -1))

# index
print("I am very very very sorry".index('very'))

print("I am very very very sorry".index('very', 5))

#print("I am very very very sorry".index('very', 6, 13))

print("I am very very very sorry".count('very'))

print("I am very very very sorry".count('very', 5))

print("I am very very very sorry".count('very', 10, 14))

print("I am very very very sorry".startswith('very'))

print("I am very very very sorry".startswith('very', 5))

print("I am very very very sorry".startswith('very', 5, 9))

print("I am very very very sorry".endswith('very', 5, 9))

print("I am very very very sorry".endswith('sorry', 5))

print("I am very very very sorry".endswith('sorry', 5, -1))

print("I am very very very sorry".endswith('sorry', 5, 100))

# 格式化
print('I am %d' % 20)

print('I am %d %d' % (20,30))  #两个以上要加括号)

print("I am %03d" % (20,))

print('I like ,%s.' % 'Python')

print('%3.2f%%,0x%x,0X%02X' % (89.7654,10,15))

print("I am %-5d" % (20,))

# format
print("{}:{}".format('192.168.1.100',8888))

print("{server}{1}:{0}".format(8888,'192.168.1.100',server="Web Server Info:"))

print("{0[0]}.{0[1]}".format(('magedu','com')))


from collections import namedtuple
Point = namedtuple('Point','x y')
p = Point(4,5)
"{0.x},{0.y}".format(p)
#"{{{0.x},{0.y}}}".format(p)

print('{0}*{1}={2:<2}'.format(3,2,2*3))

print('{0}*{1}={2:<02}'.format(3,2,2*3))

print('{0}*{1}={2:>02}'.format(3,2,2*3))

print('{:^30}'.format('centered'))

print('{:*^30}'.format('centered'))

octets = [192,168,0,1]
print('{:02X}{:02X}{:02X}{:02X}'.format(*octets))

print("{}".format(3**0.5))

print("{:g}".format(3**0.5))

print("{:f}".format(3**0.5))

print("{:10f}".format(3**0.5))

print("{:2}".format(102.231))

print("{:.2}".format(3**0.5))

print("{:.2f}".format(3**0.5))

print("{:3.2f}".format(3**0.5))

print("{:3.3f}".format(0.2745))

print("{:3.3%}".format(1/3))

print(print('{:.1f}'.format(4.234324525254)))


