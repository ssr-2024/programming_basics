# Fehlermeldungen

Bekannte Fehlermeldungen:

- [NameError](#NameError)
- [SyntaxError](#NameError)
- [IndentationError](#NameError)
- [TypeError](#NameError)



## NameError
`NameError: name 'a' is not defined`
## Ursache
Aufruf einer Variable oder Funktion, die im aktuellen Skript nicht definiert ist.
## Mögliche Ursachen
- Variable/Funktion erst später im Skript definiert?
- Fehlender Import eines Python-Moduls, welches die Variable/Funktion definiert?
## Beispiel
```py
print(x)  # x ist nicht definiert
```
## SyntaxError
`SyntaxError: invalid syntax``
## Ursache
Beschreibt einen Fehler im Aufbau des Codes.
## Mögliche Ursachen
- Schreibfehler
- Fehlendes Zeichen wie zum Beispiel das Schliessen der Klammer
## Beispiel
```python
if True  # Fehlender Doppelpunkt
    print("Hello")
```
## IntendationError
`IndentationError: inconsistent use of tabs and spaces in indentation`
## Ursache
Tritt dann ein Wenn die Einrückung nicht korrekt ist
## Mögliche Ursachen
- Fehlende Einrückung
- Unerwartete Einrückung
- Inkonstistene Einrückung
## Beispiel
```python
def greet():
print("Hello")  # Nicht eingerückt
````

## TypeError
`TypeError: can only concatenate str (not "int") to str`
## Ursache
Tritt dann ein wenn eine Operation mit inkopatiblen Datentypen ausgeführt wird oder eine Funktion mit einer falschen Zahle oder Art von Argumenten aufgerufen wird
## Mögliche Ursachen
- Unzulässige Operation zwischen verschiedenen Datentypen
- Falsche Anzahl an Argumenten in einer Funktion
- Falscher Typ bei einem Funktionsargument
- Ungültige Typen in einem Operator
## Beispiel
```python
import math
math.sqrt("16")
TypeError: must be real number, not str     #Funktion muss Zahl beinhalten und nicht einen String
````

