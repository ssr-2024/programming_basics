# Fehlermeldungen

Python gibt detaillierte Fehlermeldungen aus, die dabei helfen können, Codeprobleme schneller zu erkennen und zu beheben. Im Folgenden werden einige der häufigsten Fehlermeldungen beschrieben, die während der Programmierung in Python auftreten können, sowie Tipps zur Fehlersuche und -behebung.

## Bekannte Fehlermeldungen:

- [NameError](#nameerror)
- [TypeError](#typeerror)
- [IndexError](#indexerror)
- [KeyError](#keyerror)
- [AttributeError](#attributeerror)


## NameError
**Fehlermeldung**: `NameError: name 'a' is not defined`

### Ursache
Ein **NameError** tritt auf, wenn auf eine Variable oder Funktion zugegriffen wird, die im aktuellen Skript nicht definiert ist. Dies passiert häufig, wenn versucht wird, eine Variable oder Funktion zu verwenden, bevor sie initialisiert oder definiert wurde.

### Mögliche Ursachen
- **Variable/Funktion wurde später im Skript definiert**: Die Variable oder Funktion, die verwendet wird, wurde noch nicht initialisiert, sodass Python sie nicht finden kann.
- **Modul oder Funktion fehlt**: Es wurde vergessen, ein Modul oder eine Funktion zu importieren, das bzw. die die Variable oder Funktion definiert.
- **Tippfehler**: Ein simpler Tippfehler kann dazu führen, dass Python eine Variable nicht erkennt, auch wenn sie korrekt definiert wurde.

### Beispiel
Erzeugt Fehlermeldung:
```python
print(my_variable)  # Ausgabe: NameError: name 'my_variable' is not defined
```
Korrekt:

```python
my_variable = 10
print(my_variable)  # Ausgabe: 10
```

## TypeError
**Fehlermeldung**: `TypeError: unsupported operand type(s) for +: 'int' and 'str'`

### Ursache
Ein **TypeError** tritt auf, wenn eine Operation auf inkompatiblen Datentypen ausgeführt wird. Dies passiert häufig, wenn versucht wird, eine Zahl (z.B. `int`) mit einem Text (`str`) zu kombinieren.

### Mögliche Ursachen
- **Inkompatible Datentypen**: Ein arithmetischer oder logischer Operator wurde zwischen zwei nicht kompatiblen Datentypen angewendet.
- **Falsche Argumente**: Eine Funktion oder Methode wurde mit Argumenten falscher Datentypen aufgerufen.
- **Automatische Konvertierung fehlt**: In Python werden Daten nicht automatisch in kompatible Typen konvertiert; dies muss explizit durch den Entwickler geschehen.

### Beispiel
Erzeugt Fehlermeldung:
```python
number = 10
text = "Apples"
print(number + text)  # Ausgabe: TypeError: unsupported operand type(s) for +: 'int' and 'str'
```

Korrekt:
```python
number = 10
text = "Apples"
print(str(number) + " " + text)  # Ausgabe: 10 Apples
```

## IndexError
**Fehlermeldung**: `IndexError: list index out of range`

### Ursache
Ein **IndexError** tritt auf, wenn versucht wird, auf ein Element einer Liste, eines Tupels oder eines anderen sequenziellen Datentyps zuzugreifen, das außerhalb des gültigen Bereichs liegt. Dies passiert, wenn der Index, auf den zugegriffen wird, größer ist als die Anzahl der Elemente in der Sequenz.

### Mögliche Ursachen
- **Falscher Indexwert**: Der Index ist größer oder kleiner als die in der Liste verfügbaren Indizes.
- **Dynamische Änderungen**: Wenn Elemente während des Programmlaufs hinzugefügt oder entfernt werden, kann es zu fehlerhaften Indizes kommen.
- **Unbeabsichtigtes Schleifenende**: Eine Schleife läuft länger als die Sequenz und greift auf nicht vorhandene Indizes zu.

### Beispiel
Erzeugt Fehlermeldung:
```python
fruits = ["Apple", "Banana"]
print(fruits[2])  # Ausgabe: IndexError: list index out of range
```

Korrekt:
```python
fruits = ["Apple", "Banana"]
if len(fruits) > 2:
    print(fruits[2])
else:
    print("Index 2 ist nicht verfügbar")  # Ausgabe: Index 2 ist nicht verfügbar
```

## KeyError
**Fehlermeldung**: `KeyError: 'nonexistent_key'`

### Ursache
Ein **KeyError** tritt auf, wenn versucht wird, auf einen nicht existierenden Schlüssel in einem Dictionary zuzugreifen. Dieser Fehler weist darauf hin, dass der angegebene Schlüssel im Dictionary nicht vorhanden ist.

### Mögliche Ursachen
- **Schlüssel existiert nicht**: Der angegebene Schlüssel ist nicht im Dictionary enthalten.
- **Tippfehler im Schlüssel**: Ein Schreibfehler im Schlüsselnamen kann ebenfalls zu einem KeyError führen.
- **Verwendung falscher Datentypen als Schlüssel**: Wenn der Schlüsseltyp nicht dem erwarteten Typ entspricht, wird der KeyError ausgelöst.

### Beispiel
Erzeugt Fehlermeldung:
```python
my_dict = {"name": "Alice", "age": 30}
print(my_dict["address"])  # Ausgabe: KeyError: 'address'
```
Korrekt:

```python
my_dict = {"name": "Alice", "age": 30}
print(my_dict.get("address", "Schlüssel nicht vorhanden"))  # Ausgabe: Schlüssel nicht vorhanden
```

## AttributeError
**Fehlermeldung**: `AttributeError: 'object' has no attribute 'attribute_name'`

### Ursache
Ein **AttributeError** tritt auf, wenn versucht wird, auf ein Attribut eines Objekts zuzugreifen, das nicht existiert. Dies passiert oft, wenn das Objekt einer Klasse zugewiesen wird, die das angefragte Attribut nicht definiert hat.

### Mögliche Ursachen
- **Falscher Attributname**: Ein Schreibfehler im Namen des Attributs kann zu einem AttributeError führen.
- **Attribut ist nicht definiert**: Das Attribut wurde nicht in der Klasse oder im Objekt definiert.
- **Falsche Objektinstanz**: Es wird auf ein Attribut eines Objekts zugegriffen, das einem anderen Klassentyp angehört, der dieses Attribut nicht besitzt.

### Beispiel
Erzeugt Fehlermeldung:
```python
class Car:
    def __init__(self, color):
        self.color = color

my_car = Car("blue")
print(my_car.speed)  # Ausgabe: AttributeError: 'Car' object has no attribute 'speed'
```

Korrekt:

```python
class Car:
    def __init__(self, color, speed):
        self.color = color
        self.speed = speed

my_car = Car("blue", 120)
print(my_car.speed)  # Ausgabe: 120
```

