class MyContextManager:
    def __enter__(self):
        print("Entering Context manager")
        return "Hello !"
    
    
    def __exit__(self):
            ...
        