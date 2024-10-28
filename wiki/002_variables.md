# Variablen

In Python können Variablen verwendet werden, um Daten zu speichern. Variablen haben Namen, die auf Speicheradressen verweisen, in denen die zugewiesenen Werte gespeichert sind.

## Variablenzuordnung

Eine einfache Variablenzuweisung erfolgt mit dem Zuweisungsoperator `=`. Der Wert auf der rechten Seite wird der Variablen auf der linken Seite zugewiesen.

### Beispiel:

```python
x = 10  # Die Variable `x` erhält den Wert 10.
print(x)  # Ausgabe: 10
```


### Es können auch verschiedene Typen in Variablen gespeichert werden:

```python
y = 3.14  # Variable `y` speichert einen float-Wert.
print(y)  # Ausgabe: 3.14

name = "Nicolas"  # Variable `name` speichert eine Zeichenkette (String).
print(name)  # Ausgabe: Nicolas
```


## Mehrfachzuweisung

Python erlaubt es, mehrere Variablen gleichzeitig zuzuweisen:

```python
a, b, c = 1, 2, 3
print(a, b, c)  # Ausgabe: 1 2 3
```

## Werte tauschen

Python bietet eine einfache Möglichkeit, die Werte zweier Variablen zu tauschen, ohne eine Zwischenvariable zu verwenden:

```python
a, b = b, a
print(a, b)  # Ausgabe: 2 1
```

### Variablen können auch nachträglich überschrieben werden:

```python
x = 42  # Der Wert von `x` wird von 10 auf 42 geändert.
print(x)  # Ausgabe: 42
```

## Dynamische Typisierung

In Python ist es nicht notwendig, den Typ einer Variable explizit anzugeben. Die Variablen passen sich dynamisch dem zugewiesenen Wert an.

```python
z = "Ich bin ein String"
print(z)  # Ausgabe: Ich bin ein String

z = 100  # Jetzt speichert `z` einen integer.
print(z)  # Ausgabe: 100
```
