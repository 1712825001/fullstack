import time

def save_log(func):
    def inner(*args, **kwargs):
        # 之前：做一些事情
        func_name = func.__name__
        print(args, kwargs)
        log_path = 'func.log'
        f = open(log_path, 'a')
        f.write('%s 开始调用 %s，参数args: %s, 参数kwargs: %s' % (time.asctime(), func_name, str(args), str(kwargs)) + '\n')
        res = func(*args, **kwargs)  # 调用被装饰函数
        # 之后：再做一些事情
        f.write('%s 结束调用 %s' % (time.asctime(), func_name) + '\n')
        f.close()
        return res
    return inner

@save_log
def test1():
    time.sleep(3)

@save_log
def test2(name):
    print(name)
    time.sleep(1)

test1()
test2('tom')
