def say_hello (name):
    return f"Hello {name}"

def say_more(name):
    return f"Yo ! {name} have a great day !"


print ("\nThe functions are objects")

print ("===================================================")

print(say_hello)
print(say_more)
print ("\nFunctions can be added to lists")

print ("===================================================")

my_list = [say_hello, say_more]

print(my_list[0]("Kripa"))
print(my_list[1]("Kripa"))

        
## Functions can be passed as arguments to functions
print ("\nFunctions can be passed as arguments to functions")
print ("===================================================")
def greet_me(greeting_funcaiton):
    return greeting_funcaiton("Kripa Shetty")


print(greet_me(say_hello))
greet_me((say_more))