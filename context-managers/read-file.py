## Write a function read_lines() that opens the file at path using a with statement and returns a 
# list of its lines, each with the trailing newline removed.


def read_lines(path):
    """Return the file's lines, read with a context manager."""
    with open(path) as file:
        return [line.rstrip("\n") for line in file] ## Looping over the file object yields one line at a time
    