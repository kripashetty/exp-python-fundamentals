import functools
import math


def debug(func):
    '''Print the funcation decorator and values '''
    @functools.wraps(func)
    def debug_wrapper(*args, **kwargs):
        
        args_list_repr = [repr(a) for a in args]
        kwqrgs_list_repr = [f"{k} = {v!r}" for k,v in kwargs.items()]
        signature = ", ".join(args_list_repr+kwqrgs_list_repr)
        print(f"Calling {func.__name__!r}({signature})")
        value =  func(*args, **kwargs)
        print(f"Calling {func.__name__!r}returned {value}")
        return value
    return debug_wrapper

@debug
def greeting(name,age=None):
    if age is None: 
        return (f"Hey {name}")
    else:
        return (f"Hey {name}. Already {age}!?")
        
        
math.factorial = debug(math.factorial) # Wrapping a library function to debug! 

def approximate_e(terms = 18 ):
    return sum(1/math.factorial(i) for i in range(terms))
    

