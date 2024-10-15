from _computer_state import ComputerState

class On(ComputerState):
    name='On'
    allowed = ['Off', 'Sleep', 'Hybernate']