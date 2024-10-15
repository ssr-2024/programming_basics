# Numpy

## Inhaltsverzeichnis
- [Numpy](#numpy)
  - [Inhaltsverzeichnis](#inhaltsverzeichnis)
    - [1. Introduction to NumPy](#1-introduction-to-numpy)
    - [2. How to create a NumPy array?](#2-how-to-create-a-numpy-array)
    - [3. How to inspect the size and shape of a NumPy array?](#3-how-to-inspect-the-size-and-shape-of-a-numpy-array)
    - [4. How to extract specific items from an array?](#4-how-to-extract-specific-items-from-an-array)
      - [4.1 How to reverse the rows and the whole array?](#41-how-to-reverse-the-rows-and-the-whole-array)
      - [4.2 How to represent missing values and infinite?](#42-how-to-represent-missing-values-and-infinite)
      - [4.3 How to compute mean, min, max on the ndarray?](#43-how-to-compute-mean-min-max-on-the-ndarray)
    - [5. How to create a new array from an existing array?](#5-how-to-create-a-new-array-from-an-existing-array)
    - [6. Reshaping and Flattening Multidimensional arrays](#6-reshaping-and-flattening-multidimensional-arrays)
      - [6.1 What is the difference between flatten() and ravel()?](#61-what-is-the-difference-between-flatten-and-ravel)
    - [7. How to create sequences, repetitions, and random numbers?](#7-how-to-create-sequences-repetitions-and-random-numbers)
      - [7.1 How to create repeating sequences?](#71-how-to-create-repeating-sequences)
      - [7.2 How to generate random numbers?](#72-how-to-generate-random-numbers)
      - [7.3 How to get the unique items and the counts?](#73-how-to-get-the-unique-items-and-the-counts)

### 1. Introduction to NumPy
NumPy ist eine leistungsstarke Bibliothek für die Arbeit mit Arrays und Matrizen in Python. Sie bietet eine Vielzahl von Funktionen für mathematische Operationen, die auf diesen Arrays durchgeführt werden können. NumPy ist besonders nützlich für wissenschaftliches Rechnen und Datenanalyse, da es eine effiziente Speicherung und Verarbeitung von großen Datenmengen ermöglicht.

### 2. How to create a NumPy array?
NumPy-Arrays können mit der Funktion `np.array()` erstellt werden, die eine Liste oder eine andere Sequenz als Eingabe akzeptiert. Es gibt auch spezielle Funktionen wie `np.zeros()`, `np.ones()`, und `np.arange()`, um Arrays mit bestimmten Eigenschaften zu generieren. Beispiel:

```python
import numpy as np
arr = np.array([1, 2, 3])
```

### 3. How to inspect the size and shape of a NumPy array?
Um die Größe und die Form eines NumPy-Arrays zu überprüfen, verwendet man die Attribute `.size` und `.shape`. `.size` gibt die Gesamtzahl der Elemente zurück, während `.shape` die Dimensionen des Arrays als Tupel angibt.

```python
arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr.shape)  # Ausgabe: (2, 3)
print(arr.size)   # Ausgabe: 6
```

### 4. How to extract specific items from an array?
Um spezifische Elemente aus einem NumPy-Array zu extrahieren, kann man Indizes verwenden. Man kann auch boolesche Arrays verwenden, um Elemente basierend auf bestimmten Bedingungen auszuwählen.

```python
print(arr[0, 1])  # Gibt das Element in der ersten Zeile und zweiten Spalte zurück
```

#### 4.1 How to reverse the rows and the whole array?
Um die Zeilen eines Arrays umzukehren, kann man den Slice `[::-1]` verwenden. Um das gesamte Array umzukehren, verwendet man die Methode `np.flip()` oder auch `arr[::-1, ::-1]`.

```python
reversed_rows = arr[::-1]
reversed_array = np.flip(arr)
```

#### 4.2 How to represent missing values and infinite?
Fehlende Werte können in NumPy durch `np.nan` dargestellt werden, während unendliche Werte durch `np.inf` oder `-np.inf` repräsentiert werden. NumPy bietet Funktionen wie `np.isnan()` zur Überprüfung von `NaN`.

```python
missing_value_array = np.array([1, 2, np.nan])
infinite_value_array = np.array([1, 2, np.inf])
```

#### 4.3 How to compute mean, min, max on the ndarray?
Um den Mittelwert, das Minimum und das Maximum eines Arrays zu berechnen, verwendet man die Funktionen `np.mean()`, `np.min()`, und `np.max()`. Diese Funktionen können auch über bestimmte Achsen angewendet werden.

```python
mean_value = np.mean(arr)
min_value = np.min(arr)
max_value = np.max(arr)
```

### 5. How to create a new array from an existing array?
Um ein neues Array aus einem bestehenden zu erstellen, kann man Funktionen wie `np.copy()` verwenden, um eine Kopie des Arrays zu erstellen, oder mit Slicing ein neues Array basierend auf einem Teil des Originals zu erzeugen.

```python
new_array = arr.copy()
subset_array = arr[:, 1]  # Extrahiert die zweite Spalte
```

### 6. Reshaping and Flattening Multidimensional arrays
Um mehrdimensionale Arrays umzustrukturieren, verwendet man die Methode `reshape()`. Diese Methode ändert die Form des Arrays, solange die Anzahl der Elemente gleich bleibt.

```python
reshaped_array = arr.reshape(3, 2)  # Beispiel für eine neue Form
```

#### 6.1 What is the difference between flatten() and ravel()?
`flatten()` gibt eine Kopie des Arrays in einflächiger Form zurück, während `ravel()` eine flache Ansicht des Arrays zurückgibt, die bei Bedarf eine Kopie sein kann. `ravel()` ist in der Regel schneller und speichereffizienter.

```python
flattened_array = arr.flatten()
raveled_array = arr.ravel()
```

### 7. How to create sequences, repetitions, and random numbers?
NumPy bietet Funktionen wie `np.linspace()` und `np.arange()`, um Sequenzen zu erstellen. Für Wiederholungen kann `np.repeat()` verwendet werden, während `np.random` eine Vielzahl von Funktionen für die Erzeugung von Zufallszahlen bereitstellt.

```python
sequence = np.arange(0, 10, 2)  # Erzeugt die Sequenz [0, 2, 4, 6, 8]
```

#### 7.1 How to create repeating sequences?
Um sich wiederholende Sequenzen zu erstellen, kann man `np.tile()` verwenden, um ein Array mehrmals zu wiederholen.

```python
repeated_sequence = np.tile([1, 2, 3], 3)  # Gibt [1, 2, 3, 1, 2, 3, 1, 2, 3] zurück
```

#### 7.2 How to generate random numbers?
Zufallszahlen können mit `np.random.rand()`, `np.random.randint()`, oder `np.random.randn()` erzeugt werden. Diese Funktionen bieten verschiedene Arten von Zufallszahlen.

```python
random_numbers = np.random.rand(5)  # Erzeugt 5 Zufallszahlen zwischen 0 und 1
```

#### 7.3 How to get the unique items and the counts?
Um die einzigartigen Elemente eines Arrays und deren Häufigkeit zu erhalten, kann man `np.unique()` verwenden. Diese Funktion gibt sowohl die einzigartigen Elemente als auch deren Zählungen zurück.

```python
unique_items, counts = np.unique(arr, return_counts=True)
```

Diese Zusammenfassung bietet einen Überblick über die grundlegenden Funktionen und Anwendungen von NumPy, die für Datenanalyse und wissenschaftliches Rechnen in Python nützlich sind.