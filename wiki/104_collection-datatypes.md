# Sammel-Datentypen

In Python existieren vier Datentypen zum Zusammenfassen von Daten:
- `Lists`
- `Tuples`
- `Sets`
- `Dictionaries`

Wir betrachten vorerst nur `Lists` und `Dictionaries`

## `Lists`
Eine Liste ist eine Sammlung von Werten, die in einer bestimmten Reihenfolge gespeichert sind. Sie wird mit eckigen Klammern dargestellt, wobei die einzelnen Elemente durch Kommas getrennt werden, beispielsweise `[..., ..., ...]`. In einer Liste können verschiedene Datentypen wie Strings, Integers oder Floats enthalten sein. Eine Mischung dieser Typen ist ebenfalls möglich. Die einzelnen Elemente in der Liste werden als Items bezeichnet.

Jedes Item in der Liste hat einen zugehörigen Index, der seine Position angibt. Der erste Eintrag hat den Index 0, der zweite den Index 1, der dritte den Index 2 und so weitergehend. Das Element an der n-ten Stelle erhält den Index n-1. Mittels des Indexes kann mit unterschiedlichen Methoden auf die Elemente zurückgegriffen werden.
```python
list = ['coffe','vodka','kaluha','ice']
list[2] # --> vodka
list[-1] # --> coffee
list.index('ice') # --> 3

len(list) # --> 4
```
### `range()` and `list()`
Die `range()`-Funktion erzeugt eine Folge von Zahlen, die häufig in Schleifen verwendet wird, um eine bestimmte Anzahl von Iterationen zu steuern.

Beispiel:
```python
for i in range(3, 7):
    print(i)
```
Ausgabe:
```python
3
4
5
6
```

Die `list()`-Funktion wird verwendet, um ein neues Listenobjekt zu erstellen. Sie kann eine iterierbare Eingabe wie eine Range, String, Tuple oder Set in eine Liste umwandeln.

Beispiel:
```python
characters = list("Hallo")
print(characters)
```
Ausgabe:
```python
['H', 'a', 'l', 'l', 'o']
````


### `slice()`
Mittels `slice` können mehrere Elemente einer Liste addressiert werden.
```python
list = ['coffe','vodka','kaluha','ice']
list[1:3] # -->  vodka, kaluha, ice
list[1:] # --> vodka, kaluha, ice
```
### Listen in Listen
Listen können in verschiedenen Listen beinhaltet werden. Die Elemente können weiterhin anhand ihres Indexes abgerufen werden. Der Index muss bei mehreren Listen entsprechend angepasst werden.
```python
list = [['coffee','vodka','kaluha','ice'][7, 8, 23, 69, 420]]
list[1][2] # --> 23
list[0][-1] # --> ice
```
## `Dictionaries`
Dictionaries können ähnlich wie bei Listen, mehrere Elemente speichern sowie weitere Dictonaries. Im Unterschied zu Listen können die Indizes (sogenannte Keys) jedoch nicht nur 'integer' sein, sondern auch andere unveränderliche Datentypen wie 'Strings'. Jeder Key ist mit einem spezifischen Value verknüpft, wodurch ein Dictionary aus Key-Value-Paaren besteht.

Dictionaries werden mit geschweiften Klammern `{}` definiert. Im Gegensatz zu Listen sind sie jedoch nicht geordnet. Stattdessen wird der gespeicherte Wert durch den entsprechenden Key abgerufen. Um festzustellen, ob ein bestimmter Key oder Wert in einem Dictionary enthalten ist, können die Operators `in` und `not in` verwendet werden.

```python
# Erstellen eines Dictionaries
person = {
    "Name": "Matthieu Schaller",
    "Alter": 25,
    "Beruf": "Student",
    "Stadt": "Bern"
}

# Zugriff auf Werte mit Keys
print(person["Name"])  # Gibt "Matthieu Schaller" aus
print(person["Alter"])  # Gibt 26 aus

# Hinzufügen eines neuen Key-Value-Paares
person["Hobby"] = "Fussball"

# Ändern eines Wertes
person["Alter"] = 25  # Das Alter wird von 25 auf 26 geändert

# Löschen eines Key-Value-Paares
del person["Stadt"]

# Überprüfen, ob ein Key im Dictionary vorhanden ist
if "Beruf" in person:
    print("Beruf ist vorhanden:", person["Beruf"])

# Iteration über ein Dictionary
for key, value in person.items():
    print(f"{key}: {value}")

# Zugriff auf alle Keys und Werte
keys = person.keys()   # Gibt alle Keys zurück
values = person.values()  # Gibt alle Values zurück

print("Alle Keys:", keys)
print("Alle Values:", values)

# Überprüfen, ob ein Key existiert
if "Hobby" in person:
    print("Das Hobby ist:", person["Hobby"])
else:
    print("Kein Hobby angegeben.")
```
Ausgabe:
```python
Matthieu Schaller
25
Beruf ist vorhanden: Student
Name: Matthieu Schaller
Alter: 26
Beruf: Student
Hobby: Fussball
Alle Keys: dict_keys(['Name', 'Alter', 'Beruf', 'Hobby'])
Alle Values: dict_values(['Matthieu Schaller', 26, 'Student', 'Fussball'])
Das Hobby ist: Fussball
```
