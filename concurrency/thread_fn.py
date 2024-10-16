# we may call any function to run on a new thread
import time
import random
from threading import Thread # we may access OS threads via this class
# remember - Python always runs in a main thread, so we are spawning additional threads

def myFn(n):
    for i in range(0,6):
        print(f'{n} is sleeping')
        time.sleep( random.random()*0.1 ) # emulate a long running feature

def main():
    '''invoke the fnction on additional threads'''
    # myFn(1) # this is invoked on the main thread
    # to use Threading we target the function
    t1 = Thread(target=myFn, args=(1,), kwargs={})
    t2 = Thread(target=myFn, args=(), kwargs={'n':2})
    t1.start() # both threads run at the same time
    t2.start()
    t1.join() # the main thread will wait for the other thread to (re)join
    t2.join() # it is common practice to wait for other threads to complete
    print('back on the main thread')

if __name__ == '__main__':
    main()