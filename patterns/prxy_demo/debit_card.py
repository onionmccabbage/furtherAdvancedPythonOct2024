from payment import Payment
from bank import Bank
class DebitCard(Payment):
    '''this is a proxy for the bank'''
    def __init__(self):
        self.bank = Bank()
    def doPay(self):
        card = input('swipe, tap, insert...? ')
        self.bank.setCard(card)
        return self.bank.doPay # True or False