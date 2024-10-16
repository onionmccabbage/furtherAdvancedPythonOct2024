from threading import Lock

a = 4
lock = Lock()

def fn():
    '''we can access any global asset'''
    # global a
    # a = 2
    print(a)
    # lock = Lock() # this is local
    # global lock
    with lock: # uses the global
        pass

fn()
print(a)