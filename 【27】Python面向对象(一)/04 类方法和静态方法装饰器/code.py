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

class Person:
    def normal_function(self):
        print(self)
    @classmethod
    def class_method(cls):
        print('class method', cls, hex(id(cls)), help(id(Person)))

Person.normal_function(Person()) # <__main__.Person object at 0x00000262B08DC128>
Person.normal_function(1) # 1
Person().normal_function() # <__main__.Person object at 0x00000262B08DC278>

p1 = Person()
p1.class_method()