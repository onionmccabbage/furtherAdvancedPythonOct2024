import collections
from memory_profiler import profile # you may need to pip install memory_profiler

@profile # use the profiler as a decorator
def myFn(n):
    '''manage a double ended queue'''
    my_deq = collections.deque('9876543210') # a string
    for i in range(0,n):
        my_deq.appendleft(i)
        my_deq.append(i)
    return my_deq

if __name__ == '__main__':
    r = myFn(4)
    print(r)