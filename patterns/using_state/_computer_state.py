class ComputerState():
    name='state'
    allowed = []
    def switch(self, new_state):
        if new_state.name in self.allowed:
            print(f'Current state {self} switching to {new_state}')
            self.__class__ = new_state # actually make the state change
        else:
            print(f'Current state {self} cannot switch to {new_state}')
