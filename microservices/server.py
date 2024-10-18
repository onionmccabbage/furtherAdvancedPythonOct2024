# microservices is a design pattern
import socket

def server():
    '''This is a simple socket server. It will respond to client requests'''
    # here are some common sensible defaults
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    setup_t = ('localhost', 9876) # IP and port
    server.bind(setup_t)
    # begin listening for clients
    server.listen(4) # this may handle up to 4 concurrent requests
    print(f'Server is listening on {setup_t[0]}:{setup_t[1]}')
    while True: # keep running on main thread
        # we may choose to call a handler function on a new thread
        # todo
        # we can accept any client request
        (client, addr) = server.accept()
        buf = client.recv(1024) # receive the first 1024 bytes from the client
        buf_str = buf.decode() # convert to string
        print(f'Server received {buf_str}')
        if buf in (b'quit', b'Quit', b'QUIT'): # b'...' will make a byte string
            'Server is closing'
            break
        else:
            # respond to the client
            response_str = buf_str.upper()
            client.send(response_str.encode()) # b'{}'.format(response_str))

if __name__ == '__main__':
    server()