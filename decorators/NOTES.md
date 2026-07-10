# Functions in Python - basis for decorators
- They are like objects
- The can be stored in variables
- They can be added as items in a List , Dictionary , tuple
- They can be passes as functions arguments
- The can be returned as a value from functions
- They can have functions inside functions
- They can return the inner functions from the parent funtions 
- They can close over variables from their enclosing scope (closures).

# What is a Decorator 
 Decorator is a wrapper function around the function. It leaverages the above features of a function in python. It does not modify the original function 

 ```
    original_function
            │
            ▼
    decorator()
            │
            ▼
    wrapped_function
 ```
-   @decorator is shorthand for function = decorator(function).

# When to reach for them 
- If you want to change the behavior of a function
- You want to change the behaviour in certain conditions 
- You dont have access to the source code
- When you have cross cutting concerns that are independent of business logic and you wnat to reuse it.


# When to stay away
* the added behavior is tightly coupled to the function
* the wrapper becomes difficult to understand
* execution order between many decorators becomes confusing
* a normal helper function would be simpler


# Common use cases 
* Logging
* Timing
* Authentication
* Authorization
* Caching
* Retry logic
* Transactions
* Rate limiting
* Validation
* Feature flags
* Metrics/telemetry

# How Python already usess them 
* @property
* @classmethod
* @statismethod
* @lru_cache
* @app.route("/") in FastAPI framework

# What is a similiar feature in other languages?
- Java - Annotations + Spring AOP + Dynamic Proxies
- Javascript - Hight order functions 

# What is Plugin Architecture in python?
* Plugins solve a diffrent problem
```
    Decorator = modifies how one function behaves.
    Plugin = extends what the application can do.
```

__PS__ : will explore this in a different folder