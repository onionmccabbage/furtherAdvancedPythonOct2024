# we can write a custom decorator to be applied to any function, 
# making it thread safe (using lock)
from threading import Lock

lock = Lock()

def lock_a_method(meth):
    '''this can be used as a decorator to apply a lock to any method'''
    def locked_method(self, *args, **kwargs):
        try:
            already_locked = meth.getattr('__is_locked') # this will raise an exception if there is no __is_locked
            # raise Exception('method is already locked')
        except Exception as e:
            try:
                with lock:
                    return meth(self, *args, **kwargs)
            except Exception as e:
                print(e)
    lock_a_method.__name__ = f'Locked_Method_{meth.__name__}'
    locked_method.__is_locked = True # add an arbitrary property
    return locked_method


# next we will write a decorator to lock ALL the methods of a class
def make_thread_safe(cls, meth_l, lock):
    '''we iterate over the method of the class, to apply a lock'''
    init = cls.__init__ # take a copy of the init method of the class
    def new_init(self, *args, **kwargs):
        init(self, *args, **kwargs)
        self.__lock = lock
    cls.__init__ = new_init # replace the original __init__ with our new one
    # next we iterate over every method of the decorated class
    for meth in meth_l:
        old_meth = getattr(cls, meth)
        new_meth = lock_a_method(old_meth)
        setattr(cls, meth, new_meth) # replace the original method with our new method
    return cls # our new version of the class, with all methods locked

# to use our method as a class decorator...
def lock_a_class(meth_list, lock):
    return lambda cls: make_thread_safe(cls, meth_list, lock)

@lock_a_class(['add', 'remove','someMethod'], lock) # apply our decorator     
class MySet(set):
    '''this class extens the 'set' data-type, which has 'add' and 'remove' methods'''
    def __init__(self, new_set):
        set.__init__(self, new_set) # simple ask the 'set' to make a set!
    # @lock_a_method # use our decorator
    def someMethod(self, new_value):
        '''this method only allows int values to be added'''
        if type(new_value) == int:
            self.add(new_value) # remember, set has an add method
        else:
            pass # do nothing!!

def main():
    '''exercise the code - check we may add int members with our someMethod'''
    ms = MySet({3,2,6,8,True,'this is my set'})
    ms.add(12)
    # ms.someMethod(99) # all good, its an int
    # ms.someMethod('oops') # not an int, fail silently
    print(ms)
    # can we tell if the someMethod is locked?
    # print( ms.someMethod.__is_locked ) # see an exception
    print( ms.add.__is_locked ) # True

if __name__ == '__main__':
    main()