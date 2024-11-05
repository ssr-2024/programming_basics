# Funktionen
Das Prinzip der Modularität beschreibt die Wiederverwendbarkeit von Funktionen in verschiedenen Kontexten.

## Funktionen aufrufen
Man kann Funktionen die in einer Datei definiert sind direkt aufrufen. Die Basic-Python-Funktionen kann man auch von überall aufrufen. Wenn man Funktionen aus anderen Packages oder Dateien aufrufen möchte, muss man entweder zuerst das package importieren (dann wird die Funktion mit `package.function()` aufrufen). Wenn man die Funktion direkt importiert, kann man direkt auf die Funktion zugreifen ohne package nahmen.

## Funktionen von Bibliotheken aufrufen
Zuerst muss man die Bibliothek installieren:
```Python
import turtle as t
```
dann kann man die Funktionen aus dieser Bibliothek aufrufen:
```Python
t.forward(10)
```

## Funktionen definieren
Man kann auch eigene Funktionen definieren:
```Python
def my_function():
    print("my function was called")
```

### `return`
Mit dem Return statement kann man einen Rückgabewert definieren:
```Python
def my_function():
    print("my function was called")
    return "my function"
```
In diesem Fall wird einfach ein String zurückgegeben, der den Wert `'my function'` hat.

## Variablen in Funktionen
Man kann den Funktionen auch Variablen mitgeben, die in der Funktion genutzt werden können:
```Python
def add(a,b):
    return a+b
```
