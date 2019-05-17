# Python中有3种方式定义类方法, 常规方式, @classmethod修饰方式, @staticmethod修饰方式

class A(object):
    def foo(self, x):
        print("executing foo(%s,%s)" % (self, x))
        print('self:', self)

    @classmethod
    def class_foo(cls, x):
        print("executing class_foo(%s,%s)" % (cls, x))
        print('cls:', cls)

    @staticmethod
    def static_foo(x):
        print("executing static_foo(%s)" % x)

a = A()


'''
1.定义方式
普通的类方法foo()需要通过self参数隐式的传递当前类对象的实例。 @classmethod修饰的方法class_foo()需要通过cls参数传递当前类对象。
@staticmethod修饰的方法定义与普通函数是一样的。self和cls的区别不是强制的，只是PEP8中一种编程风格，slef通常用作实例方法的第一参数，
cls通常用作类方法的第一参数。即通常用self来传递当前类对象的实例，cls传递当前类对象。
'''
'''
2.绑定对象
'''
# print(a.foo) # foo方法绑定对象A的实例 bound method A.foo of <__main__.A object at 0x000002077D62C3C8>>
# print(a.class_foo) # class_foo方法绑定对象A <bound method A.class_foo of <class '__main__.A'>>
# print(a.static_foo) # static_foo没有参数绑定 <function A.static_foo at 0x000002593519A158>
'''
3.调用方式
'''
a.foo(1)
A.foo(a, 1)
# A.foo(1) 报错

A.class_foo(1)
a.class_foo(1)

A.static_foo(1)
a.static_foo(1)
'''
4.继承与覆盖普通类函数是一样的
'''
class B(A):
    pass

b = B()
b.foo(1)
b.class_foo(1)
b.static_foo(1)

class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

s = Student('Bob', 100)
s.score = 1000
print(s.name, s.score)

class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.__score = score

    def get_score(self):
        return self.__score

    def set_score(self, score):
        if score < 0 or score > 100:
            raise ValueError('score必须在1--100之间')
        self.__score = score

s =Student('Jerry', 1000)
s.set_score(100)
print(s.name, s.get_score())

class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.__score = score

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, score):
        if score < 0 or score > 100:
            raise ValueError('score必须在1--100之间')
        self.__score = score

s = Student('赵冬梅', 23)
s.score = 98
print(s.name, s.score)
