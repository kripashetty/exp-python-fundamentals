from decorators import do_thrice, do_thrice_and_return

@do_thrice
def return_greeting(name):
    print(f"Hello {name}")
    return f"Hello {name}"
    
print(return_greeting("Kripa")) # None

@do_thrice_and_return
def return_greeting(name):
    print(f"Hello {name}")
    return f"Hello {name} returned"
    
print(return_greeting("Kripa")) 