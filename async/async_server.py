import asyncio

async def handleRequests(reader, writer):
    '''This server will expect to receieve requests and respond accordingly'''
    data = await reader.read(1024)
    message = data.decode() # convert bytes to string
    addr = writer.get_extra_info('peername')
    # using !r means use raw data
    print(f'Received {message!r} from {addr}')
    writer.close()

async def main():
    '''start the microservice'''
    server = await asyncio.start_server(handleRequests, 'localhost', 8889)
    print('Server started')
    async with server: # keep the server running
        await server.serve_forever()

if __name__ == '__main__':
    asyncio.run(main())