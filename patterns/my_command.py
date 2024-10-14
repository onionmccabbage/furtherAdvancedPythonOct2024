# the command pattern lets us run code by issuing commands (statements)
from abc import ABCMeta, abstractmethod

class Order(metaclass=ABCMeta):
    @abstractmethod
    def execute(self): # we need an execute method to call as a command
        pass

class StockTrade:
    '''low-level buy and sell operations'''
    def buy(self):
        print('buy stocks')
    def sell(self):
        print('sell stocks')

class BuyStock(Order):
    '''enable a command to be executed which will buy stocks'''
    def __init__(self, stock):
        self.stock = stock
    @property
    def stock(self):
        return self.__stock
    @stock.setter
    def stock(self, new_stock):
        if type(new_stock)== StockTrade:
            self.__stock = new_stock
        else:
            raise TypeError('Missing required stock trade instance')
    def execute(self):
        return self.stock.buy() # call a low-level method of our StiockTrade instance

class SellyStock(Order):
    '''enable a command to be executed which will sell stocks'''
    def __init__(self, stock):
        self.stock = stock
    @property
    def stock(self):
        return self.__stock
    @stock.setter
    def stock(self, new_stock):
        if type(new_stock)== StockTrade:
            self.__stock = new_stock
        else:
            raise TypeError('Missing required stock trade instance')
    def execute(self):
        return self.stock.sell() # call a low-level method of our StiockTrade instance
    