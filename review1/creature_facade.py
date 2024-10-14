from abc import ABCMeta, abstractmethod
class Animal(metaclass=ABCMeta):
    def make_a_noise(self):
        pass
    @abstractmethod
    def __str__(self):
        pass

# here are some concrete creatures (better that they exist in separate modules)
class Dog(Animal):
    def make_a_noise(self):
        return 'woof'
    def __str__(self):
        return f'dog says {self.make_a_noise()}'
class Cat(Animal):
    def make_a_noise(self):
        return 'miaow'
    def __str__(self):
        return f'cat says {self.make_a_noise()}'
class Lion(Animal):
    def make_a_noise(self):
        return 'roar'
    def __str__(self):
        return f'Lion says {self.make_a_noise()}'
class Bat(Animal):
    def make_a_noise(self):
        return '____'
    def __str__(self):
        return f'bat says {self.make_a_noise()}'

# here is a creature factory
class CreatureFacade():
    '''This is a single point of access for all our creatures'''
    def __init__(self):
        self.cat = Cat()
        self.dog = Dog()
        self.lion = Lion()
        self.bat = Bat()
    def make_sounds(self):
        cacophony = f'{self.cat.__str__()} {self.dog.__str__()} {self.lion.__str__()} {self.bat.__str__() }'
        return cacophony
    
if __name__ == '__main__':
    cf = CreatureFacade()
    print( cf.make_sounds() )