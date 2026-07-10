
from datetime import datetime




def not_during_night(func):
    def wrapper():
        if 7<= datetime.now().hour < 22 : 
            func()
        else: 
            print("Its too late ....")
            pass
    return wrapper

@not_during_night
def say_whee():
    print("Wheee")
    
say_whee()