def do_twice(f, v):
    """Takes a function object as an argument and calls it twice."""
    f(v)
    f(v)

def print_twice(bruce):
    """Prints the value of the parameter twice."""
    print(bruce)
    print(bruce)

def do_four(f, v):
    """Takes a function object and a value and calls the function four times, passing the value as a parameter."""
    do_twice(f, v)
    do_twice(f, v)
