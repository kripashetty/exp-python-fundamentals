
from datetime import datetime


def say_whee():
    print("Wheee")
    
    
def decorator(func):
    def wrapper():
        print("Before ......")
        func()
        print("After.........")
    return wrapper


say_whee = decorator(say_whee)
say_whee()

def not_during_night(func):
    def wrapper():
        if 7<= datetime.now().hour < 22 : 
            func()
        else: 
            print("Its too late ....")
            pass
    return wrapper
say_whee = not_during_night(say_whee)
say_whee()