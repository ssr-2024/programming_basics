import numpy as np

# @exercise_1
array = np.arange(10)
print(array)
# @exercise_2
array = np.full((4, 3), 4)
print(array)
# @exercise_3
array = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
array = array[array % 2 != 0]
'''Boolean Indexing: 
The expression array % 2 != 0 creates 
a boolean array where each element is True 
if the corresponding element in array 
is odd, and False if it is even.
'''
print(array)

# @exercise_4

# @exercise_5
init = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

# @exercise_reshape

# @exercise_stack

# @exercise_range
