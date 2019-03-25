# x = 54321
# w = 10000
# n = 5
# for i in range(n):
#     print(x // w, end=' ')
#     x = x % w
#     w = w // 10


x = '00700'
x = int(x)
n = 5
w = 10 ** (n-1)

flag = False

for i in range(n): # i:0 1 2 3 4
    y = x // w # y:0 0 7 70 700
    if flag or y: # 0 0 1 1 1
        print(y, end=' ')
        flag = True
    x = x % w  # x:700 700 0 0 0
    w = w // 10 # w:1000 100 10 1
