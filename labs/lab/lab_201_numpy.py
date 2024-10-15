import numpy as np

# @exercise_1
import numpy as np
array = np.arange(0, 10)
print(array)
# @exercise_2
array = np.full((4, 3), 4)
print(array)
# @exercise_3
array=np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
array = array[array % 2 == 1]
# @exercise_4
init4_arrary=np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
array = np.where(init4_arrary % 2 == 0, init4_arrary, -1)
# @exercise_5
init = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
array = np.where(init % 2 == 0, -1,init)
'''
np.where(condition, x, y): This is a NumPy function that returns elements chosen from x or y based on the condition. It evaluates the condition for each element in the input array and selects:

x if the condition is True
y if the condition is False
'''
# @exercise_reshape
init = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
array = init.reshape(2, 5)
'''
Die Parameter (2, 5) geben an, dass das neue Array 2 Zeilen 
und 5 Spalten haben soll. In diesem Fall wird das ursprüngliche 
eindimensionale Array (10 Elemente) in ein zweidimensionales Array 
mit der Form 2x5 umgewandelt.
'''
# @exercise_stack
a = np.array([[0, 1, 2, 3, 4],
              [0, 0, 0, 0, 0]])
b = np.array([[0, 1, 1, 0, 1],
              [0, 1, 0, 1, 0]])
array = np.vstack((a, b))
# @exercise_range
range_array = np.array([2, 6, 1, 9, 10, 3, 27])
array = range_array[(range_array > 5) & (range_array <= 10)]