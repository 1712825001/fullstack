# 打印n边形
# val = int(input('>>>'))
# for i in range(val):
#     if i % (val-1) == 0:
#         print('*' * val)
#     else:
#         print('*' + ' ' * (val-2) + '*')

val = int(input('>>>'))
for i in range(val):
    if i == 0 or i == (val-1):
        print('*' * val)
    else:
        print('*' + ' ' * (val-2) + '*')