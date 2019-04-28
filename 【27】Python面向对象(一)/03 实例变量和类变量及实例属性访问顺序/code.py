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
# print(tom.name, jerry.age) # Tom 25
# jerry.age += 1
# print(jerry.age) # 26
# jerry.showage() # 26


# class MyClass:
#     def __init__(self):
#         print('self in init = {}'.format(id(self)))
#
# c = MyClass() # self in init = 2526911840832
# print('c = {}'.format(id(c))) # c = 2526911840832
#
# d = MyClass() # self in init = 2526911841224
# print('d = {}'.format(id(d))) # d = 2526911841224

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
# print(tom.name1, tom.age) # Tom 3
# print(jerry.name1, jerry.age) # Jerry 3
#
# Person.age = 30
# print(Person.age, tom.age, jerry.age) # 30 30 30
#
# tom.name1 = 'tommy'
# print(jerry.name1) # Jerry
# print(tom.name1) # tommy

# class Person:
#     age = 3
#
#     def __init__(self, name):
#         self.name = name
#
# print('-----class-----')
# print(Person.__class__) # <class 'type'>
# print(Person.__name__) # Person
# print(sorted(Person.__dict__.items()), end='\n\n')
# #[('__dict__', <attribute '__dict__' of 'Person' objects>), ('__doc__', None), ('__init__', <function Person.__init__ at 0x00000280821C9048>), ('__module__', '__main__'), ('__weakref__', <attribute '__weakref__' of 'Person' objects>), ('age', 3)]
#
# tom = Person('Tom')
# print('-----instance Tom-----')
# print(tom.__class__) # <class '__main__.Person'>
# print(sorted(tom.__dict__.items()), end='\n\n') # [('name', 'Tom')]

# class Person:
#     age = 3
#     height = 170
#
#     def __init__(self, name, age=18):
#         self.name = name
#         self.age = age
#
# tom = Person('Tom')
# jerry = Person('Jerry', 20)
#
# Person.age = 30
# print(Person.age, tom.age, jerry.age) # 30 18 20
# print(Person.height, tom.height, jerry.height) # 170 170 170
#
# jerry.height = 175
# print(Person.height, tom.height, jerry.height) # 170 170 175
#
# tom.height += 10
# print(Person.height, tom.height, jerry.height) # 170 180 175
#
# Person.height += 15
# print(Person.height, tom.height, jerry.height) # 185 180 175
#
# Person.weight = 70
# print(Person.weight, tom.weight, jerry.weight) # 70 70 70