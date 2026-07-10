
import functools
import time
def do_twice(func):
    def do_twice_wrapper():
        func()
        func()
    return do_twice_wrapper


def do_thrice(func):
    def do_thrice_wrapper(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)
        func(*args, **kwargs)
    return do_thrice_wrapper


def do_thrice_and_return(func):
    def do_thrice_wrapper(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)
        return func(*args, **kwargs)
    return do_thrice_wrapper

def do_thrice_and_return_func_tools(func):
    @functools.wraps(func)
    def do_thrice_wrapper(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)
        return func(*args, **kwargs)
    return do_thrice_wrapper

