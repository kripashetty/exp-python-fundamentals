# Generators - producer for values 
import asyncio
from random import randint
import time


def odds(start, stop):
    for odd in range(start, stop+1,2):
        yield odd # return the first value and pause , the next caller calling this function will call for the next value

# Couroutines -

async def randnd():
    await asyncio.sleep(3) # Some I/O operation 
    return randint(1,10)
    

async def main():
    odd_values = [odd for odd in odds(3,15)]
    print(odd_values)
    start = time.perf_counter()
    r = await randnd()
    elapsed_time = time.perf_counter() - start
    print(f'Sync : Random Number {r} took {elapsed_time:0.2f} seconds' )
    
    
    
    
    start = time.perf_counter()
    r = await asyncio.gather(*(randnd() for _ in range(10))) # the round brackets returns a generator and the star calls the generator
    elapsed_time = time.perf_counter() - start
    print(f'Async : Random Number {r} took {elapsed_time:0.2f} seconds' )
    
    
if __name__ == "__main__":
    asyncio.run(main()) # This is the event loop 
    
    



