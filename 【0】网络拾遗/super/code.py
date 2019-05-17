# class Animal(object):
#     def __init__(self, name):
#         self.name = name
#
#     def greet(self):
#         print('the animal name is %s' % self.name)
#
#
# class Dog(Animal):
#     def greet(self):
#         super(Dog, self).greet()
#         print('wangwang')
#
#
# dog = Dog('huang')
# dog.greet()

# class Base(object):
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#
# class Inherit(Base):
#     def __init__(self, a, b, c):
#         super(Inherit, self).__init__(a, b)
#         # super().__init__(a, b) # py3支持的写法
#         self.c = c
#         print(self.a)
#         print(self.b)
#         print(self.c)
#
#
# test = Inherit('daocoder', 'mudai', 'dao')

# class Base(object):
#     def __init__(self):
#         print('enter base')
#         print('leave base')
#
#
# class A(Base):
#     def __init__(self):
#         print('enter A')
#         super(A, self).__init__()
#         print('leave A')
#
#
# class B(Base):
#     def __init__(self):
#         print('enter B')
#         super(B, self).__init__()
#         print('leave B')
#
#
# class C(A, B):
#     def __init__(self):
#         print('enter C')
#         super(C, self).__init__()
#         print('leave C')
#
# c = C()

# class Vehicle:  # 定义交通工具类
#     Country = 'China'
#
#     def __init__(self, name, speed, load, power):
#         self.name = name
#         self.speed = speed
#         self.load = load
#         self.power = power
#
#     def run(self):
#         print('开动啦...')
#
#
# class Subway(Vehicle):  # 地铁
#     def __init__(self, name, speed, load, power, line):
#         Vehicle.__init__(self, name, speed, load, power)
#         self.line = line
#
#     def run(self):
#         print('地铁%s号线欢迎您' % self.line)
#         Vehicle.run(self)
#
#
# line13 = Subway('中国地铁', '180m/s', '1000人/箱', '电', 13)
# line13.run()


# class Vehicle:  # 定义交通工具类
#     Country = 'China'
#
#     def __init__(self, name, speed, load, power):
#         self.name = name
#         self.speed = speed
#         self.load = load
#         self.power = power
#
#     def run(self):
#         print('开动啦...')
#
#
# class Subway(Vehicle):  # 地铁
#     def __init__(self, name, speed, load, power, line):
#         # super(Subway,self) 就相当于实例本身 在python3中super()等同于super(Subway,self)
#         super().__init__(name, speed, load, power)
#         self.line = line
#
#     def run(self):
#         print('地铁%s号线欢迎您' % self.line)
#         super(Subway, self).run()
#
#
# class Mobike(Vehicle):  # 摩拜单车
#     pass
#
#
# line13 = Subway('中国地铁', '180m/s', '1000人/箱', '电', 13)
# line13.run()

# 指名道姓与super()的区别
# class A:
#     def __init__(self):
#         print('A的构造方法')
# class B(A):
#     def __init__(self):
#         print('B的构造方法')
#         A.__init__(self)
#
#
# class C(A):
#     def __init__(self):
#         print('C的构造方法')
#         A.__init__(self)
#
#
# class D(B,C):
#     def __init__(self):
#         print('D的构造方法')
#         B.__init__(self)
#         C.__init__(self)
#
#     pass
# f1=D() #A.__init__被重复调用

#使用super()
class A:
    def __init__(self):
        print('A的构造方法')
class B(A):
    def __init__(self):
        print('B的构造方法')
        super(B,self).__init__()


class C(A):
    def __init__(self):
        print('C的构造方法')
        super(C,self).__init__()


class D(B,C):
    def __init__(self):
        print('D的构造方法')
        super(D,self).__init__()

f1=D() #super()会基于mro列表,往后找