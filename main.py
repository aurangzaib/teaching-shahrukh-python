"""
1 way of commenting
"""

# another way of commenting

# to print something
print("baber")

# in python, we don't use any brackets for defining a function. instead, spaces are used
# in python, we don't use ; at end of every line

# in python, we dont need to define datatypes
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


"""

13. December 2017

Data structures in Python

"""

# variable
a_variable = 12

"""**** array / list / vector ****"""

# 1, "nimra" .. are elements of array
an_array = [1, "nimra", 3.34, 4, "shahrukh"]

# length of array
print(len(an_array))

# accessing an element
# 4 is element index
print(an_array[4])

# changing an element
an_array[4] = "baber"
print(an_array[4])

"""**** 2D array / Matrix ****"""

# matrix is array of arrays
a_matrix = [
    [1, "nimra", 3.34, 4, "shahrukh"],
    [3, "madiha", 3.44, 1, "shafi_bhai"]
]

# nimra
print(a_matrix[0][1])
# "shafi_bhai"
print(a_matrix[1][4])

"""**** tuple ****"""

# tuple is array of pairs
a_tuple = [
    ("name", "baber"),
    ("last_name", "ali")
]

# ("name", "baber")
print(a_tuple[0])

# "baber"
print(a_tuple[0][1])

# "ali"
print(a_tuple[1][1])

"""**** object ****"""

# object is a key-value pair
# name  --> key
# baber --> value
an_object = {
    "name": "baber",
    "last_name": "ali"
}

# baber
print(an_object["name"])

""""**** collection ****"""

# collection is array of objects
a_collection = [
    {
        "name": "baber",
        "last_name": "ali"
    },
    {
        "name": "nimra",
        "last_name": "siddiqui"
    }
]

# "baber"
print(a_collection[0]["name"])

# "siddiqui"
print(a_collection[1]["last_name"])
