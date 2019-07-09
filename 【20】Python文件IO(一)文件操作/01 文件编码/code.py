f = open('test.txt', mode='r', encoding='utf-8')
print(f.read())
f.close() # 一定要关闭
# print(f.read()) # I/O operation on closed file