from math import pi
a = 12

# checks if a is integer or not
result = isinstance (a, int)
print(result)

# prob -> 0 .... 1
# uniform probability
prob = [1/5, 1/5, 1/5, 1/5, 1/5]

print("pi: ", pi)
print("formatted pi: {:.3f}".format(pi))


"""
 List Comprehension
"""
# to create a uniform distribution
array_length = 4

# manually creating uniform distribution
array_1 = [1/array_length, 1/array_length, 1/array_length, 1/array_length]

# creating uniform disctribution using list comprehension
array_1 = [1/array_length for row in range(array_length)]

# creating an array of 5 null elements 
an_array = [0 for row in range(5)]
