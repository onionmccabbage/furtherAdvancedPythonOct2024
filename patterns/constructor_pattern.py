a = 1 # we have an int
b = 3.4 # a float - or boolean, None...
s = 'hello' # an immutable collection of characters
l = []
t = (4,)
d = {}

# if none of the built-in types suit your purpose, construct your own
e = {'x':7.0, 'y':3.8} # or e = [3,4] e=(5,4)

from abstract_point import Planar

class Point(Planar): # or class (object): or class Point:
    ''' a point in 2-d planar space
    x and y must be numeric'''
    # in Python we tend to allow specific members in our class construct
    __slots__ = ('__x', '__y') # constrain this class to allow only these properties
    def __init__(self, x, y):
        '''a bit like a constructor'''
        # here self.x looks like a property, but Python calls a method (passin the right-side of the property setter)
        self.x = x # here we call the SETTER METHOD (only works due to @property and @setter)
        self.y = y
    @property
    def x(self):
        return self.__x
    @x.setter
    def x(self, new_x):
        '''validate the incoming argument is permissable'''
        if type(new_x) in (int, float):
            self.__x = new_x
        else:
            raise TypeError('X must be numeric')
    @property
    def y(self):
        return self.__y
    @y.setter
    def y(self, new_y):
        '''validate the incoming argument is permissable'''
        if type(new_y) in (int, float):
            self.__y = new_y
        else:
            raise TypeError('Y must be numeric')
    # we may also declare class methods
    def __str__(self):
        '''this method overrides the built in __str__ and is used by 'print()' '''
        return f'This point is at {self.x} {self.y} hypot {self.hypot()}'
    def __repr__(self):
        '''override the built in __repr__ used in immediate Python'''
        return f'Point at {self.x} {self.y}'
    def hypot(self): # here we declare a derived property (does not persist in the class)
        '''the hypotenuse is derived from the square root of the sum of the squares of thx and y'''
        h = (self.x**2+self.y**2)**0.5 # call the getter methods for __x and __y
        return h

if __name__ == '__main__':
    '''we may instantiate our class'''
    p1 = Point(4,3) # this will call the property setter for x and for y, thereby validating x and y
    # p2 = Point('4', 3)
    p1.x = 5 # all good - when we mutate properties it calls the setter method
    # p1.y = [] # nope - this raises the typeError
    print( p1.x, p1.y)
    print(p1)


