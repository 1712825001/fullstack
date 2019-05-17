'''
高阶函数定义:
1.函数接收的参数是一个函数名
2.函数的返回值是一个函数名
3.满足上述条件任意一个,都可称之为高阶函数
'''
# 高级函数示例
def foo():
    print('我的函数名作为参数传给高阶函数')

def gao_jie1(func):
    print('我就是高阶函数1,我接收的参数名是%s' %func)
    func()

def gao_jie2(func):
    print('我就是高阶函数2,我的返回值是%s' %func)
    return func

gao_jie1(foo)
gao_jie2(foo)

# 函数当做参数
import time
# def foo():
#     print('from the foo')
#
# def timmer(func):
#     start_time = time.time()
#     func()
#     end_time = time.time()
#     print('函数%s 运行时间是%s' % (func, end_time - start_time))
#
# timmer(foo)

# 函数当做返回值
def foo():
    print('from the foo')

def timmer(func):
    start_time = time.time()
    return func
    end_time = time.time()
    print('函数%s 运行时间是%s' % (func, end_time - start_time))


foo = timmer(foo)
foo()
'''
高阶函数总结
1.函数接收的参数是一个函数名
　　作用:在不修改函数源代码的前提下,为函数添加新功能,
　　不足:会改变函数的调用方式
2.函数的返回值是一个函数名
　　作用:不修改函数的调用方式
　　不足:不能添加新功能
'''
def father(name):
    print('from father %s' %name)
    def son():
        print('from son')
        def grandson():
            print('from grandson')
        grandson()
    son()

father('林海峰')
