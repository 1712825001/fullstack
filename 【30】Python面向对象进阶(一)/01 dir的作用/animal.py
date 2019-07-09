class Animal:
    x = 123
    def __init__(self, name):
        self.name = name
        self.__age = 10
        self.weight = 20
    print('animal module\'s names = {}'.format(dir()))