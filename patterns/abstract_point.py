import abc

# we can declare an abstract class to enforce rules on our concrete classes
class Planar(metaclass=abc.ABCMeta):
    '''Abstraction for a planar point x and y'''
    def __init__(self):
        pass
    @abc.abstractmethod
    def hypot(self):
        pass

# we implement no actual functionality