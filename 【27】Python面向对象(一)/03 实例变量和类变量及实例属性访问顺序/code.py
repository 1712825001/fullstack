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


# class MyClass:
#     def __init__(self):
#         print('self in init = {}'.format(id(self)))
#
# c = MyClass()
# print('c = {}'.format(id(c)))
#
# d = MyClass()
# print('d = {}'.format(id(d)))

# class Person:
#     age = 3
#     def __init__(self, name):
#         self.name1 = name
#
#     def showname(self):
#         print(self.name1)
#
# tom = Person('Tom')
# jerry = Person('Jerry')
#
# print(tom.name1, tom.age)
# print(jerry.name1, jerry.age)
#
# Person.age = 30
# print(Person.age, tom.age, jerry.age)
#
# tom.name1 = 'tommy'
# print(jerry.name1)
# print(tom.name1)

# class Person:
#     age = 3
#
#     def __init__(self, name):
#         self.name = name
#
# print('-----class-----')
# print(Person.__class__)
# print(sorted(Person.__dict__.items()), end='\n\n')
#
# tom = Person('Tom')
# print('-----instance Tom-----')
# print(tom.__class__)
# print(sorted(tom.__dict__.items()), end='\n\n')

class Person:
    age = 3
    height = 170

    def __init__(self, name, age=18):
        self.name = name
        self.age = age

tom = Person('Tom')
jerry = Person('Jerry', 20)

Person.age = 30
print(Person.age, tom.age, jerry.age)
print(Person.height, tom.height, jerry.height)

jerry.height = 175
print(Person.height, tom.height, jerry.height)

tom.height += 10
print(Person.height, tom.height, jerry.height)

Person.height += 15
print(Person.height, tom.height, jerry.height)

Person.weight = 70
print(Person.weight, tom.weight, jerry.weight)
