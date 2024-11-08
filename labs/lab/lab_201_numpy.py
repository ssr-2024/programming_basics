import numpy as np

# Exercise 1: Create an array of integers from 0 to 9
array = np.arange(0, 10)
print(array)
'''
np.arange(start, stop): This function generates an array containing a sequence of numbers.
In this case, it generates numbers from 0 to 9 (stop is exclusive).
'''

# Exercise 2: Create a 4x3 array filled with the value 4
array = np.full((4, 3), 4)
print(array)
'''
np.full(shape, fill_value): This function creates an array of the specified shape and fills it with the specified value.
Here, it creates a 4x3 array filled with the number 4.
'''

# Exercise 3: Extract all odd numbers from an array of integers from 0 to 9
array = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
array = array[array % 2 == 1]
'''
array[array % 2 == 1]: This applies a condition on the array, selecting only the elements
that satisfy the condition (i.e., odd numbers).
'''

# Exercise 4: Replace all odd numbers in an array of integers from 0 to 9 with -1
initial_array = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
array = np.where(initial_array % 2 == 0, initial_array, -1)
'''
np.where(condition, x, y): This function returns elements chosen from x or y based on the condition.
If the condition is True, elements are chosen from x; otherwise, from y.
Here, even numbers are retained, and odd numbers are replaced with -1.
'''

# Exercise 5: Replace all even numbers in an array of integers from 0 to 9 with -1
initial = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
array = np.where(initial % 2 == 0, -1, initial)
'''
np.where(condition, x, y): This function conditionally replaces elements.
If the condition is True (even number), it replaces the element with -1; if False, retains the element.
'''

# Exercise: Reshape a 1D array of integers from 0 to 9 to a 2D array with shape 2x5
initial = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
array = initial.reshape(2, 5)
'''
np.reshape(new_shape): This function reshapes an array without changing its data.
The new shape (2, 5) specifies 2 rows and 5 columns.
'''

# Exercise: Vertically stack two 2D arrays
a = np.array([[0, 1, 2, 3, 4],
              [0, 0, 0, 0, 0]])
b = np.array([[0, 1, 1, 0, 1],
              [0, 1, 0, 1, 0]])
array = np.vstack((a, b))
'''
np.vstack((array1, array2, ...)): This function vertically stacks arrays along the first axis (row-wise).
In this case, it stacks arrays `a` and `b` to form a new array.
'''

# Exercise: Extract elements from an array that fall within a specified range
range_array = np.array([2, 6, 1, 9, 10, 3, 27])
array = range_array[(range_array > 5) & (range_array <= 10)]
'''
array[condition]: This extracts elements based on a condition.
(range_array > 5) & (range_array <= 10) selects elements greater than 5 and less than or equal to 10.
'''
