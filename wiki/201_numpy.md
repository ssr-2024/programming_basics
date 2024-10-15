# NumPy
```Python
import numby as np
```
Mit NumPy können z.B. operationen auf Listen ausgeführt werden, welche mit den normalen Listen nicht möglich sind. Die Umsetzung in Python braucht viel Aufwand und funktioniert schlussendlich auch viel langsamer, als es mit NumPy möglich ist. In NumPy werden die Daten von Arrays so gespeichert, dass die Operationen viel effizienter funktionieren (Sind dann aber auch weniger flexibel).

## Array erstellen
Man kann aus Listen direkt `numpy.array` erstellen: 
```Python
list = [1, 2, 3]
np_array = np.array(list)
```
Das funktioniert auch automatisch mit 2D-Arrays. 
### Unterschiede zu normalen Listen
NumPy.Arrays sind dazu designed vektorisierte Operationen auf Arrays auszuführen. D.h. die Operation wird direkt auf allen Objekten des Arrays ausgeführt, nicht auf dem Array selbst.
<br>
Beispiel:
```Python
list + 2 # gibt einen Fehler aus
np_array + 2 # [3, 4, 5] alle Items sind um 2 erhöht
```

## Daten aus Array abfragen
Man kann bestimmte Teile aus dem Array abfragen.
<br>
Beispiel (die ersten 2 Reihen und Spalten):
```Python
arr2[:2, :2]
```
Gibt die ersten beiden Elemente, der ersten beiden Arrays wieder. (Zuerst sagt man welche Liste, dann welches Element (im 2D-Array))
### 1d array
```Python
list = [1, 2, 3]
np_array = np.array(list)
```
### 2d array
```Python
list2 = [[0,1,2], [3,4,5], [6,7,8]]
arr2d = np.array(list2)
```

### n-d array
```Python
list3 = [[[0,1,2], [3,4,5]],[ [6,7,8], [9, 10, 11]]]
arr2d = np.array(list3)
```

## Rechnen mit Arrays
Man kann Minimum, Maximum und Mittelwerte berechnen:
```Python
print("Mean value is: ", arr2.mean())
print("Max value is: ", arr2.max())
print("Min value is: ", arr2.min())
```
Man kann das Minimum auch pro Zeile berechnen:
```Python
# Row wise and column wise min
print("Column wise minimum: ", np.amin(arr2, axis=0))
print("Row wise minimum: ", np.amin(arr2, axis=1))
```
Für andere Funktionen kann man `.apply_over_axis` brauchen:
```Python
# Summe Achsenweise für die Achsen von 0-2 berechnen
np.apply_over_axes(np.sum, array, [0,2])

```