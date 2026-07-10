import functools
import random

PLUGINS = dict()

def register(func):
    PLUGINS[func.__name__] = func
    return func

@register
def say_hello(name):
    return f"Hello {name}"

@register
def say_hi(name):
    return f"Hi there {name}"
    
 
def randomly_greet(name):
    greeter , greeter_func = random.choice(list(PLUGINS.items()))
    print(f"Using {greeter!r} to greet.")
    return greeter_func(name)