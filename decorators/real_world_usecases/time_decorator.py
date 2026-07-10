import functools
import time


def timer(func):
    @functools.wraps(func)
    def timer_wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        value =  func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time 
        print(f"{func.__name__!r} ran in {run_time:.4f} secs")
        return value
    return timer_wrapper

@timer
def waste_some_time(num_time):
    for _ in range(num_time):
        sum([i**2 for i in range(10000)])
    
        
        
