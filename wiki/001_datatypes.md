# Datentypen
Python bietet eine Vielzahl an Datentypen, die von einfachen Zahlen bis hin zu komplexen Datenstrukturen reichen. Primitive Typen wie int, float, bool und str sind die Grundbausteine der meisten Programme. Mit komplexeren Datentypen wie list, tuple, set, und dict lassen sich vielfältige Datenstrukturen darstellen.

## Gängige Datentypen
Untenstehend werden gängige Datentypen für den gebrauch von Python kurz gezeigt.

### `int` für Integer
Ganze Zahlen, sowohl positiv wie negativ möglich. Null (`0`) ist ebenfalls erlaubt.

```python
a = 13
b = -12
c = 0

print(type(a)) # Ausgabe --> <class 'int'>
````

### "float" für Floating-Point oder 
Zahlen mit Dezimalpunkt, sowohl positiv wie negativ möglich. Achtung, auch ganze Zahlen können als Floating-Point interpretiert werden, Bsp. 69.0.

```python
a = 69.0
b = -0.001
c = 3.1415

print(type(b)) # Ausgabe --> <class 'float'>
```

### `strs` für Strings
Dient als Bezeichung für Textwerte. Damit die Strings tatsächlich als solche gesehen werden müssen einfache Anführungszeichen am Anfang des Strings sowie am Ende platziert werden damit das Format als solches erkannt werden kann. Der String kann dabei ebenfalls nichts beinhalten wie am beispiel für Wert `c` ersichtlich

```python
a = 'Matthieu'
b = "Howdy Cowboy"
c = ''

print(type(b)) # Ausgabe --> <class 'str'>
```

### `bool` für Boolesche Werte
Kann die Werte `true` oder `false`besitzen. Diese Funktion kommt vor allem dann zum Einsatz wenn es darum geht Bedingungen oder Verzweigungen auszudrücken.

```python
a = True
b = False

print(type(a)) # Ausgabe --> <class 'bool'>
```


### Spezialfall `None`
Der Wert `None` gibt in Python die Abwesenheit des Wertes an. Mittels dieser Funktion kann überprüft werden, ob die Variable definiert wurde oder eben noch nicht.

```python
a = None
b = "Hello World"
c = ''

print(type(a)) # Ausgabe --> <class 'NoneType'>
```


### Spezialfall `nan`
`nan` steht für "Not a Number". Dieser Wert wird dann verwendet, wenn durch die vorgegebenen Werte kein sinnvolles mathematisches Resultat generiert werden kann.


## Datentyp einer Variable bestimmen
In Python der Datentyp einer Variable mit der Funktion `type()` bestimmt werden. Diese Funktion gibt den Typ des übergebenen Objekts zurück.

```python
a = 42
print(type(a))  # Ausgabe: <class 'int'>

b = "Hello"
print(type(b))  # Ausgabe: <class 'str'>

c = [1, 2, 3]
print(type(c))  # Ausgabe: <class 'list'>
```
Des weiteren kann mittels `isinstance` überprüft werden, ob eine Variable tatsächlich zu einem bestimmten Datentyp gehört.

```python
a = 3.14
print(isinstance(x, int))  # Ausgabe: False

b = "Howdy"
print(isinstance(b, str))  # Ausgabe: True

c = [1, 2, 3]
print(isinstance(c, (list, tuple)))  # Ausgabe: True
```

## Umwandlung zwischen Datentypen (`casten`)
Das `casten` ermöglicht das ändern eines Datentyps von einem Wert in einen anderen.

```python
num_str = "123"
num_int = int(num_str)  # 123 (Integer)
num_float = float(num_str)  # 123.0 (Float)
```