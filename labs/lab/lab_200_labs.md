# Übungen Termin 4

## [lab_201_numpy](lab_201_numpy.py)
Alle Resultate sollen für diese Übung als Variable `array` gespeichert werden.
### Exercise 1
Erstelle ein numpy-array `array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])` ohne dabei alle Elemente explizit anzugeben.

### Exercise 2
Erstelle ein numpy-array ohne dabei alle Elemente explizit anzugeben:
```py
array([[4, 4, 4],
       [4, 4, 4],
       [4, 4, 4],
       [4, 4, 4]])
```

### Exercise 3

Ausgangslage: `array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])`
Gewünschter Output: `array([1, 3, 5, 7, 9])`


### Exercise 4

Ausgangslage: `array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])`
Gewünschter Output: `array([0, -1, 2, -1, 4, -1, 6, -1, 8, -1])`

### Exercise 5
Ausgangslage: `array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])`
Gewünschter Output: `array([-1, 1, -1, 3, -1, 5, -1, 7, -1, 9])`
Die Variable `init` darf sich nicht ändern.


### Exercise reshape
Ausgangslage: `array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])`
Output:
```py
array([[0, 1, 2, 3, 4],
       [5, 6, 7, 8, 9]])
```


### Exercise stack
Ausgangslage:
```py
a = np.array([[0, 1, 2, 3, 4],
              [0, 0, 0, 0, 0]])
b = np.array([[0, 1, 1, 0, 1],
              [0, 1, 0, 1, 0]])
```

Output:
```py
np.array([[0, 1, 2, 3, 4],
          [0, 0, 0, 0, 0],
          [0, 1, 1, 0, 1],
          [0, 1, 0, 1, 0]])
```

### Exercise range
Ausgangslage: `array([2, 6, 1, 9, 10, 3, 27])`
Output: Alle Elemente grösser `5` und kleiner gleich `10`
```py
array([6, 9, 10])
```

## [lab_202_circshift](lab_202_circshift.py)

**Voraussetzung**: Den Abschnitt "Local and Global Scope" in Kapitel 3 gelesen.

Das in der Übung [lab_103_collections](lab_103_collections.py) verwendete Herz soll wie auf einer Werbetafel animiert werden:

<img src="../images/202_moving_heart.gif" width="300">

Implementiere als erstes die Funktion `reset()`. Sie soll die Ausgangslage wiederherstellen, so dass in der Variable `heart` wieder das ursprüngliche Herz gespeichert ist.

Implementiere die beiden Funktionen `circshift_left_to_right()` und `circshift_top_to_bottom()`.

**Hinweis**: Von einer Freundin weisst du, dass diese Aufgabe in Matlab mit der Funktion `circshift()` sehr einfach umgesetzt werden kann.

