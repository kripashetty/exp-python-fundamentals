
import sys

class RedirectStdOut: 
    
    def __init__(self, new_output):
        self.new_output = new_output
        
    def __enter__(self):
        self.saved_output = sys.stdout
        sys.stdout = self.new_output
        
        
    def __exit__(self, *args):
        self.new_output = self.saved_output
   
