import sys

class Redirect:
    '''This class will redirect output to a different stream
    Return the original output stream when done'''
    def __init__(self, new_stdout):
        '''receive the new output stream'''
        self.new_stdout = new_stdout
    def __enter__(self):
        '''The __enter__ method is invoked whenever this class or an instance of this class is called'''
        self.orig_stdout = sys.stdout
        sys.stdout = self.new_stdout # switch the putput stream to our new stream
    def __exit__(self, exc_type, exc_value, exc_traceback): #we MUST provide these
        '''The __exit__ method is invoked whenever this class or an instance of this class completes'''
        sys.stdout = self.orig_stdout # recover the original output stream

def main():
    '''use 'with' to manage a file access object'''
    with open('my_log.txt', 'at') as fobj:  # when 'with' is done, the fle access object will be closed
        r = Redirect(fobj) # r will use fobj as the new stdout
        with r: # use our class instance
            print('This output will be sent to the log text file')
            # when the 'with' block ends, it releases r (call __exit__)
        print('back to the console')

if __name__ == '__main__':
    print(f'The standard output stream is {sys.stdout}')
    main()
    print(f'The standard output stream is back to {sys.stdout}')