from decorators import do_thrice

@do_thrice
def say_whee():
    print("Wheee")
    
say_whee()


@do_thrice
def say_hello(name):
    print(f"hello {name}")
    
say_hello("Kripa")