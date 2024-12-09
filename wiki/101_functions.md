# Funktionen
Die Modularität ist ein Konzept in der Softwareentwicklung, das darauf abzielt, Programme in kleinere, überschaubare und wiederverwendbare Teile (Module) zu zerlegen. In Python wird dieses Prinzip durch Funktionen und Module umgesetzt. Mittels der Modularität wird der Code einfacher lesbar und kann wiederverwendet werden. Des weiteren ist die Fehlerfindung in gut dokumentierten Funktionen um einges einfacher und die Modularität ermöglicht eine gleichzeitige Teamarbeit an diversen Modulen.

## Funktionen aufrufen
Funktionen können ganz eifach dann aufgerufen werden wenn sie namentlich genannt werden. Verschiedene Importationen von Funktionen stattfinden. Hier noch einige Beispiele dafür welche Import-Arten von Funktionen möglich sind:
| Syntax | Beschreibung |
|:---------|:-------------|
| `import module`     |    ganzes Modul importieren.           |
| `import module as alias`     |    Modul mit Alias importieren           |
| `from module import func`     |    spezifische Funktion importieren           |
| `from module import func as alias`     |    Funktion mit Alias importieren           |
| `from module import *`     |    alle Inhalte importieren           |
| `importlib.import_module('module')`     |    dynamisches Importieren           |

## Funktionen von Bibliotheken aufrufen
Damit eine Funktion aufgerufen werden kann muss diese vorerst importiert werden. 
Hier noch ein Beispiel für die Importation von `math` :

``` python
import math

# Nutzung einer Funktion aus dem Modul

print(math.sqrt(16))  # Ausgabe: 4.0
```

## Funktionen definieren
Um eigene Funktionen zu erstellen, verwendet man den Ausdruck `def.` Dieser wird an den Anfang des Codeblocks geschrieben, der die Funktion definiert. Direkt danach folgt der Name der Funktion, gefolgt von Klammern, in denen Parameter angegeben werden können (falls nötig). Der zugehörige Funktionscode, der festlegt, was beim Aufruf der Funktion ausgeführt wird, beginnt in der nächsten Zeile und muss **eingerückt** sein. Alle eingerückten Zeilen gehören zur Funktion, bis eine nicht mehr eingerückte Zeile erscheint.

Im folgenden Beispiel wird mit `def` eine Funktion namens hello definiert. Diese Funktion gibt eine Begrüßung so oft aus, wie es der übergebene Parameter beim Aufruf der Funktion angibt. Im gezeigten Fall passiert dies dreimal. Wichtig zu beachten: Die Funktion wird erst beim Aufruf ausgeführt, nicht bei ihrer Definition.
```python
def hello(parameter):
    print("Howdy!" * parameter)
    print("Howdy Cowboy!" * parameter)
    print("Hello there General Kenobi!" * parameter)

hello(3)
```

### `return`
Wenn das Ergebnis einer Funktion für weitere Berechnungen oder Verarbeitungen benötigt wird, sollte es innerhalb der Funktion mit dem Schlüsselwort return zurückgegeben werden.
Wichtig: Lokale Variablen existieren nur während der Ausführung der Funktion und werden danach automatisch gelöscht!
### Beispiel
```python
def quadrat(x):
    # Berechnung des Quadrats
    ergebnis = x ** 2
    # Rückgabe des Ergebnisses
    return ergebnis

# Die Funktion wird aufgerufen und der Rückgabewert in einer Variable gespeichert
zahl = 5
resultat = quadrat(zahl)

# Ausgabe des Ergebnisses
print(f"Das Quadrat von {zahl} ist {resultat}.")
```
## Variablen in Funktionen
Bei Variablen in Funktionen handelt es sich um einen wichtigen Bestandteil von Python-Programmen. Sie beeinflussen, wie Daten innerhalb einer Funktion verarbeitet werden und wie sie sich außerhalb der Funktion verhalten.
Die Variablen in den Funktionen können lokal sowie global gespeichert werden, heisst, Variablen, die innerhalb einer Funktion definiert werden, sind lokal und existieren nur während der Ausführung der Funktion. Variablen, die außerhalb aller Funktionen definiert sind, sind global und können in der gesamten Datei verwendet werden.

#### Lokales Speichern
```python
def berechne_summe(a, b):
    ergebnis = a + b  # 'ergebnis' ist eine lokale Variable
    return ergebnis

print(berechne_summe(3, 5))  # Ausgabe: 8
# print(ergebnis)  # Fehler! 'ergebnis' ist außerhalb der Funktion nicht definiert.
```

##### Globales Speichern
```python
zahl = 10  # Globale Variable

def multiplizieren(faktor):
    global zahl  # Zugriff auf die globale Variable
    zahl = zahl * faktor  # Wert der globalen Variable wird verändert

multiplizieren(3)
print(zahl)  # Ausgabe: 30
```