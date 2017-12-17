"""
range(len()) --> gives index
for element in array --> gives element
zip --> loops multiple arrays
"""

# np is shorthand for numpy
import numpy as np
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