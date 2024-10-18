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

