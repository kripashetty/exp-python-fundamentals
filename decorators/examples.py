from decorators import do_twice, do_thrice_and_return_func_tools

@do_twice
def say_whee():
    print("Wheee")


@do_thrice_and_return_func_tools
def say_whee_functools():
    print("Wheee")
    
    
