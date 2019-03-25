# floor向下取整，ceil向上取整
# round()，四舍六入五取偶
# int()，取整数部分
# //，整除且向下取整

import math
print(math.floor(2.5), math.floor(-2.5)) # 2 -3
print(math.ceil(2.5), math.ceil(-2.5)) # 3 -2
print(int(-3.6),int(-2.5),int(-1.4)) # -3 -2 -1
print(7//2,7//-2,-7//2,-(7//2)) # 3 -4 -4 -3
print(2//3,-2//3,-1//3) # 0 -1 -1
print(round(2.5),round(2.5001),round(2.6)) # 2 3 3
print(round(3.5),round(3.5001),round(3.6),round(3.3)) # 4 4 4 3
print(round(-2.5),round(-2.5001),round(-2.6)) # -2 -3 -3
print(round(-3.5),round(-3.5001),round(-3.6),round(-3.3)) # -4 -4 -4 -3
print(round(-1.5),round(-2.5),round(-3.5)) # -2 -2 -4
print(list(range(10)))
print(type(list(range(10))))