import numpy as np

# @exercise_1
array = np.arange(10)

# @exercise_2
array = np.arange(4, 10, 0.5, dtype=int).reshape(4, 3)

# @exercise_3
array = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
array = array[array % 2 != 0]



# @exercise_4
array = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
array[1::2] = -1 # nimmt jedes zweite Element des Arrays und ersetzt es mit -1



# @exercise_5
init = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
array = np.copy(init)
array[::2] = -1


# @exercise_reshape
array = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]).reshape(2,5)


# @exercise_stack
a = np.array([[0, 1, 2, 3, 4],
              [0, 0, 0, 0, 0]])
b = np.array([[0, 1, 1, 0, 1],
              [0, 1, 0, 1, 0]])
array = np.stack((a, b)).reshape(4, 5)


# @exercise_range
array = np.array([2, 6, 1, 9, 10, 3, 27])
array = array[(array > 5)]
array = array[ (array <= 10)]
print(array)

