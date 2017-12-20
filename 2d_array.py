import numpy

"""
2D matrix

it has rows as well as columns:
http://students.cse.tamu.edu/pritam2309/csce350/backups/matrix.png
"""

an_array = [1, 2, 3, 4]
len(an_array)

# two dimension matrix
two_dim_matrix = [[1, 2, 3],
                  [0, 0, 0],
                  [9, 9, 9],
                  [4, 4, 2]]

# print value of last row last column
# [a][b] --> [a] -> row and [b] -> column
print("value of last row last column:", two_dim_matrix[1][2])

# length of rows
print("# of rows: ", len(two_dim_matrix))

# length of columns
print("# of columns: ", len(two_dim_matrix[0]))

# row x column
print("row * col: ", len(two_dim_matrix), '*', len(two_dim_matrix[0]))

print("\n\n\n")

# iterate a matrix
for row_value in two_dim_matrix:
    print(row_value)

print("\n\n\n")

# iterate individual element in a matrix
# used when index is not needed
for row_value in two_dim_matrix:
    for col_value in row_value:
        print("element: ", col_value)

print("\n\n\n")

# iterate individual element in a matrix using range method
for row_index in range(len(two_dim_matrix)):
    for col_index in range(len(two_dim_matrix[0])):
        print("index: ", row_index)

print("\n\n\n")

# iterate matrix and print elements (values)
# used when index is also needed
for row_index in range(len(two_dim_matrix)):
    for col_index in range(len(two_dim_matrix[0])):
        print("element: ", two_dim_matrix[row_index][col_index])

print("\n\n\n\n")

a = [1, 2, 3]
mx = [[3, 4],
      [5, 6]]

""" SUMMARY OF ARRAY AND MATRIX """

# *****   method - 1:   *****

for value in a:
    print(value)

for row_value in mx:
    for col_value in row_value:
        print(col_value)

# *****   method - 2:   *****

for index in range(len(a)):
    print(a[index])

for row_index in range(len(mx)):
    for col_index in range(len(mx[0])):
        print(mx[row_index][col_index])
