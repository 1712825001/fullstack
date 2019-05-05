# 不涉及继承的例子
# class Animal:
#     def shout(self):
#         print('Animal shout')
#
# animal = Animal()
# animal.shout()
#
# class Cat:
#     def shout(self):
#         print('Cat shout')
#
# cat = Cat()
# cat.shout()

# 继承
class Animal:
    age = 10
    def __init__(self, name):
        self.name = name

    def shout(self):
        print('{} shout'.format(type(self).__name__))

class Cat(Animal):
    pass

animal = Animal('动物')
animal.shout()
print(animal.name, animal.age)

c = Cat('黑子')
c.shout()
print(c.name,c.age)

