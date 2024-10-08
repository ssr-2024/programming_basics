# Übungen Termin 1


## [lab_001_datatypes.py](lab_001_datatypes.py)

### Exercise 1
Zu was werden die folgenden Ausdrücke evaluiert?

a.
```py
'Yes' + 'YesYes'
```
b.
```py
'NoNoNo' * 3
```
c.
```py
'12 * 3 = {12 * 3}'
```
d.
```py
f'12 * 3 = {12 * 3}'
```

### Exercise 2
Flicke die Skripts ohne dabei Operatoren zu entfernen.

#### 2.c Folgefrage
Kommen noch weitere Datentypen für `repeat_n` in Frage? Oder warum nicht?

### Exercise 3
**a.)**
Schreibe ein Skript, welches den Benutzer nach einer Eingabe fragt und dann die Länge des Eingabetextes zurückgibt.
Beispiel:
```sh
>>> Enter something: foobar
>>> 6
```

**b.)** Erweitere *3a.)* so, dass der eingegebene Text ebefalls angezeigt wird.

Beispiel:
```sh
>>> Enter something: foobar
>>> foobar: 6 Letters
```

## [lab_002_variables.py](lab_002_variables.py)
### Exercise 1

Definiere zwei Variablen `name` und `vorname` und weise ihnen einen sinnvollen Wert zu.

### Exercise 2
**a.)** Was enthält die Variable `tore` nachdem das folgende Skript ausgeführt wurde?
```py
tore = 2
tore + 1
```

**b.)** Schreibe den vorgegebenen Code aus 2a so um, dass er wie erwartet funktioniert und die Variable erhöht wird.

### Exercise 3: Kreise
Definiere eine Variable `radius` und berechne damit die Fläche des resultierenden Kreises.
Zeige das Resultat mit `print()` an.

**Hinweis**: Um `pi` zu verwenden, muss pi zuerst aus der `math` Bibliothek importiert werden. Dies geschieht auf der erste Zeile mit:
```py
from math import pi
```
Anschliessend kann `pi` wie eine Variable verwendet werden.

Teste das Skript mit unterschiedlichen Werten für `radius`.

## [lab_003_errors.py](lab_003_errors.py)

### Exercise 1: Fehlermeldungen erzeugen

**a.)** Erzeuge die folgende Fehlermeldung:
```
TypeError: can only concatenate str (not "float") to str
```
**b.)** Erzeuge die folgende Fehlermeldung:
```
TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'int'
```
**c.)** Erzeuge die folgende Fehlermeldung:
```
ZeroDivisionError: division by zero
```

### Exercise 2: Welche Fehlermeldung passt?

```py
'some ' + 'text' = a
```
- [ ] `NameError: name 'a' is not defined`
- [x] `SyntaxError: can't assign to operator`
- [ ] `TypeError: unsupported operand type(s) for |: 'str' and 'str'`
- [ ] `TypeError: Can't convert 'str' object to int implicitly`