class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "Point({},{})".format(self.x, self.y)

    def show(self):
        print(self.x, self.y)

p = Point(4,5)
print(p) # Point(4,5)
print(p.__dict__) # {'x': 4, 'y': 5}
p.__dict__['y'] = 16
print(p.__dict__) # {'x': 4, 'y': 5}
p.z = 10
print(p.__dict__) # {'x': 4, 'y': 16, 'z': 10}
print(dir(p))
'''
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'show', 'x', 'y', 'z']
'''
print(p.__dir__())
'''
['x', 'y', 'z', '__module__', '__init__', '__str__', 'show', '__dict__', '__weakref__', '__doc__', '__repr__', '__hash__', '__getattribute__', '__setattr__', '__delattr__', '__lt__', '__le__', '__eq__', '__ne__', '__gt__', '__ge__', '__new__', '__reduce_ex__', '__reduce__', '__subclasshook__', '__init_subclass__', '__format__', '__sizeof__', '__dir__', '__class__']
'''

# 修改如上代码
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "Point({},{})".format(self.x, self.y)

    def show(self):
        print(self)

p1 = Point(4,5)
p2 = Point(10,10)
print(repr(p1), repr(p2), sep='\n')
'''
<__main__.Point object at 0x0000021CB3F355C0>
<__main__.Point object at 0x0000021CB3F35588>
'''
print(p1.__dict__) # {'x': 4, 'y': 5}
setattr(p1, 'y', 16)
setattr(p1, 'z', 10)
print(getattr(p1, '__dict__')) # {'x': 4, 'y': 16, 'z': 10}

# 动态调用方法
# 为类增加方法
if not hasattr(Point, 'add'):
    pass