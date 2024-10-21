import numpy as np
# @exercise_1
    
array = np.arange(10)
    
# @exercise_2

array = np.full((4, 3), 4)

# @exercise_3

array = np.arange(1, 10, 2)

# @exercise_4

array = np.arange(10)
array [np.arange(1,10,2)] = -1


# @exercise_5
init = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

array = init.copy() #creates a copy from *init* to modify it 
array [np.arange(0,9,2)] = -1


# @exercise_reshape

array = np.arange(10).reshape(2,5)

# @exercise_stack
a = np.array([[0, 1, 2, 3, 4], [0, 0, 0, 0, 0]])
b = np.array([[0, 1, 1, 0, 1], [0, 1, 0, 1, 0]])

array = np.vstack((a,b))

# @exercise_range

# Defining the function to solve the exercise
def exercise_range() -> np.ndarray:
    """
    Filter the elements of an array to return only the values greater than 5 
    and less than or equal to 10.

    Parameters
    ----------
    None

    Returns
    -------
    array : numpy.ndarray
        A NumPy array containing the elements greater than 5 and less than or 
        equal to 10 from the original array.
    """

    # original array
    array = np.array([2, 6, 1, 9, 10, 3, 27])
    
    # filtering the arry
    array = array[(array > 5) & (array <= 10)]
    
    return array

# Calling the function and storing the result in the variable array

array = exercise_range()
array = np.array(array)
array













