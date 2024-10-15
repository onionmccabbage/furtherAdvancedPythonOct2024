from threading import Thread
import random
import time

class MyClass(Thread): # we inherit from Thread
    '''we implement a run method'''
    def __init__(self, n):
        Thread.__init__(self)
        self.n = n # we should think about validating this
    def run(self): # in order to be runable we must implement a run method
        for i in range(0,6):
            print(f'{self.n} is sleeping')
            time.sleep(random.random()*0.1)

def main():
    '''invoke our class as thread target'''
    t1 = MyClass(1) # we have instances of Thread (our class)
    t2 = MyClass(2)
    
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print('back on the main thread')

if __name__ == '__main__':
    main()