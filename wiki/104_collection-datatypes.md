# Sammel-Datentypen

In Python existieren vier Datentypen zum Zusammenfassen von Daten:
- `Lists`
- `Tuples`
- `Sets`
- `Dictionaries`

Wir betrachten vorerst nur `Lists` und `Dictionaries`

## `Lists`
Listen können genutzt werden um Objekte zu speichern. Sehr nützlich sind Listen, wenn über die Objekte iteriert werden soll. 
### `range()` and `list()`
Die `range()`-Funktion erzeugt eine Sequenz von Zahlen, die oft in Schleifen verwendet wird. Mit der `list()`-Funktion kann diese Sequenz in eine Liste umgewandelt werden.
### `slice()`
```Python
numbers = list(range(1, 6))
# numbers = [1, 2, 3, 4, 5]
```

### Listen in Listen
Mehrdimensionale Listen können durch Listen in Listen erstellt werden:
```Python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
```


## `Dictionaries`
`Dictionnaries` haben einen `key` mit dem auf gespeicherte Werte zugegriffen werden kann.

Beispiel:
```Python
person = {
    "name": "Alice",
    "age": 30,
    "city": "Berlin"
}

# person[name] = "Alice"
```
Neue Werte können so hinzugefügt werden:
```Pyhon
person["email"] = "alice@example.com"
```
Entfernen von Werten:
```Python
del person["age"]  # Entfernen
```
Iterieren durch `Dictionnaries`:
```Python
for key in person:
    print(key, person[key])

for value in person.values():
    print(value)

for key, value in person.items():
    print(key, value)
```
