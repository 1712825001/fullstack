import animal
from animal import Animal

class Cat(Animal):
    x = 'cat'
    y = 'abcd'

class Dog(Animal):
    def __dir__(self):
        return ['dog']

print('~~~~~~~~~')
print('Current Module\'s names = {}'.format(dir()))
print('animal Module\'s names = {}'.format(dir(animal)))