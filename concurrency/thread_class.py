from threading import Thread
import random
import time

class MyClass:
    '''we override the __call__ method so we can invoke as a thread target'''
    def __call__(self, n):
        for i in range(0,6):
            print(f'{n} is sleeping')
            time.sleep(random.random()*0.1)

def main():
    '''invoke our class as thread target'''
    c1 = MyClass()
    t1 = Thread(target=c1, args=(1,))
    t2 = Thread(target=c1, args=(2,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print('back on the main thread')

if __name__ == '__main__':
    main()