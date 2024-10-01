# Variablen
Variablen zeigen auf einen bestimmten Ort im Speicher, an dem verschiedene Werte gespeichert sind.
Durch diese ist es einfacher den Code zu schreiben. Man sollte die Variablen deskriptiv benennen, um die Leserlichkeit des Codes zu vereinfachen. Schlüsselworte wie `for` oder `if` dürfen nicht verwendet werden. Ausserdem dürfen am Anfang keine Zahlen stehen.
<br>
In Python wird eine dynamische variable Typisierung verwendet. Dies bedeutet, dass der Typ einer Variable nicht deklariert werden muss. 
## Variablenzurodnung
Eine Variable kann (in Python) erst als ein Datentyp erstell und dann zu einem anderen Gewechselt werden.
```Python
x = 10    # Zunächst ist x ein Integer
x = "Hallo"  # Jetzt ist x ein String
```
Die Funktion `id()` kann genutzt werden, um die Speicheradresse abzulesen.

### Konventionen
- Konstanten werden immer gross geschrieben.
- 