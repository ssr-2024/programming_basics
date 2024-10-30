
# Sammel-Datentypen in Python

In Python existieren vier Hauptdatentypen zur Gruppierung von Daten:

- **Lists**: geordnete, veränderbare Sequenzen von Elementen
- **Tuples**: geordnete, unveränderbare Sequenzen von Elementen
- **Sets**: ungeordnete Sammlungen einzigartiger Elemente
- **Dictionaries**: Sammlungen von Schlüssel-Wert-Paaren

Für den Anfang betrachten wir nur `Lists` und `Dictionaries`.

## Lists

Listen sind geordnete und veränderbare Sammlungen, die eine beliebige Anzahl an Elementen enthalten können. Sie sind besonders praktisch, um eine sequenzielle Sammlung ähnlicher Elemente zu speichern und darauf zuzugreifen.

### Beispiel einer einfachen Liste

```python
fruits = ["Apple", "Banana", "Cherry"]

# Zugriff auf Elemente über Indizes
print(fruits[0])  # Ausgabe: Apple
```

## `range()` und `list()`

Mit `range()` und `list()` lassen sich Listen von Zahlen in einem bestimmten Bereich erstellen.

### Beispiel: Erstellen einer Liste von Zahlen von 0 bis 9
```python
numbers = list(range(10))
print("Zahlen 0 bis 9:", numbers)  # Ausgabe: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

## `slice()`

Mit `slice()` können Teilbereiche einer Liste ausgewählt werden.

### Beispiel: Zugriff auf Teilbereiche einer Liste
```python
fruits = ["Apple", "Banana", "Cherry", "Date"]
print("Erste drei Früchte:", fruits[:3])  # Ausgabe: ['Apple', 'Banana', 'Cherry']
print("Letztes Element:", fruits[-1])     # Ausgabe: Cherry
```

## Listen in Listen

Listen können auch andere Listen enthalten, um mehrdimensionale Strukturen zu erzeugen.

### Beispiel einer verschachtelten Liste
```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Zugriff auf Elemente der inneren Listen
print("Erstes Element der zweiten Zeile:", matrix[1][0])  # Ausgabe: 4
```

## Dictionaries

Dictionaries sind Sammlungen von Schlüssel-Wert-Paaren. Sie eignen sich hervorragend zur Speicherung von Daten, die durch Schlüssel eindeutig identifiziert werden können.

### Beispiel eines einfachen Dictionarys

```python
person = {
    "name": "Alice",
    "age": 30,
    "city": "Berlin"
}

# Zugriff auf Werte durch Schlüssel
print("Name:", person["name"])  # Ausgabe: Alice
print("Alter:", person["age"])  # Ausgabe: 30
```

### Beispiel zum Hinzufügen und Ändern von Einträgen im Dictionary

```python 
person["age"] = 31  # Ändern des Alters
person["profession"] = "Engineer"  # Hinzufügen eines neuen Schlüssels
print("Aktualisiertes Dictionary:", person)
```

### Beispiel zur Iteration über Schlüssel und Werte

```python 
for key, value in person.items():
    print(f"{key}: {value}")
```