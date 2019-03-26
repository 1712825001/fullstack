# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def showage(self):
#         print('{} is {}'.format(self.name, self.age))
#
# tom = Person('Tom', 20)
# jerry = Person('Jerry', 25)
# print(tom.name, jerry.age)
# jerry.age += 1
# print(jerry.age)
# jerry.showage()


class MyClass:
    def __init__(self):
        print('self in init = {}'.format(id(self)))

c = MyClass()
print('c = {}'.format(id(c)))

d = MyClass()
print('d = {}'.format(id(d)))