

import functools
import time



def slowdown(func):
    @functools.wraps(func)
    def slowdown_wrapper(*args, **kwargs):
        time.sleep(2)
        value =  func(*args, **kwargs)
        return value
    return slowdown_wrapper

@slowdown
def countdown(from_number):
    if from_number < 1:
        print("Liftoff!")
    else : 
        print(from_number)
        countdown(from_number-1)
    