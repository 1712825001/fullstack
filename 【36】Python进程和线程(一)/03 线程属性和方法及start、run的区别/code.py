import threading
import time

def showthreadinfo():
    print("当前线程 = {}".format(threading.current_thread()))
    print("主线程 = {}".format(threading.main_thread()))
    print("alive线程个数 = {}".format(threading.active_count()))

def worker():
    count = 0
    showthreadinfo()
    while True:
        if count > 5:
            break
        time.sleep(1)
        count += 1
        print("I am working")

t = threading.Thread(target=worker, name='worker')
showthreadinfo()
t.start()
print('==============end=================')
print('==============end=================')
print('==============end=================')
print('==============end=================')
print('==============end=================')