from abc import ABCMeta, abstractmethod
import sys

class Animal(metaclass=ABCMeta):
    @abstractmethod
    def make_noise(self):
        pass
# we would probably declare these in separate modules
class Dog(Animal):
    def make_noise(self):
        return 'woof'
class Cat(Animal):
    def make_noise(self):
        return 'miaow'
class Lion(Animal):
    def make_noise(self):
        return 'roar'
class Bat(Animal):
    def make_noise(self):
        return '____'

# here is a creature factory
class CreatureFactory:
    '''This is a single-point-of-access to return any type of creature we have'''  
    def make_sound(self, obj): # we expect to receive the object to be rturned
        # e.g Lion() Cat() etc.
        return eval(obj)().make_noise()

if __name__ == '__main__':
    cf = CreatureFactory()
    creature = sys.argv[1] # Here we expect a system argument variable
    noise = cf.make_sound(creature)
    print(f'The creature {creature} says {noise}')