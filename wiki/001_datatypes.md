# Datentypen in Python

## Gängige Datentypen
- **Integer**: Ganze Zahlen. Beispiel: `x = 10`
- **Float**: Gleitkommazahlen (in Python 64bit, entspricht IEEE 754 "double precision"). Beispiel: `x = 10.5`
- **String**: Zeichenketten, die in Anführungszeichen (`"` oder `'`) geschrieben werden. Beispiel: `x = "Hallo"`
- **List**: Geordnete, veränderbare Sammlung von Elementen, die verschiedene Datentypen enthalten kann. Beispiel: `x = [1, 2, 3]`
- **Dictionary**: Ungeordnete Sammlung von Schlüssel-Wert-Paaren. Beispiel: `x = {"name": "Max", "alter": 25}`
- **Boolean**: Wahrheitswert, der entweder `True` oder `False` sein kann. Beispiel: `x = True`

### Wichtige Hinweise zu Python-Datentypen
- **Char**: Es gibt keinen eigenen `char`-Datentyp in Python, da ein einzelnes Zeichen nur ein String mit der Länge 1 ist. Beispiel: `x = 'A'` ist ein String.
- **Double**: In Python gibt es keinen expliziten `double` Datentyp. `float` wird als 64-bit Gleitkommazahl gespeichert, was dem entspricht, was in anderen Sprachen als `double` bekannt ist.

### Spezialfall `None`
`None` ist ein spezieller Datentyp, der für einen nicht vorhandenen Wert steht. `None` wird häufig als Platzhalter verwendet, um das Fehlen eines Wertes auszudrücken. Beispiel: 
```python
x = None
```
Wichtig: `None` wird nicht als True oder False betrachtet, ist aber selbst als Falsch zu bewerten (`bool(None) == False`)
## Spezialfall `nan`
 `nan`steht für "not a number" (keine Zahl) und kommt typischerweise in Berechnungen vor, die nicht definiert sind, z.B. 0 geteilt durch 0. `nan` gehört zum `float`-Typ:
 ```python
 import math
 x = float('nan') # Oder math.nan
 ```
 Achtung: `nan==nan` ist immer `False`!
 ## Datentp einer Variable bestimmen
 Funktion `type()` nutzen um Datentyp einer variable bestimmen zu können.
 ```python 
 x=10
 print(type(x)) # Ausgabe: <class 'int'>
 ```
 ## Umwandlung zwischen Datentypen
 Zahlen:
 - `float()`:`int` --> `float` (geht ohne Informationsverlust)
 - `int()`: `float`--> `int`(kann hat informationsverlust und passiert ohne Runden: int(10.5) gibt 10 aus)
 - `list("abc")`gibt `['a', 'b', 'c']` aus.
 - `str(10)` gibt `"10"` aus
 - `dict('name', ''Max')` gibt ein dictionary aus, bei welchem 'Name' mit 'Max' verbunden ist
