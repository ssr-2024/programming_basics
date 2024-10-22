import numpy as np

# @exercise_1


array = np.arange(10)

# @exercise_2

array = np.full((4, 3), 4)
print(array)

# @exercise_3

array = np.arange(10)
result = array[1::2]
array = result
print(array)

# @exercise_4

array = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
array[array % 2 != 0] = -1
print(array)


# @exercise_5
init = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

array = init.copy()

# Ersetzen von geraden Zahlen (außer der ersten) mit -1
array[0::2] = -1
print(array)

# @exercise_reshape

array = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

array = np.reshape(array, (2, 5))

print(array)

# @exercise_stack

a = np.array([[0, 1, 2, 3, 4],
              [0, 0, 0, 0, 0]])
b = np.array([[0, 1, 1, 0, 1],
              [0, 1, 0, 1, 0]])

array = np.vstack((a, b))

print(array)

# @exercise_range

array1 = np.array ([2, 6, 1, 9, 10, 3, 27])

array = array1[(array1 > 5) & (array1 <= 10)]

print(array)
