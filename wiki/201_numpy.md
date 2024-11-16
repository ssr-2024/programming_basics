# NumPy
NumPy (Numerical Python) ist eine Open-Source-Bibliothek für die Programmiersprache Python, die leistungsstarke Funktionen zur Verarbeitung und Analyse von großen Datenmengen sowie für numerische Berechnungen bereitstellt. NumPy bietet eine breite Palette an Funktionen für mathematische Operationen und ermöglicht eine schnelle und effiziente Arbeit mit Listen, welche in NumPy als "Arrays" bezeichnet werden. Der wesentliche Unterschied besteht darin, dass Arrays im Gegensatz zu normalen Listen in Python direkt für mathematische Operationen genutzt werden können.
 ```python
[7,23,69] - [1,2,3]           # ohne NumPy würde diese Rechnung einen TypeError -> siehe Wiki 004 ausgeben
    
 import numpy as np

np.array([7,23,69]) - np.array([1,2,3])           # mit NumPy kann dies nun gerechnet werden
    
array([6,21,66])              # Ausgabe
```
## Array erstellen
Zum Erstellen eines Arrays wird in NumPy die Funktion np.array() verwendet. Mit dieser Funktion lassen sich multi-dimensionale Arrays erzeugen.
```python
import numpy as np

array_1_dimension = np.array([1,2,3])

array_2_dimension = np.array([1,2,3],[4,3,2])

array_3_dimension = np.array([1,2,3],[4,3,2],[5,6,7])
```
## Daten aus Array abfragen
Mit Hilfe von Indices kann auf Numpy-Arrays zurückgegriffen werden.
### 1d array
In einem 1d Array erfolgt der Zugriff auf die Elemente über einen Index. Ähnlich wie bei Listen beginnt die Zählung hier bei 0. Das erste Element hat also den Index [0], das zweite den Index [1] etc.
```python
import numpy as np

array_1_dimension = np.array([1,2,3])

ausgabe = array_1_dimension[1]     # Ausgabe = 2
```
### 2d array
Bei einem 2d Array werden 2 Indices gebraucht. Der Erste um die Sub-Arrays anzusprechen, und der Zweite um die einzelnen Elemente herauszuschreiben.

```python
import numpy as np

array_2_dimension = np.array([[1,2,3],[4,3,2]])

ausgabe = array_2_dimension[1][0]      # Ausgabe = 4

```
### n-d array
Bei einem n-d Array werden n Indices gebraucht. Dem entsprechend werden für n grosse Arrays n Indices gebraucht.
## Rechnen mit Arrays
Mittles NumPy-Arrays können mathematische Operationen durchgeführt werden.
```python
    import numpy as np

    array1 = np.array([1,2,3])
    array2 = np.array([6,5,4])

    ausgabe1 = array1 + array2       # ausgabe1 = [7,7,7]

    ausgabe2 = array2 * 2            # ausgabe2 = [12,10,8]

    ausgabe3 = array2 // array1      # ausgabe3 = [6,2,1]

    ausgabe4 = array1 ** 2           # ausgabe4 = [1,4,9]
```