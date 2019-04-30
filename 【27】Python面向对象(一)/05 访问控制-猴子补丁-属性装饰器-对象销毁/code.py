# class Person:
#     def __init__(self, name, age=18):
#         self._name = name
#         self.__age = age
#
#     def getage(self):
#         return self.__age
#
#     def getname(self):
#         return self._name
#
# tom = Person('tom')
# print(tom.getage())
# print(tom.getname())

class Person:
    def __init__(self, name, age):
        self._name = name
        self.__age = age

    @property # setter
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        self.__age = value

    @age.deleter
    def age(self):
        del self.__age

tom = Person('tom', 18)
print(tom._name, tom.age)

tom.age = 20
print(tom.age)