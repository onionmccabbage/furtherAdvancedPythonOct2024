a = 1 # we have an int
b = 3.4 # a float - or boolean, None...
s = 'hello' # an immutable collection of characters
l = []
t = (4,)
d = {}

# if none of the built-in types suit your purpose, construct your own
e = {'x':7.0, 'y':3.8} # or e = [3,4] e=(5,4)

class Point(): # or class (object): or class Point:
    ''' a point in 2-d planar space
    x and y must be numeric'''
    # in Python we tend to allow specific members in our class construct
    __slots__ = ('__x', '__y') # constrain this class to allow only these properties
    def __init__(self, x, y):
        '''a bit like a constructor'''
        self.x = x
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
            raise TypeError('T must be numeric')

if __name__ == '__main__':
    '''we may instantiate our class'''
    p1 = Point(4,3)
