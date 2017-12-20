"""

13. December 2017

Data structures in Python
    1D Array            --> detail in 1D_array.py
    2D Matrix           --> detail in 2D_array.py
    Tuple
    Object & Classes    --> detail in classes.py
    Collection

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
# key   --> name
# value --> baber
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