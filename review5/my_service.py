# microservice is a design pattern
# break a system into parts each solving a specific problem
# each service could interacrt with other services
# we often think of microservices as Application Programming Interfaces (API)

import socket # this provides a means for services to interact
import requests

def myServer():
    '''This microservice will receive requests from clients'''
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    setup_t = ('localhost', 9876) # IP and port
    server.bind(setup_t) # tell the server which IP address and port it should use
    # we can set the number of concurrent clients to be handled
    server.listen(4) # begin listening for requests from clients
    print(f'Server is listening on {setup_t[0]}:{setup_t[1]} ')
    # a run loop (the server will run continously)
    while True:
        # begin responding to requests
        (client, addr) = server.accept() # unpack the client request into client and their address
        buf = client.recv(1024) # read the first 1024 bytes from the client request
        buf_str = buf.decode() # convert bytes to a string
        print(f'server received {buf_str}')
        if buf == b'quit':
            break # stop this microservice 
        else:
            # this service is a proxy for the weather API
            url_template = f'http://api.openweathermap.org/data/2.5/weather?q={buf_str}&units=metric&APPID=48f2d5e18b0d2bc50519b58cce6409f1'
            print(f'server is trying {url_template}')
            response = requests.get(url_template)
            data = response.json()
            print(f'Server received {data}')
            # read one part of the weahter report
            descr = data['weather'][0]['description']
            # send a response to the client
            # response = buf.upper()
            # client.send(response)
            client.send(descr.encode())

if __name__ == '__main__':
    myServer()

