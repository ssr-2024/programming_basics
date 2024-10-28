# Funktionen

In Python sind Funktionen wiederverwendbare Codeblöcke, die eine spezifische Aufgabe ausführen. Funktionen helfen, den Code modular, lesbar und effizient zu gestalten. Sie werden mit dem Schlüsselwort `def` definiert, gefolgt vom Funktionsnamen und optionalen Parametern in Klammern. Funktionen können Werte mit `return` zurückgeben und lassen sich in verschiedenen Programmteilen mehrfach aufrufen.

## Prinzip der Modularität

Modularität bedeutet, den Code in unabhängige und wiederverwendbare Blöcke zu unterteilen, die jeweils eine klar definierte Aufgabe erfüllen.

Funktionen sind ein wichtiges Konzept der Modularität. Sie ermöglichen es, komplexe Programme in kleine, handhabbare Teile zu zerlegen.

So wird der Code strukturierter, leichter lesbar und einfacher zu warten und zu erweitern.

### Beispiel: Begrüssungsfunktion
```python
def greet(name):

    print("Hello, " + name)

#Gibt eine Begrüßung für den angegebenen Namen aus.
```

### Aufruf der Funktion

Hier rufen wir die Funktion `greet` auf und übergeben den Namen "Alice" als Argument.

Die Funktion gibt eine Begrüßung aus.


## Funktionen von Bibliotheken aufrufen

Python bietet viele Standard- und Drittanbieterbibliotheken, die vorgefertigte Funktionen für spezielle Aufgaben enthalten.

Diese Funktionen können importiert und direkt verwendet werden, ohne dass wir sie selbst schreiben müssen.

### Beispiel: Installation und Nutzung der `art`-Bibliothek für ASCII-Kunst

Um eine externe Bibliothek zu verwenden, muss sie zuerst installiert werden. 

### Installation in der Konsole ausführen:

```
pip install art
```

Nachdem die Bibliothek installiert ist, können wir sie importieren und die Funktionen nutzen.

Die `art`-Bibliothek erzeugt ASCII-Art, also Zeichnungen aus Textzeichen.

Die Funktion `text2art` aus der `art`-Bibliothek erzeugt ASCII-Text aus dem übergebenen String.

Dies kann für kreative Projekte wie Terminal-Anwendungen oder dekorativen Text verwendet werden.

### Beispiel für Übung: ASCII-Kunst erstellen mit der `art`-Bibliothek

```python
from art import text2art

# Ausgabe von ASCII-Art
print(text2art("Fun"))

# Output:
  _____
 |  ___| _   _  _ __
 | |_   | | | || '_ \
 |  _|  | |_| || | | |
 |_|     \__,_||_| |_|

```


## Funktionen mit Rückgabewerten

Funktionen können Werte zurückgeben, um Berechnungen oder Ergebnisse an den Aufrufer zurückzugeben. Das `return`-Schlüsselwort beendet die Funktion und gibt einen Wert zurück. Ohne `return` würde die Funktion `None` zurückgeben.

### Beispiel: Addition zweier Zahlen

```python
def add(a, b):

    #Addiert zwei Zahlen und gibt das Ergebnis zurück.

    result = a + b
    return result
```

### Nutzung der Funktion

Hier rufen wir die Funktion `add` auf und übergeben die Werte 5 und 3.

Die Funktion addiert die beiden Zahlen und gibt das Ergebnis zurück, das wir in der Variable `result` speichern.

```python
result = add(5, 3)
print(f"Das Ergebnis der Addition: {result}")  # Ausgabe: 8
```

### Erklärung:
1. Die Funktion `add` hat zwei Parameter: `a` und `b`.

2. Sie addiert `a` und `b` und gibt das Ergebnis mit `return` zurück.

3. Der Wert von `result` wird dann ausgegeben.

## Beispiel: Funktion zur Berechnung des Umfangs eines Kreises

Diese Funktion zeigt die Nutzung einer mathematischen Bibliothek (`math`) zur Berechnung.

Sie berechnet den Umfang eines Kreises für einen gegebenen Radius.

```python
import math

def calculate_circumference(radius):
    """Berechnet den Umfang eines Kreises für den gegebenen Radius."""
    circumference = 2 * math.pi * radius
    return circumference
```

### Aufruf und Ausgabe

Hier verwenden wir die Funktion `calculate_circumference`, um den Umfang eines Kreises mit Radius 5 zu berechnen.

```python
circumference = calculate_circumference(5)
print(f"Der Umfang eines Kreises mit Radius 5 beträgt: {circumference:.2f}")  # Ausgabe: 31.42
```

### Erklärung:
1. Die Funktion verwendet die Konstante `pi` aus der `math`-Bibliothek.

2. Der Umfang eines Kreises wird mit der Formel `2 * pi * radius` berechnet.

3. Die `return`-Anweisung gibt das Ergebnis an den Aufrufer zurück.

4. Der `.2f`-Formatierungscode zeigt das Ergebnis auf zwei Dezimalstellen gerundet an.


## Variablen in Funktionen

Variablen, die innerhalb einer Funktion definiert werden, sind **lokale Variablen**.

Diese existieren nur innerhalb der Funktion und sind außerhalb der Funktion nicht sichtbar oder zugänglich.

```python
def example_function():
    """Beispiel für eine lokale Variable innerhalb einer Funktion."""
    local_variable = 10
    print(f"Lokale Variable innerhalb der Funktion: {local_variable}")
```

### Aufruf der Funktion

Beim Aufruf wird `local_variable` innerhalb der Funktion `example_function` ausgegeben.

```python
example_function()  # Ausgabe: Lokale Variable innerhalb der Funktion: 10
```

### Hinweis:

Die folgende Zeile würde zu einem Fehler führen, da `local_variable` nur innerhalb der Funktion existiert

```python
# print(local_variable)   # NameError: name 'local_variable' is not defined
```

### Erklärung:

1. `local_variable` ist eine lokale Variable, die nur in `example_function` existiert.

2. Der Zugriff auf `local_variable` außerhalb der Funktion würde einen Fehler verursachen, da die Variable dort nicht definiert ist.
