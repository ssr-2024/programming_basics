import time as tt
from os import path
import json
import numpy as np

# LOAD DATA
with open(path.join(path.dirname(__file__), 'data/esc_data.json')) as json_file:
    data = json.load(json_file)

# samples, recorded @200Hz
samples = len(data['left'][0])


# append version:

# initialize result vectors
top_left = []
top_left_x = []
top_left_y = []
top_left_z = []
top_right = []
top_right_x = []
top_right_y = []
top_right_z = []

# CALCULATE RESULT WITH LISTS
# ...
t0 = tt.perf_counter()
for i in range(samples):
    top_left_x.append(data['left'][0][i] - data['top'][0][i])
    top_left_y.append(data['left'][1][i] - data['top'][1][i])
    top_left_z.append(data['left'][2][i] - data['top'][2][i])

    top_right_x.append(data['right'][0][i] - data['top'][0][i])
    top_right_y.append(data['right'][1][i] - data['top'][1][i])
    top_right_z.append(data['right'][2][i] - data['top'][2][i])

top_left.append(top_left_x)
top_left.append(top_left_y)
top_left.append(top_left_z)
top_right.append(top_right_x)
top_right.append(top_right_y)
top_right.append(top_right_z)
execution_time_list_append = tt.perf_counter() - t0
# report results
print(f"Execution time List Append: {execution_time_list_append} s.")


# loop version

# initialize result vectors

zero24 = [0] * samples
top_right = [zero24.copy(), zero24.copy(), zero24.copy()]
top_left = [zero24.copy(), zero24.copy(), zero24.copy()]

# CALCULATE RESULT WITH LISTS
# ...
t0 = tt.perf_counter()

for i in range(samples):
    for j in range(3):
        top_left[j][i] = (data['left'][j][i] - data['top'][j][i])
        top_right[j][i] = data['right'][j][i] - data['top'][j][i]

execution_time_lists = tt.perf_counter() - t0
# report results
print(f"Execution time Lists: {execution_time_lists} s.")

# WITH NUMPY ARRAYS
np_data = {
    'left': np.array(data['left']),
    'right': np.array(data['right']),
    'top': np.array(data['top'])
}

# CALCULATE RESULT WITH NUMPY
# ...
top_left = []
top_right = []

t0 = tt.perf_counter()

top_left = np_data['left'] - np_data['top']
top_right = np_data['right'] - np_data['top']

execution_time_numpy = tt.perf_counter() - t0


# REPORT COMPARISON
print(f"Execution time NumPy: {execution_time_numpy} s.")
print(f"Speed Up Factor: {execution_time_lists/execution_time_numpy} x.")
