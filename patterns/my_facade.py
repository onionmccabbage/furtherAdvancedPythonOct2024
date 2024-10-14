# we need to bring together different capabilities (provided in separate classes)

class Coder():
    '''create code to solve problems'''
    def __init__(self):
        print('write some code')
    def __is_available(self):
        '''we may need to check the resourxe is available'''
        print('coding skills are available')
        return True # or False
    def book_time(self):
        if self.__is_available():
            print('coder has been booked')

class Tester():
    '''write tests to ensure diligence'''
    def __init__(self):
        print('preparing some tests')
    def testing(self):
        print('tests are in place')

class Technician():
    def __init__(self):
        print('preparing equipment for the team')
    def doStuff(self):
        print('network, machines, cloud all in place')

class Artisan():
    '''design stuff'''
    def __init__(self):
        print('designing things')
    def make_prototype(self):
        print('wireframes are ready')

class Manager():
    '''The manager is the facade to the team members'''
    def __init__(self):
        print('Manager says I can arrange the team')
    def arrange(self):
        '''the facade provides instances of all the other subsystems/microservices'''
        self.coder = Coder()
        self.tester = Tester()
        self.technician = Technician()
        self.artisan = Artisan()
        # we may call on plenty other assets!!!
        # Next, we call methods of our subsystems
        self.coder.book_time()
        self.tester.testing()
        self.technician.doStuff()
        self.artisan.make_prototype()

class Client():
    '''The client needs some resourcces to solve a problem'''
    def __init__(self):
        print('We need a team for our project')
    def askManager(self):
        print('Lets talk to the manager')
        self.manager = Manager() # here we access the facade
        self.manager.arrange() # ask the facade to sort things out for us
    def __del__(self): # every class will run __del__ when done
        print('all done')

if __name__ == '__main__':
    cust = Client()
    cust.askManager()

