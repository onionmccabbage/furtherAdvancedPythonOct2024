import sys
import socket
from threading import Thread

def myClient(city='Galway'):
    '''make requests to the microservice'''
    cli = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    setup_t = ('localhost', 9876) # IP and port
    # tell this client where to connect
    cli.connect(setup_t)
    if len(sys.argv)>1:
        # concaternate the system arument variables
        msg = ', '.join(sys.argv[1:])
    else:
        msg = city
    # remember to encode all communication
    cli.send(msg.encode())
    # handle any response from the server
    response = cli.recv(1024)
    print(f'Client received {response}')
    # end of interaction, so close
    cli.close()

if __name__ == '__main__':
    cities = ['London', 'Canberra', 'Maine', 'Hull', 'Belfast']
    for city in cities:
        t = Thread(target=myClient, args=(city,))
        t.start()
        t.join()
    # print( sys.argv[1:] )
    # myClient()

