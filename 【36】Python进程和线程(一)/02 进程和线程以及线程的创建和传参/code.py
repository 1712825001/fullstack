# 最简单多线程
# import threading
#
# def worker():
#     print("I'm working")
#     print('Finished')
#
# t = threading.Thread(target=worker, name='worker')
# t.start()
# print('===end====')

# import threading
# import time
#
# def worker():
#     count = 0
#     while True:
#         time.sleep(1)
#         print("I'm working")
#         print("Finished")
#         count += 1
#         if count > 5:
#             #raise Exception('Thread Error!!!')
#             break
#
# t = threading.Thread(target=worker, name="worker")
# t.start()

# 传参
import threading
import time

def worker(n):
    count = 0
    while True:
        time.sleep(1)
        print("I'm working")
        print("Finished")
        count += 1
        if count > n:
            #raise Exception('Thread Error!!!')
            break

t = threading.Thread(target=worker, name="worker", args=(4,))
t.start()