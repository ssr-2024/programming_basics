import numpy as np

# @exercise_1
array = np.arange(10)
print(array)
"""
Erstellt einn numpy-array ohne explizite Angabe zu den Elementen
"""

# @exercise_2
array = np.full((4, 3), 4)
print(array)
"""
Erstellt ein numpy-array mit Angabe auf die Zahl, die Anzahl Zahlen in der Zeile und die Anzahl Zeilen
"""

# @exercise_3
array = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
array = array[1::2]
print(array)
"""
Erstellt ein numpy-array und eleminiert dabei die Zahlen, welche durch 2 teilbar sind
"""

# @exercise_4
array = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
array[1::2] = -1
print(array)
"""
Erstellt ein numpy-array und ersetzt dabei die Zahlen, welche nicht durch 2 teilbar sind mit (-1)
"""

# @exercise_5
init = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
array = init.copy()
array[::2] = -1
print(array)
"""
Erstellt ein numpy-array und ersetzt dabei die Zahlen, welche durch 2 teilbar sind mit (-1)
"""

# @exercise_reshape
array = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
array = array.reshape(2, 5)
print(array)
"""
Erstellt ein numpy-array mit der Vorgabe über die Zeilenanzahl (2) und die Anzahl der Zahlen pro Zeile (5)
"""

# @exercise_stack
a = np.array([[0, 1, 2, 3, 4],
              [0, 0, 0, 0, 0]])
b = np.array([[0, 1, 1, 0, 1],
              [0, 1, 0, 1, 0]])
array = np.vstack((a, b))
print(array)
"""
Erstellt ein zwei numpy-array (a, b) und kombiniert sie vertikal zu neuen Array und gibt  Ergebnis aus
"""

# @exercise_range
array = np.array([2, 6, 1, 9, 10, 3, 27])
array = array[(array > 5) & (array <= 10)]
print(array)
"""
Erstellt ein numpy-array mit Vorgabe alle kleineren Zahlen als 5 und grösser oder gleich 10 ebenfalls zu eleminieren
"""
