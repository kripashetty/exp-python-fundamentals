
Use : Managing the setup and tear down of resources 
Types of resouces  you need to manage : 
    - File handlers 
    - 

1. Try-except-finally - you need to remeber to add teh finally block
2. open function can be used as a context manager
    ```with open() as :```
    Clean up is managed by the context manager but there is not opportunity to do any cleanup

3. Context manager protocol
    they are pythin object that must have 
    __enter__()
    __exit__()
4. multiple contexts




### Common Context Manager 
- scandir
- path
- localcontext - used with decimal module to manage precision 
- threading.lock - prevent race conditions

### Own Context managers 
- implement the __enter__()__exit__() on a class

- use the contextlib.contextmanager decorator and yield keyword to make a function behave as a context manager


### Task Group in asyncio 
- 


### What is the SWE concept of context managers