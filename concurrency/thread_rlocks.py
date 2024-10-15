# we will write a 'ticket seller' class
# several instances of this class will sell tickets from a shared pool
# we then report how many tickets each seller sold

import threading
import sys
import time
import timeit
import random

ticketsAvailable = 100
numThreads = 8 # we balance the number of threads with the likely amount of work to be done

class TicketSeller(threading.Thread):
    '''we will use a re-entrant lock to manage the locking of shared resources'''
    ticketsSold = 0 # a class member
    def __init__(self, lock): # we choose to pass in a thread lock
        threading.Thread.__init__(self)
        self.__lock = lock
        print('Ticket seller started selling tickets')
    def run(self):
        global ticketsAvailable # or a DB, a file...
        running = True
        while running:
            self.randomDelay() # sleep for a bit
# when we acquire a thread lock, resources are reserved to manage this lock
            self.__lock.acquire() # exclusively access shared resources
            if ticketsAvailable <=0:
                running = False
            else:
                ticketsAvailable -=1
                self.ticketsSold +=1
                print(f'Sold a ticket, {ticketsAvailable} remaining')
# when we release a thread Lock, most of its resources are released for re-use
# when we release a thread re-entrant lock, many oif it's resources are retained (not recycled)
# this means re-acquiring a re-entrant lock is faster
            self.__lock.release()
        print(f'Sold {self.ticketsSold}')
    def randomDelay(self):
        time.sleep(random.randint(0,4)/4) # 0, 0.25, 0.5 0.75

if __name__ == '__main__':
    lock = threading.RLock() # a re-entrant lock
    sellers_l = []
    for _ in range(0,numThreads):
        seller = TicketSeller(lock)
        sellers_l.append(seller)
        seller.start()
    for _ in sellers_l:
        _.join()