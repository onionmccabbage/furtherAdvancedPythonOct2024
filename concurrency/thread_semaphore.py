# semaphores let us specify the maximum number of 
# threads that may access a resource concurrently
import random
import time # we could use time.time() to measure how long our code takes
import timeit # this is a more accurate tool for time-difference measurements
import threading

# a global resource
testAvailable = 1024 # a nice power of two

class TestRunner(threading.Thread):
    '''Use a semaphore to control concurrent access to the tests'''
    testsRun = 0
    def __init__(self, semaph):
        threading.Thread.__init__(self)
        self.__semaph = semaph
    def run(self):
        global testAvailable
        running = True
        while running:
            self.__semaph.acquire() # just like acquire a lock or an RLock
            # emulate a long running feature
            self.randomDelay() 
            if testAvailable <=0:
                running=False
            else:
                self.testsRun += 1  
                testAvailable -= 1
            self.__semaph.release() 
        print(f'Test runner {self.getName()} ran {self.testsRun}')
    def randomDelay(self):
        time.sleep(random.randint(0,4)/16) # 0, 0.25, 0.5, 0.75...

def main():
    '''provide a semaphore for concurrent access to the tests being run'''
    sem = threading.Semaphore(64) # we may choose how many concurrent threads may acces the resource
    runners = []
    start = timeit.default_timer()
    for _ in range(0,512):
        runner = TestRunner(sem)
        runners.append(runner)
        runner.start()
    # once all the threads are running, we may call join()
    for thread in runners:
        thread.join()
    end = timeit.default_timer()
    print(f'Total execution time: {end-start}')

if __name__ == '__main__':
    main()