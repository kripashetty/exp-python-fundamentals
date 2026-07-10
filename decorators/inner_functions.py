
# def parent_function():
#     print("Printing from Parent Function")
#     def first_function ():
#         print("Printing from First Function")
    
#     def second_function ():
#         print("Printing from Second Function")
        
#     second_function()
#     first_function()
    

# parent_function()




def parent_function(num):
    print("Printing from Parent Function")

    def first_function ():
        print("Printing from First Function")
    
    def second_function ():
        print("Printing from Second Function")
        
    if num == 1 : 
        return first_function
    else: 
        return second_function
    

    

child_function_1 = parent_function(1)
child_function_2 = parent_function(2)

child_function_1()
child_function_2()

'''

Write a function make_greeter() that takes a greeting string and returns a new function. The returned function should take a name and return the full greeting.


Requirements
make_greeter() should accept a single string argument (the greeting)
It should return a new function
The returned function should accept a name and return "{greeting}, {name}!"

Example 
greet = make_greeter("Hello")
hi = make_greeter("Hi")


greet("World")
outputs
'Hello, World!'

greet("Python")
outputs
'Hello, Python!'

hi("Alice")
outputs
'Hi, Alice!'
'''

def make_greeter(greeting):
    """Return a function that greets with the given greeting."""
    def greet(name):
        return f"{greeting}, {name}!"
    return greet
greet = make_greeter("Hello")
greet("Python")
hi = make_greeter("Hi")
greet("Python")