# There are many decorators built in to Python
# @property, @x.setter
# @abstractmethod

# we may write our own custom decorator function
def showArgs(func): # take a function as an argument
    '''this function may be used to decorate any other function
    It will reveal all arguments and positional arguments
    Then run the original function'''
    def newFunc(*args, **kwargs):
        '''log the arg/kwarg values'''
        print(f'''Running a function called {func.__name__}
The positional arguments are {args}
The keyword arguments are {kwargs}''')
        # remember to call the original function!
        return func(*args, **kwargs)
    return newFunc # we do no invoke our new function

@showArgs # we apply our decorator to this function
def isOdd(n):
    return n%2 !=0

@showArgs
def squares(m,n):
    s = []
    for i in range(m,n):
        s.append(i*i)
    return s

if __name__ == '__main__':
    print( isOdd(7) ) # True
    print( squares(-2, 3) ) # [4,1,0,1,4]
    # call a function with keyword arguments
    print( squares(m=-2, n=3) ) # [4,1,0,1,4]