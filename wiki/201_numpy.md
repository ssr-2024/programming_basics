# NumPy in Python

NumPy ist eine leistungsfähige Bibliothek für numerische Berechnungen in Python. Sie bietet das Konzept von Arrays, die für effizientes Speichern und Verarbeiten großer Mengen numerischer Daten verwendet werden.

### Installation
Um NumPy zu verwenden, muss es zunächst installiert werden. Dies kann über die Kommandozeile erfolgen:

```python
pip install numpy
```

### Verwendung
Nach der Installation kann NumPy importiert und für numerische Berechnungen und die Arbeit mit Arrays verwendet werden:

```python
import numpy as np
```

## Array erstellen

Arrays sind das zentrale Datenformat in NumPy. Sie können eindimensional (1D), zweidimensional (2D) oder mehrdimensional (n-D) sein.

### Beispiel 1: Erstellen eines eindimensionalen Arrays (1D)

```python
import numpy as np

array_1d = np.array([1, 2, 3, 4, 5])
print("1D Array:", array_1d)# Ausgabe:1D Array: [1 2 3 4 5] 
```


### Beispiel 2: Erstellen eines zweidimensionalen Arrays (2d)

```python
array_2d = np.array([[1, 2, 3], [4, 5, 6]])
print("2d Array:\n", array_2d) #Ausgabe: 2D Array:
 [[1 2 3]
  [4 5 6]]
```

### Beispiel 3: Erstellen eines dreidimensionalen Arrays (n-d)

```python
array_3d = np.array([
    [[1, 2, 3], [4, 5, 6]],
    [[7, 8, 9], [10, 11, 12]]
])
print("3d Array:\n", array_3d) #Ausgabe: 3D Array:
 [[[ 1  2  3]
   [ 4  5  6]]

  [[ 7  8  9]
   [10 11 12]]]
```


# Daten aus Array abfragen

Daten in NumPy-Arrays lassen sich über Indizes abfragen. Je nach Dimension kann man auf einzelne Elemente oder Bereiche zugreifen.

## 1D Array

### Zugriff auf einzelne Elemente

Im eindimensionalen Array kann man durch Angabe des Indexes auf spezifische Elemente zugreifen.

```python
import numpy as np

array_1d = np.array([1, 2, 3, 4, 5])
print("Element bei Index 2 im 1D Array:", array_1d[2])  # Ausgabe: 3
```

### Zugriff auf mehrere Elemente im 1d-Array (Slicing)

Durch Slicing lassen sich bestimmte Bereiche eines Arrays auswählen.

```python
print("Bereich von Index 1 bis 3 im 1d Array:", array_1d[1:4])  # Ausgabe: [2, 3, 4]
```

## 2d Array

### Zugriff auf Zeilen und Spalten im 2d-Array

In einem zweidimensionalen Array kann man auf spezifische Zeilen, Spalten oder Teilbereiche zugreifen.

```python
print("Erste Zeile im 2d Array:", array_2d[0])  # Ausgabe: [1, 2, 3]
print("Element in Zeile 2, Spalte 1:", array_2d[1, 0])  # Ausgabe: 4

# Zugriff auf Teilbereiche im 2d-Array (Slicing)
print("Erste zwei Spalten in beiden Zeilen:\n", array_2d[:, :2])  # Ausgabe: [[1, 2], [4, 5]]
```

## n-d Array
### Zugriff auf Elemente in einem 3d-Array

In einem dreidimensionalen Array kann man ebenso auf einzelne Elemente und Bereiche zugreifen.

```python
print("Erstes Element der zweiten Matrix:", array_3d[1, 0, 0])  # Ausgabe: 7

# Zugriff auf Teilbereiche in einem 3d-Array (Slicing)
print("Alle Elemente in der ersten Spalte jeder Matrix:\n", array_3d[:, :, 0])  # Ausgabe: [[1, 4], [7, 10]]
```


## Rechnen mit Arrays

NumPy ermöglicht effiziente Berechnungen mit Arrays. Operationen werden elementweise auf die Array-Elemente angewendet.

### Beispiel 1: Addition von Arrays

```python
array_a = np.array([1, 2, 3])
array_b = np.array([4, 5, 6])
print("Array A:", array_a)
print("Array B:", array_b)
print("A + B:", array_a + array_b)  # Ausgabe: [5, 7, 9]
```

### Beispiel 2: Multiplikation jedes Elements mit einer Zahl (Skalierung)

```python
print("A * 3:", array_a * 3)  # Ausgabe: [3, 6, 9]
```

### Beispiel 3: Elementweise Multiplikation zweier Arrays
 
```python
print("A * B:", array_a * array_b)  # Ausgabe: [4, 10, 18]
```

### Beispiel 4: Berechnung des Mittelwerts, der Summe und der Standardabweichung eines Arrays

```python
print("Mittelwert von A:", np.mean(array_a))         # Ausgabe: 2.0
print("Summe von A:", np.sum(array_a))               # Ausgabe: 6
print("Standardabweichung von A:", np.std(array_a))  # Ausgabe: ~0.82
```

### Beispiel 5: Matrixmultiplikation (nur für 2d-Arrays möglich)

```python
array_c = np.array([[1, 2], [3, 4]])
array_d = np.array([[5, 6], [7, 8]])
print("Matrixmultiplikation von C und D:\n", np.dot(array_c, array_d))
```