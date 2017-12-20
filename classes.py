"""

Revision

"""

# 1 d array
_array_ = [1, 2, 3]

# 2d array
# array of arrays
_matrix_ = [
    [1, 2, 3],
    [3, 4, 5]
]

# tuple
# array of pairs
_tuple_ = [
    (1, 2, 3),
    (3, 4, 5)
]

# object
_object_ = {
    "school": "rose land",
    "city": "karachi"
}

# collection
# array of objects
_collection_ = [
    {"name": "baber"},
    {"name": "nimra"}
]


# function
# a, b, c are arguments
def new_function(a, b, c):
    return a + b + c


new_function(1, 2, 3)
"""

Classes
_____________
            |
            |
Objects     |            
Methods     |
            |
_____________

class is a collection of object and function (method)

methods can access objects of the class but we have to use "self"
    
Example:
        Tesla makes Model S "prototype". This is "class". It has headlight, tyres etc.
        Now Tesla sells thousand of these cars, all of them are "instances"
        All instances are in the beginning similar to each other
        But later you can change the instance
"""


class ClassName:
    # object
    my_object = {
        "model": "Tesla S"
    }

    # method
    def get_value(self):
        return self.my_object["model"]

    # method
    def set_value(self, value):
        self.my_object["model"] = value


an_instance1 = ClassName()
print("Car 1 Model: ", an_instance1.get_value())

an_instance2 = ClassName()
print("Car 2 Model: ", an_instance2.get_value())

an_instance2.set_value("Roadster")
print("Car 2 Model: ", an_instance2.get_value())
print("Car 1 Model: ", an_instance1.get_value())