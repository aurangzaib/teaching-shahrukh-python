# np is shorthand for numpy
import numpy as np


"""
print 's' 5 times
"""

for index in range(0, 5):
  print('s')

"""
array has "index" and "element (value)"
range(len()) --> gives index
for element in array --> gives element
zip --> loops multiple arrays
"""

an_array = np.array(['a','b','c', 'd'])
an_array_2 = np.array(['nimra', 'baber', 'js', 'ms'])
# task:
  # 1- print element index (position of element)
  # 2- print element value

# loops through an_array and gives index
for index in range(len(an_array)):
  print("index:", index, " value:", an_array[index])

print()
# loops through an_array and gives only element
for element in an_array:
  print("value: ", element)

print()
# loops through multiple array at once
for element1, element2 in zip(an_array, an_array_2):
  print("element of an_array:", element1, ",element of an_array_2:", element2)

print()
# find_stop_index --> print index when stop ('s') is found

def find_stop_index():
  road = np.array(['r', 'r', 'r', 'r', 'r', 's', 'r'])
  for index in range(len(road)):
    if road[index] == 's':
      print ("index of 's':", index)

find_stop_index()

def find_stop_index_or_break(n):
  road = np.array(['r', 'r', 'r', 'r', 'r', 's', 'r'])
  for index in range(len(road)):
    if road[index] == 's':
      print ("index of 's':", index)
    # if 's' is not found in first n elements
    if index == n:
      print("s is not found in first", n, "elements")
      break # get out of loop

find_stop_index_or_break(3)


# This function takes in the road and determines where to stop
def find_stop_index_udacity(road):
    ## TODO: Iterate through the road array
    ## TODO: Check if a stop sign ('s') is found in the array
    ## If one is, break out of your iteration
    ## and return the value of the index that is *right before* the stop sign
    ## Change the stop_index value
    stop_index = 0
    
    for index in range(len(road)):
        if road[index] == 's':
            # - 1 because 'right before stop sign' 
            stop_index = index - 1
            # get out of loop
            break
    
    return stop_index

  # This function takes in the road and determines where to stop
def find_stop_index_udacity_simpler(road):
    ## TODO: Iterate through the road array
    ## TODO: Check if a stop sign ('s') is found in the array
    ## If one is, break out of your iteration
    ## and return the value of the index that is *right before* the stop sign
    ## Change the stop_index value
        for index in range(len(road)):
        if road[index] == 's':
          return index - 1