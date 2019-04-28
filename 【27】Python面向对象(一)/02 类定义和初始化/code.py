# class MyClass:
#     x = 'abc'
#
#     def foo(self):
#         return "My Class"
# print(MyClass.x) # abc
# print(MyClass.foo) # <function MyClass.foo at 0x00000239AA078048>
# print(MyClass.__doc__) # None


class Person:
    x = 13
    def __init__(self, name, age):
        print('init')
        self.name = name
        self.age = age
    def showage(self):
        print(self.age)
tom = Person('tom', 20) # init
print(tom.name, tom.age) # tom 20
print(tom.showage()) # 20

jerry = Person('jerry', 18) # init
print(jerry.name, jerry.age) # jerry 18
print(jerry.showage()) # 18
