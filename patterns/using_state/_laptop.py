from _off import Off

class Laptop:
    def __init__(self):
        self.state = Off() # the laptop is initially Off
    def change(self, change_to):
        self.state.switch(change_to)