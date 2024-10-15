from _on import On
from _off import Off
from _sleep import Sleep
from _hybernate import Hybernate
from _laptop import Laptop

def main():
    '''Exercise the stateful laptop'''
    c = Laptop() # initially Off
    c.change(On)
    c.change(Off)
    c.change(On)
    c.change(Sleep)
    c.change(On)
    c.change(Sleep)
    c.change(Hybernate)
    c.change(On)
    c.change(Hybernate)
    c.change(Off) # nope


if __name__ == '__main__':
    main()