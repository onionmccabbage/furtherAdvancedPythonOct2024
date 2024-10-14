from payment import Payment
import random

class Bank(Payment):
    def __init__(self):
        self.card = None
        self.account = None
    def setCard(self, card):
        self.card = card
    def __getAccount(self):
        self.account = self.card # we could offer many proxies for this account
        return self.account
    def __has_funds(self):
        print(f'Bank is checking if {self.__getAccount()} has funds...')
        return bool(random.getrandbits(1)) # True or False
    def doPay(self):
        if self.__has_funds():
            print('Bank is paying')
            return True
        else:
            print('Insufficient funds')
            return False