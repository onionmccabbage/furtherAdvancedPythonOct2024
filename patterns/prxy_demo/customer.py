from debit_card import DebitCard

class Customer():
    def __init__(self):
        print('lets buy some stuff')
        self.debitCard = DebitCard()
        self.isPurchased = None
    def makePayment(self):
        self.isPurchased = self.debitCard.doPay() # call our proxy
    def __del__(self):
        if self.isPurchased:
            print('Success! we bought something')
        else:
            print('Oh dear, lend me a fiver?')

