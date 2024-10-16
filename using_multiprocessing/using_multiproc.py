import multiprocessing
import os
import timeit

def whichProc():
    '''see which process ID this code is running on'''
    print( f'Running on process ID {os.getpid()}' )

if __name__ == '__main__':
    #we can cmpare running on ONE process or many
    whichProc() # this copy of Python is running on a process
    start1 = timeit.default_timer()
    whichProc() 
    whichProc()
    whichProc()
    whichProc()
    print(f'Sequential took {timeit.default_timer - start1}')
    # next we make a list of separate processes
    procs_l = []
    # all modern computers can run more processes than they have processors (mutliprocessing)
    start2 = timeit.default_timer()
    for n in range(0,4):
        # we invoke a new Process, targetting a function run in that process
        p = multiprocessing.Process(target=whichProc)
        procs_l.append(p)
        p.start() # this is where the process begins to run
    print(f'Parallel took {timeit.default_timer - start2}')
    for _ in procs_l:
        _.join() # optional but good practice