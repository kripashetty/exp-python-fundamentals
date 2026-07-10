"""
Write a decorator log_calls that logs each call to a function and what it returns, then returns the result unchanged.

Before the function runs, log the call. After it runs, log the value the function returned, then return that value unchanged. Include the function’s own name in your messages by reading it from func.__name__ so the decorator works for any function. Preserve the original function’s name and docstring using functools.wraps. The example below shows a suggested format, but the exact wording isn’t important.

Examples
@log_calls
def greet(name):
    return f"Hi, {name}"
>>> greet("Ada")
Calling greet()
greet() returned 'Hi, Ada'
'Hi, Ada'
Requirements
Before the function runs, print a message that includes the function’s own name
After it runs, print a message that includes the value the function returned
Return the original function’s result unchanged
Work with any number of positional and keyword arguments
Preserve the original function’s name and docstring using functools.wraps
"""

import functools


def log_calls(func):
    """Decorator that logs calls to a function and its return value."""
    '''Print the funcation decorator and values '''
    @functools.wraps(func)
    def logger_wrapper(*args, **kwargs):
        print(f"Calling {func.__name__!r}")
        value =  func(*args, **kwargs)
        print(f" {func.__name__!r}returned {value}")
        return value
        
    return logger_wrapper

@log_calls
def greet(name):
    return f"Hey there {name}"
    
    