# Datentypen

In Python gibt es verschiedene Datentypen, die verwendet werden, um unterschiedliche Arten von Daten zu speichern.

Einige der gängigsten Datentypen werden im Folgenden erklärt.

## Gängige Datentypen

- **int**: Ganzzahlen  
  Beispiele: `1`, `100`, `-50`

- **float**: Gleitkommazahlen  
  Beispiele: `3.14`, `-0.001`

- **str**: Zeichenketten (Strings)  
  Beispiele: `"Hallo"`, `"Python"`

- **bool**: Wahrheitswerte  
  Beispiele: `True`, `False`

- **list**: Listen, veränderbare Sammlungen von Elementen  
  Beispiele: `[1, 2, 3]`, `["Apfel", "Banane", "Kirsche"]`

- **tuple**: Tupel, unveränderbare Listen  
  Beispiele: `(1, 2, 3)`, `("Rot", "Grün", "Blau")`

- **dict**: Wörterbücher, Sammlungen von Schlüssel-Wert-Paaren  
  Beispiel: `{"Name": "Nicolas", "Alter": 30}`


## Spezialfall `None`

`None` ist ein spezieller Datentyp in Python, der verwendet wird, um das Fehlen eines Wertes zu kennzeichnen.

```python
x = None
print(x)  # Ausgabe: None
```

## Spezialfall `nan`

`nan` steht für "Not a Number" und wird hauptsächlich im Zusammenhang mit Gleitkommazahlen und mathematischen Operationen verwendet. Es kennzeichnet einen nicht existierenden oder undefinierten numerischen Wert.

```python
import math
x = float('nan')
y = 5

print(math.isnan(x))  # Ausgabe: True
print(x + y)          # Ausgabe: nan
```


## Datentyp einer Variable bestimmen

Der Datentyp einer Variable kann mit der Funktion `type()` bestimmt werden.

```python
x = 10
print(type(x))  # Ausgabe: <class 'int'>

y = 3.14
print(type(y))  # Ausgabe: <class 'float'>
``` 


## Umwandlung zwischen Datentypen (casten)

In Python kann man Daten von einem Typ in einen anderen Typ umwandeln ("Casten"):

```python
# Integer zu String
x = 42
print(str(x), type(str(x)))  # Ausgabe: "42" <class 'str'>

# String zu Integer
y = "10"
print(int(y), type(int(y)))  # Ausgabe: 10 <class 'int'>

# Float zu Integer
z = 3.14
print(int(z), type(int(z)))  # Ausgabe: 3 <class 'int'>

# Liste zu Tuple
list_data = [1, 2, 3]
print(tuple(list_data), type(tuple(list_data)))  # Ausgabe: (1, 2, 3) <class 'tuple'>

