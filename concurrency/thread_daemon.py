# a daemon thread will continue running until the main thread ends
import time
from threading import Thread

def standardFn(n):
    '''this will be invoked as a standard thread'''
    print('starting a standard thread')
    time.sleep(n)
    print('ending standard thread')

def daemonFn():
    '''this will be invoked as a daemon thread'''
    print('starting a daemon thread')
    while True:
        print('heartbeat...')
        time.sleep(0.5)

if __name__ == '__main__':
    s = Thread(target=standardFn, args=(5,))
    # s.setDaemon(True) # this will make a function run as a daemon thread
    d = Thread(target=daemonFn, daemon=True) # this will terminate when the main thread is done
    s.start()
    d.start()
    s.join()
    # we do not wait for daemon to end - it is endless!!