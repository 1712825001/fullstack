# class Person:
#     AGE = 20
#
# # 为Person动态增加一个类属性NAME
# def add_name(cls, name):
#     cls.NAME = name
# add_name(Person, 'tom')
#
# print(Person.__dict__)

# def add_name(name='jerry'):
#     def wrapper(cls):
#         cls.NAME = name
#         return cls
#     return wrapper
#
# @add_name(name='tom')
# class Person: # 等价于Person = wrapper(Person)
#     AGE = 20
#
# print(Person.__dict__)

# class Person:
#
#     def method(self): # 普通方法
#         print(self)
#
#     @classmethod
#     def class_method(cls):
#         print('class method', cls, hex(id(cls)), hex(id(Person)))
#
#     @staticmethod
#     def static_method():
#         print('static method')
#
# Person.method(Person()) # <__main__.Person object at 0x000002922EDCC128>
# Person().method() # <__main__.Person object at 0x000002922EDCC128>
#
# Person.class_method() # class method <class '__main__.Person'> 0x1e630495338 0x1e630495338
# Person().class_method() # class method <class '__main__.Person'> 0x1e630495338 0x1e630495338
#
# Person.static_method() # static method
# Person().static_method() # static method

class Person:
    def normal_method():
        print('normal')

    def method(self):
        print("{}'s method".format(self))

    @classmethod
    def class_method(cls):
        print('class = {0.__name__} ({0})'.format(cls))

    @staticmethod
    def statuc_method():
        print(Person.HEIGHT)

print('~~~~~~~~~~类方法')
print(1,Person.normal_method())
#print(2,Person.method())
print(3,Person.class_method())