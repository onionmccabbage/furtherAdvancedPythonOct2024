import multiprocessing
import os
import timeit

value = 'this is global'

def whichProc(n):
    '''see which process ID this code is running on'''
    global value # this will be a global scope within each separate process
    value  = n # careful - each new process will copy the original parent process scope
    print( f'Running on process ID {os.getpid()} value is {value}' )

if __name__ == '__main__':
    #we can cmpare running on ONE process or many
    # whichProc(0) # this copy of Python is running on a process
    start1 = timeit.default_timer()
    # whichProc(1) 
    # whichProc(2)
    # whichProc(3)
    # whichProc(4)
    end1 = timeit.default_timer()
    print(f'Sequential took {end1 - start1}')
    # next we make a list of separate processes
    procs_l = []
    # all modern computers can run more processes than they have processors (mutliprocessing)
    start2 = timeit.default_timer()
    for n in range(0,4):
        # we invoke a new Process, targetting a function run in that process
        p = multiprocessing.Process(target=whichProc, args=(n,))
        procs_l.append(p)
        p.start() # this is where the process begins to run
    for _ in procs_l:
        _.join() # optional but good practice
        print(value) # is this value inside the process?
    print(value) # this is the orignal global object
    
    
    end2 = timeit.default_timer()
    print(f'Parallel took {end2 - start2}')