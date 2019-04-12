# 举例
# s1 = 'string'
# s2 = "string2"
# s3 = '''this's a "String"'''
# s4 = 'hello \n magedu.com'
# s5 = r"hello \n magedu.com"
# s6 = 'c:\windows\nt'
# s7 = R"c:\windows\nt"
# s8 = 'c:\windows\\nt'
# sql = """select * from user where name='tom'"""
# print(sql)

# 字符串元素访问
# 【1】字符串支持索引访问
# sql = """select * from user where name='tom'"""
# sql[4]  # 返回c
# # sql[4] = 'o' #返回TypeError

# 【2】有序序列
# sql = "select * "
# for i in sql:
#     print(i)
#     print(type(i))
#
# # 【3】可迭代
# sql = "select * "
# l0 = list(sql)
# l1 = [sql]
# print(l0)
# print(l1)
# ','.join(sql)
# ','.join(map(str, range(10)))

# 字符串join连接
# lst = ['1','2','3']
# print("\"".join(lst))
# print('"'.join(lst)) #单引号和双引号没有歧义可以不用转义
# lst = ['1',['a','b'],'3']
# print("|".join(map(str, lst)))

# 字符串分割
# print('a,b,c'.split('.')) #找不到分隔符会返回原
# print('a,b,c'.split(','))
# print('a \t\rb\nc d'.split(maxsplit=2)) # 两个参数：第一个代表用什么切割，默认为None即为空行 第二个maxsplit=-1代表任意切割
# print('a \t\rb\nc d'.split(sep='\n'))
# print('\n'.join('@'.join(['1','2','3']).split('@')+['4']))
# print('@'.join(['1','2','3']).rsplit('@',1))
# print('\n'.join(['1','2','3']).splitlines()) #默认是False
# print('\n'.join(['1','2','3']).splitlines(True)) # 保留尾巴\n的意思

# partition
print('1ab2ab3ab4'.partition('ab'))
print('1ab2ab3ab4'.rpartition('ab'))