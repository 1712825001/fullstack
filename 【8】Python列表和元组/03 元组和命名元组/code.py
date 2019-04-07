# 命名元组
from collections import  namedtuple
Point = namedtuple('_Point', ['x', 'y'])
p = Point(11,22)

Student = namedtuple('Student', 'name age')
tom = Student('tom', 20)
print(tom.name, tom.age)