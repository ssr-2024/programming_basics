import numpy as np

# @exercise_1
array = np.arange(10)
print(array)
# @exercise_2
array = np.full((4, 3), 4)
print(array)
# @exercise_3
array = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
array = array[1::2]
print(array)

# @exercise_4
array = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
array[1::2] = -1
print(array)
# @exercise_5
init = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
array = init.copy()
array[::2] = -1
print(array)
# @exercise_reshape
array = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
array = array.reshape(2, 5)
print(array)
# @exercise_stack
a = np.array([[0, 1, 2, 3, 4],
              [0, 0, 0, 0, 0]])
b = np.array([[0, 1, 1, 0, 1],
              [0, 1, 0, 1, 0]])
array = np.vstack((a, b))
print(array)
# @exercise_range
array = np.array([2, 6, 1, 9, 10, 3, 27])
array = array[(array > 5) & (array <= 10)]
print(array)
# the arange function which does exist in numpy doesn't work in this case, so i solved it like this