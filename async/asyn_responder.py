import asyncio
import random

async def makeRandom(idx, threshold=6):
    '''emulate several streams of data as random values'''
    i = random.randint(0,10)
    while i <= threshold:
        '''try to see a value to match the threshold'''
        print(f'{idx}=={i} is too low... retrying')
        # emulate a complex long running piece of code
        await asyncio.sleep(i)
        i = random.randint(0,10)
    idx = i
    print(f'Threshold met: {idx}=={i}')

async def main():
    result = await asyncio.gather( makeRandom(3, 6), makeRandom(5, 6) )
    return result

if __name__ == '__main__':
    asyncio.run(main())
