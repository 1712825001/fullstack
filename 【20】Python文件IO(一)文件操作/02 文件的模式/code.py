# w模式：文件存不存在都不报异常，写入会清空之前内容

# f = open('test.txt', mode='w', encoding='utf-8')
# f.write('2222')
# # f.read() 会报错 读的时候不能写，写的时候不能读
# f.close()

# x模式：文件存在报异常
# f = open('test1.txt', mode='x', encoding='utf-8')
# f.write(('1111'))
# f.close()

# a模式: 追加模式,文件存在与否不重要
f = open('test1.txt', mode='a', encoding='utf-8')
f.write('222')
f.close()