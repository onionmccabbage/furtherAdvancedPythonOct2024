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
    l = (makeRandom(i, 10-i-1) for i in range(4)) # a generator
    # result = await asyncio.gather( makeRandom(3, 6), makeRandom(5, 6) )
    result = await asyncio.gather( *l ) # use * to unpack the positional arguments
    return result

if __name__ == '__main__':
    random.seed(3333) # differrent random for each instance
    r1, r2, r3, r4 = asyncio.run(main())
    print(f'r1: {r1} r2: {r2} r3: {r3} r4: {r4}')
