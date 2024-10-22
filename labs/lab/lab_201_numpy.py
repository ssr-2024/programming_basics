import numpy as np

# @exercise_1

import numpy as np
# mit arange erstellen wir ein Array mit 10 Elementen, beginnend immer bei 0.
array = np.arange(10)
print(array)

# @exercise_2

import numpy as np
# full wird verwendet, um das ganze array mit einer bestimmten Zahl zu füllen. die erste zahl in der klammer definiert die anzahl zeilen, die zweite zahl definiert die anzahl spalten. mit der dritten zahl wird definiert, mit welcher zahl das array gefüllt werden soll.
array = np.full((4, 3), 4)
print(array)

# @exercise_3

import numpy as np
# Ausgangsarray
array1 = np.arange(10)
# mit [1::2] wird das Array von der 1. Stelle bis zum Ende genommen und nur jeder zweite Wert ausgegeben.
array = array1[1::2]
print(array)

# @exercise_4

import numpy as np
# Ausgangsarray
array = np.arange(10)
array [array % 2 !=0] = -1
print(array)

# @exercise_5
import numpy as np
# Ausgangsarray
init = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
# mit dem Befehl .copy() wird eine Kopie des Arrays erstellt, damit bleibt das Ausgangsarray unverändert.
array = init.copy()
# Setze jeden zweiten Wert auf -1, beginnend bei Index 0
array[0::2] = -1
print(array)

# @exercise_reshape

import numpy as np
# Ausgangslage
array1 = np.arange(10)
# mit dem Befehl .reshape() wird das Array in eine Matrix umgewandelt. Die erste Zahl in der Klammer definiert die Anzahl der Zeilen, die zweite Zahl die Anzahl der Spalten. In diesem Beispiel also 2 Zeilen und 5 Spalten.
array = array1.reshape(2, 5)
print(array)

# @exercise_stack

import numpy as np
# Ausgangslage
a = np.array([[0, 1, 2, 3, 4],
              [0, 0, 0, 0, 0]])
b = np.array([[0, 1, 1, 0, 1],
              [0, 1, 0, 1, 0]])
# mit dem Befehl vstack() werden die beiden Arrays vertikal gestapelt. mit dem Befehl hstack() würden die beiden Arrays horizontal gestapelt werden. Bildlich vorgstellt bedeutet das, dass die Zeilen der beiden Arrays aneinander gehängt werden.
array = np.vstack((a, b))
print(array)

# @exercise_range

import numpy as np
# Ausgangslage
array1 = np.array([2, 6, 1, 9, 10, 3, 27])
# Wir fügen 2 Boolesche Bedingungen ein, die alle Werte zwischen 5 und 10 ausgeben. Mit dem &-Zeichen wird ein AND generiert.
array = array1[(array1 > 5) & (array1 <= 10)]
print(array)
