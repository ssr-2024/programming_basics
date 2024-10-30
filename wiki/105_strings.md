# Strings in Python

In Python sind Strings Zeichenfolgen, die häufig zur Darstellung und Manipulation von Text verwendet werden. Python bietet viele eingebaute Methoden zur Bearbeitung und Formatierung von Strings.

## Groß- und Kleinschreibung ändern

Python stellt mehrere Methoden zur Verfügung, um die Groß- und Kleinschreibung eines Strings zu verändern.

### Beispiele

#### 1. `upper()`
Konvertiert alle Buchstaben zu Großbuchstaben.

```python
text = "Hello World"
print(text.upper())  # Ausgabe: "HELLO WORLD"
```

### 2. lower()
Konvertiert alle Buchstaben zu Kleinbuchstaben.


```python
print(text.lower())  # Ausgabe: "hello world"
```

### 3. title()
Setzt den ersten Buchstaben jedes Wortes auf Großbuchstaben.

```python

print(text.title())  # Ausgabe: "Hello World"
```

### 4. capitalize()
Setzt nur den ersten Buchstaben des gesamten Strings auf Großbuchstaben.

```python
print(text.capitalize())  # Ausgabe: "Hello world"
```

## Formatierte Ausgabe

F-Strings sind eine einfache Möglichkeit, Variablen und Ausdrücke in Strings einzubetten. Sie wurden in Python 3.6 eingeführt und bieten eine kompakte und lesbare Syntax.

### Syntax
Die Syntax für einen F-String sieht wie folgt aus: 

```python
f"Text {Variable oder Ausdruck}"
```


### Beispiel für einen F-String

```python
print(f"Name: {name}, Alter: {age}")  # Ausgabe: "Name: Alice, Alter: 30"
```

### F-Strings unterstützen auch Ausdrücke direkt im String

``` python
print(f"2 * 2 = {2 * 2}")  # Ausgabe: "2 * 2 = 4"
```

## Beispiele für fortgeschrittene Manipulation

Verschiedene Methoden zur String-Manipulation und Formatierung:

### 1. `strip()` entfernt Leerzeichen am Anfang und Ende des Strings

```python
text_with_spaces = "   Hello World   "
print(text_with_spaces.strip())  # Ausgabe: "Hello World"
```

### 2. `replace()` ersetzt bestimmte Teile des Strings

```python
print(text.replace("World", "Python"))  # Ausgabe: "Hello Python"
```

### 3. `split()` teilt den String in eine Liste von Wörtern

```python
print(text.split())  # Ausgabe: ["Hello", "World"]
```

### 4. `join()` fügt eine Liste von Strings zu einem einzelnen String zusammen

```python
words = ["Python", "is", "fun"]
print(" ".join(words))  # Ausgabe: "Python is fun"
```

### 5. String-Länge mit `len()`

```python
print(f"Länge des Textes '{text}': {len(text)}")  # Ausgabe: Länge des Textes 'Hello World': 11
```

### 6. Mehrzeiliger String mit dreifachen Anführungszeichen

```python
long_text = """Das ist ein
mehrzeiliger String,
der über mehrere Zeilen geht."""
print(long_text)
```
