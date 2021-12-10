from functools import wraps

def func_name_printer(func):
    @wraps(func)
    def wrapper(*args):
        """Prints the Name of the function.
        """
        print("Function that started running is " + func.__name__)
        result = func(*args)
        return result # Extra Return 
    return wrapper

@func_name_printer
def add(*args):
    """
    Args: Tuple of Numbers:
    Returns: Sum of the numbers in Tuple
    """
    tot_sum = 0
    for arg in args:
        tot_sum += arg
    return "result = " + str(tot_sum)

print(add.__name__)
print(add.__doc__)
print(add.__module__)

print(add(5,6,7))

# Output Before Wraps
# wrapper
# Prints the Name of the function.     
# __main__

# # Output After Wraps
# add
# Args: Tuple of Numbers:
# Returns: Sum of the numbers in Tuple
# __main__

# # Output:
# Function that started running is add
# result = 18