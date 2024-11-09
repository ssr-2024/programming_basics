# Strings
`Strings` sind Zeichenketten, die aus einer Sequenz von Zeichen bestehen. In Python werden Strings in Anführungszeichen gesetzt, entweder in einfachen (`'`), doppelten (`"`), oder dreifachen Anführungszeichen (`'''` oder `"""`). Strings sind unveränderlich, was bedeutet, dass der Inhalt eines Strings nach seiner Erstellung nicht geändert werden kann.

## Gross- Kleinschreibung
Python bietet mehrere Methoden, um die Groß- und Kleinschreibung von Strings zu ändern. Einige der häufig verwendeten Methoden sind:

- `str.upper()`: Wandelt alle Zeichen des Strings in Großbuchstaben um.
- `str.lower()`: Wandelt alle Zeichen des Strings in Kleinbuchstaben um.
- `str.capitalize()`: Wandelt das erste Zeichen des Strings in einen Großbuchstaben um und alle anderen Zeichen in Kleinbuchstaben.
- `str.title()`: Wandelt den ersten Buchstaben jedes Wortes in Großbuchstaben um.

Beispiel:
```python
text = "hello world"
print(text.upper())       # Ausgabe: HELLO WORLD
print(text.lower())       # Ausgabe: hello world
print(text.capitalize())  # Ausgabe: Hello world
print(text.title())       # Ausgabe: Hello World
```
## Formatierte Ausgabe `f'2 * 2 = {2 * 2}'`
Manchmal möchte man variablen in einem String ausgeben. Beispielsweise möchte man ein Alter abfragen und anschliessend in der Kommandozeile das Geburtsjahr ausgeben.
```Python
age = int(input("Wie alt bis du"))
print(f"Du bist (wahrscheinlich) im Jahre {2024-age} geboren.")
```

## Beispiele
### Verkettung von Strings
Strings können mit dem +-Operator verkettet werden.
```Python
greeting = "Hallo"
name = "Bob"
message = greeting + ", " + name + "!"
```

### Multiline-Strings
Multiline-Strings können mit dreifachen Anführungszeichen erstellt werden.
```Python
multiline_text = """Dies ist ein
mehrzeiliger
String."""
```

### Zugriff auf Zeichen
Sie können auf einzelne Zeichen in einem String mit Indexierung zugreifen.
```Python
text = "Python"
print(text[0])  # Ausgabe: P
print(text[-1]) # Ausgabe: n
```

### Länge eines Strings
Die Länge eines Strings kann mit der len()-Funktion ermittelt werden.
```Python
text = "Python"
print(len(text))  # Ausgabe: 6
```
