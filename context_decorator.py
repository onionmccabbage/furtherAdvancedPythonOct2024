# in Python 3 we have a context manager
from contextlib import contextmanager
import sys

@contextmanager # make our function behave as a context manager
def outputRedirect(newOutput):
    '''Redirect output to a different context'''
    old_st = sys.stdout
    sys.stdout = newOutput
    yield # our function will yield the next available content to be written
    sys.stdout = old_st

def main():
    print('using normal context')
    with open('my_log.txt', 'at') as fobj: # closes the fobj when with ends
        with outputRedirect(fobj):
            print('redirected content')

if __name__ == '__main__':
    main()
