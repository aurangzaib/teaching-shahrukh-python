"""
1 way of commenting
"""

# another way of commenting

# to print something
print("baber")

# in python, we don't use any brackets for defining a function. instead, spaces are used
# in python, we don't use ; at end of every line

# in python, we don't need to define datatypes
my_string = "baber"
my_integer = 10
print(my_string)


# defining a function
def my_function():
    # variables are defined without types
    a = 10
    b = 20
    print(a + b)


def another_function():
    a = 30
    b = 420
    c = a + b
    return a + b


# using a function
# () is called invocation
my_function()


# Default Arguments/Parameters
# in python we can have default arguments for functions
# 1,2,3 are default values
# default values are used when user doesn't provide any value
def yet_another_function(a=1, b=2, c=3):
    print("sum: ", a + b + c)


yet_another_function(5, 6, 7)
yet_another_function()
