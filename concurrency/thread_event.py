from threading import Thread, Event
import time

event = Event()

def myFn(n):
    '''when each thread begins, it has EXCLUSIVE access to the process (one copy of Python)'''
    global event
    print(f'{n} waiting for a thread event...')
    event.wait() # when the event flag changes to True we may continue
    print(f'{n} continuing after thread event')

if __name__ == '__main__':
    t_l = []
    for _ in range(4):
        # the GIL is used for exclusive locking of the main process (Python)
        t = Thread(target=myFn, args=(_,))
        t_l.append(t)
        t.start()
    time.sleep(4) # wait for some dependency to complete...
    event.set() # the event flag is set to True
