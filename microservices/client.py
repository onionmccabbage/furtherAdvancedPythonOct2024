import socket
import sys

def client():
    '''This simple socket client will make requests over IP'''
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    setup_t=('localhost', 9876)
    client.connect(setup_t) # we connect to the server
    # if there are additional system argument variables, send them to the server
    if len(sys.argv) > 1: # remember sys.argv[0] is always the module name
        msg = ', '.join(sys.argv[1:]) # ignore sys.argv[0]
    else:
        msg = 'default'
    client.send(msg.encode())
    # we may reasonably expect a response
    response = client.recv(1024)
    print(f'Client received {response}') # response will be bytes
    client.close()

if __name__ == '__main__':
    client()