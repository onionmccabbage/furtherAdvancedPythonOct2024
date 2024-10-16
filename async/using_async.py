import asyncio
# asyncio is stable from 3.7
# NB do not use coroutines, they are deprecated
# @asyncio.coroutine
# def fn():
#     '''old way'''
#     print('I am an async co-routine')
import time
import timeit

# instead we use async-await, mostly because this is a common pattern across languages
async def count():
    '''any function may be decared as 'async' - we can then invoke it using 'await' '''
    print('first do this...')
    await asyncio.sleep(2) # sleep within async is thread safe
    print('secondly do that...')

def count2():
    print('first do this...')
    time.sleep(2)
    print('secondly do that...')

async def main():
    '''call serveral asynchronous versions of our fnction
    Run them at the same time'''
    # gather lets us run the co-routines at the same time
    await asyncio.gather( count(), count(), count(), count() )
    # await count() # these will run sequentially
    # await count() 
    # await count()
    # await count()

if __name__ == '__main__':
    '''await will let the main thread get on with other stuff
    When await returns, it can intrrupt the main thread'''
    start1 = timeit.default_timer()
    asyncio.run(main())
    end1 = timeit.default_timer()
    print(f'Async code took {end1-start1} seconds')
    print('next we run non-async code...')
    start2 = timeit.default_timer()
    count2()
    count2()
    count2()
    count2()
    end2 = timeit.default_timer()
    print(f'Normal code took {end2-start2} seconds')
