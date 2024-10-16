# Fibonacci  1 1 2 3 5 8 13 21...
# always aim for performant code
from memory_profiler import profile 
import timeit

def fib1(n):
    '''Here is a low performance Fibonacci function'''
    if n in (0, 1): # if n>=1
        return 1
    else:
        '''recursively call this function again'''
        return ( fib1(n-1)+fib1(n-2) )

def fib2(n):
    ''''''

if __name__ == '__main__':
    print('fib')
    start1 = timeit.default_timer()
    print( fib1(7) ) # find the result of the first 4 members of the sequence
    end1 = timeit.default_timer()
    print(f'total: {end1-start1}')
    # start2 = timeit.default_timer()
    # fib2()
    # end2 = timeit.default_timer()
    # print(f'total: {end2-start2}')