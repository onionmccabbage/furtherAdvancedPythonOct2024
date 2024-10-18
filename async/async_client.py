import asyncio

async def my_client(message):
    reader, writer = await asyncio.open_connection('localhost', 8889)
    print(f'Sending {message}')
    writer.write(message.encode())
    await writer.drain() # wait for the writer to complete
    writer.close()

if __name__ == '__main__':
    asyncio.run(my_client('message from client'))