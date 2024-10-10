 Dokumentation zu Programming Basics

## Kapitel 1: Python Basics

### Interaktive Python Shell

Es gibt mehrere Varianten, wie man in Visual Studio Code die interkative Shell von Python nutzen kann. Die einfachste (für mich) ist über das Terminal, welches sich über den Reiter "Anzeigen" -> "Terminal" öffnen lässt. Gibt man darin den Befehl "python" ein, wird diese interaktive Shell gestartet. Zu erkennen ist dies and den drei Grösser-als-Zeichen ">>>". Die interaktive Shell kann verwendet werden, um schnell Code, bzw. dessen Ausgabe zu testen.

### Operationen in Python

Operatoren werden in Python verwendet um Berechnungen durchzuführen oder Bedingungen auszuwerten. Sie ermöglichen es uns, mathematische und logische Operationen zu implementieren, und umfassen unter anderem arithmetische, Vergleichs- und logische Operatoren.

Die wichtigsten Operatoren in Python, wie sie Text-Book aufgelistet sind:

| Operator | Operation                        | Beispiel                   | Ergebnis |
|----------|----------------------------------|----------------------------|-----------------|
| **       | Exponentialrechnung              | `2 ** 3`                   | 8               |
| %        | Modulus (Rest nach einer Divison)| `22 % 8`                   | 6               |
| //       | Integer Division                 | `22 // 8`                  | 2               |
| /        | Division                         | `22 / 8`                   | 2.75            |
| *        | Multiplikation                   | `3 * 5`                    | 15              |
| -        | Subtraktion                      | `5 - 2`                    | 3               |
| +        | Addition                         | `2 + 2`                    | 4               |

Bei einer komplizierteren Rechnung, mit mehreren Operatoren verfolgt Python die gleiche Logik wie in der Mathematik: Punkt vor Strich, bzw. Klammern vor Punkt vor Strich. Dazu ein Beispiel:

```py
rechnung1 = 5 + 5 * 5
print(rechnung1)

Output: 30

rechnung2 = (5 + 5) * 5
print(rechnung2)

Output: 50
```

### Datentypen in Python

In Python gibt es mehrere Datentypen, die unterschiedliche Eigenschaften haben. Die wichtigsten, wie sie im Text-Book stehen sind nachstehend wieder zusammengefasst:

| Datentyp                    | Abkürzung | Beispiele                                               |
|-----------------------------|-----------|--------------------------------------------------------|
| Ganzzahlen                  | int       | -2, -1, 0, 1, 2, 3, 4, 5                               |
| Kommazahlen            | float     | -1.25, -1.0, -0.5, 0.0, 0.5, 1.0, 1.25               |
| Zeichenketten (aka. Text)               | str       | 'a', 'aa', 'aaa', 'Hallo!', '11 Katzen'               |

Gerade diese Datentypen sind (am Anfang) immer wieder die Quelle für Fehler. Am Beispiel von vorhin kann das anschaulich dargestellt werden:

```py
beispiel1 = 5 + 5 * 5 
print(beispiel1) # Hier wird normal die Rechnung ausgeführt, weil Python mit Zahlen rechnet

Output: 30

beispiel2 = '5 + 5 * 5' 
print(beispiel2) # Durch das Hinzufügen von Anführungszeichen wird die Variable in Text (String/str) umgewandelt

Output: 5 + 5 * 5
```

Zwei String Variablen können mit dem '+'-Operator problemlos miteinander verbunden werden. Die Datentypen lassen sich jedoch nicht mischen. Dies in einem Beispiel:

```py
beispiel3 = 'Laura' + 'Martin'
print(beispiel3) 

Output: LauraMartin

beispiel4 = 'Laura' + 5 
print(beispiel4) 

Output: Errormeldung

beispiel5 = 'Laura' * 3 
print(beispiel5) 

Output: LauraLauraLaura
```

Um eine Variable in den jeweiligen Datentyp umzuwandeln, kann die Abkürzug des Datentyps verwendet werden:

str(variable)

int(variable)

float(variable)

```py
alter = 29 # Eine Zahl wird standardmässig als Integer in einer Variable gespeichert, diese muss zuerst umgewandelt werden mit str().
print('Ich bin ' + str(alter) + ' Jahre alt.') # Wird der Befehl str() weggelassen, entsteht ein Error.

Output: Ich bin 29 Jahre alt.
```

Dieses Beispiel würde man in Python nie so coden, es veranschaulicht mir aber gut, worum es geht:

```py
alter = int(input("Wie alt bist du? "))
# Mit input wird eine User Eingabe gefordert. Diese wird mit dem vorhergehenden Befehl int() in eine Ganzzahl umgewandelt.
print("Du bist " + str(alter) + " Jahre alt.")
# Somit ist die Variable alter als Ganzzahl gespeichert, dadurch kann sie aber nicht mit Strings kombiniert werden. Damit das möglich ist, wird sie mit dem Befehl str() in einen String umgewandelt.
```

### Kommentare in Python

Wie oben zu sehen ist können Hashtags '#' verwendet werden um Kommentare in Python hinzuzufügen. Weil dieser Teil des Codes dann vom Compiler ignoriert wird, können Hashtags auch verwendet wurden um temporär Zeilen von Code auszukommentieren beim Testen von Ausführungen.

### Variablen in Python

In den vorangingen Beispielen wurden die ganze Zeit schon stillschweigend Variablen verwendet. Variablen werden verwendet, um Daten zu speichern, die später wiederverwendet werden. Variablen sind so intuitiv, dass sie nicht weiter beschrieben werden. Es folgend lediglich ein paar Beispiele: 

```py
name = 'Max'
alter = 22
grösse = 1.87
gewicht = 87
```

### Variablen Namen

Im Text-Boox werden einige Regeln aufgelistet zu Variablen Namen:

1. Variablen Namen dürfen nur ein Wort sein
1. Variablen Namen dürfen nur Buchstaben, Zahlen und Unterstriche enthalten
1. Variablen Namen dürfen nicht mit einer Zahl beginnen

Für meine eigene Klarstellung: mit einem Wort ist gemeint, dass kein Leerschlag dazwischen sein kann. So etwas wie 'jump_height' ist völlig okay, nicht aber 'jump height'.

### Print Funktion

Auch die Print Funktion wurde in einigen Beispielen schon verwendet. Sie wird benutzt, um Ausgaben in der Konsole anzuzeigen. 

### Input Funktion

Mit der Input FUnktion kann eine Eingabe des Benutzers angefordert werden. Diese muss dann mit der Eingabe Taste bestätigt werden. Hier ein Beispiel:


```python
name = input('Wie heisst du?: ') 
print('Schön dich zu sehen, ' + name)

Output: Schön dich zu sehen, Robin # Sofern oben der Name Robin eingegeben wurde ;)
```

### len Funktion

Die len-Funktion in Python wird verwendet, um die Länge (Anzahl der Elemente) eines Objekts zu ermitteln. Sie funktioniert grundsätzlich mit verschiedenen Datentypen, vorläufig mal mit Strings. Auch dazu ein Beispiel: 

```py
text = 'Hallo'
print(len(text))  

Output: 5 # Das Wort "Hallo" entählt also 5 Buchstaben (Elemente).
```
Dieses Beispiel ist sehr trivial, es werden im Verlauf der Dokumentation weitere Beispiele dazu folgen.

## Kapitel 2: Flow Control

Mit Flow Control (auch Kontrollfluss genannt) in Python ist der Ablauf der Ausführung eines Programms gemeint. Sie bestimmt, in welcher Reihenfolge und unter welchen Bedingungen bestimmte Codeabschnitte ausgeführt werden. 

Das Schreiben des Codes und dessen Ausführung ist dabei erst der letzte Teilschritt beim Erarbeiten eines Programms. In einem ersten Schritt wird ein Plan des Programms erstellt, dies geschieht ausserhalb der Programmierumgebung. Dieser Plan wird Flowchart oder zu Deutsch Flussdiagramm genannt. 

Flowcharts werden verwendet, um den Ablauf eines Prozesses oder eines Algorithmus grafisch darzustellen. Sie helfen dabei, komplexe Abläufe verständlich zu visualisieren, indem sie einzelne Schritte und deren Abhängigkeiten in Form von Symbolen und Pfeilen zeigen.

Dazu ein Beispiel aus dem Text-Book:

<img src='./img/flowchart.JPG'>

Einfach ausgedrückt versucht ein Flowchart (auch UML-Diagramm genannt) das Problem zu skizzieren, mit seinen Teilschritten.

### Boolesche Operatoren


Boolesche Operatoren in Python werden verwendet, um logische Ausdrücke zu vergleichen und zu verknüpfen. Sie geben Wahrheitswerte aus, das heisst true oder false, basierend auf deren Bedingungen. Sie helfen, komplexe logische Ausdrücke zu formulieren und steuern den Ablauf von Entscheidungen im Code.

### Vergleichs Operatoren

Vergleichs Operatoren werden, wie der Name schon vermuten lässt, verwendet, um 2 Werte miteinander zu vergleichen. Aus diesem Vergleich entsteht schlussendlich ein Wert: entweder true oder false.

Die Vergleichs Operatoren, wie sie im Text-Book sind:

| Operator | Bedeutung                    |
|----------|------------------------------|
| ==       | Gleich                        |
| !=       | Ungleich                      |
| <        | Kleiner als                   |
| >        | Größer als                    |
| <=       | Kleiner gleich           |
| >=       | Größer gleich            |

Beispiele in Python:

```python
# Beispiel zu Vergleichsoperatoren in Python

a = 10
b = 20

# Gleichheit
print(a == b)  # False

# Ungleichheit
print(a != b)  # True

# Kleiner als
print(a < b)  # True

# Größer als
print(a > b)  # False

# Kleiner oder gleich
print(a <= b)  # True

# Größer oder gleich
print(a >= b)  # False
```

Wichtig festzuhalten ist noch, dass "=" verwendet wird, um einer Variablen einen Wert zuzuweisen und "==" um zwei Werte miteinander zu vergleichen.


### and, or & not

And, or und not sind auch boolesche Operatoren, sie werden verwendet um logische Ausdrücke zu kombinieren. And gibt nur dann true zurück, wenn beide Operanden wahr sind, während or true zurückgibt, wenn mindestens einer der Operanden wahr ist. Not kehr tden Wahrheiswert eines Ausdrucks um, also wird true zu false und umgekehrt.

### Bedingte Anweisungen

Bedingte Anweisungen, auch Kontrollstrukturen genannt, ermöglichen es im Code Entscheidungen zu treffen. Dazu werden unterschiedliche Codeblöcke basierend auf bestimmten Bedingungen ausgeführt. Dazu werden in Python **if, else und elif** verwendet:

**if** prüft eine Bedingung, **elif** (steht für else if) bietet zusätzliche Bedingungen und **else** wird asugeführt, wenn keine der vorherigen Bedingungen zutraf. Dazu wieder Beispiele: 

```python
# Beispiel 1: if-Anweisung
x = 10
if x > 5:
    print("x ist größer als 5")

# Beispiel 2: if-else-Anweisung
y = 3
if y > 5:
    print("y ist größer als 5")
else:
    print("y ist kleiner oder gleich 5")

# Beispiel 3: if-elif-else-Anweisung
z = 7
if z > 10:
    print("z ist größer als 10")
elif z == 7:
    print("z ist genau 7")
else:
    print("z ist kleiner als 10 und nicht 7")
```

### While Schleifen

While Bedingungen oder Schleifen werden in Python verwendet um einen Codeblock solange auszuführen (bzw. zu wiederholen), wie ein Statement wahr, also true ist. Sobald die Bedingung nicht mehr wahr ist, wird die Schleife beendet. Auch hier wieder ein Beispiel, das es viel besser erklärt:


```py
count = 1

while count <= 5:
    print(count)
    count += 1
```
Die Schleife wird beendet, sobald count 6 erreicht hat. 

Das Beispiel aus dem Textbook is ebenfalls sehr anschaulich, und ein bisschen lustig:

```py
name = ''
while name != 'your name':
        print('Please type your name.')
        name = input()
print('Thank you!')
```

Der Codeblock wird solange "please type your name" ausgeben, bis der User wirklich "your name" eingibt. Brilliant.

Mit den Befehlen "break" kann eine While Schleife unterbrochen werden, mit "continue" wird sie weiter ausgeführt, obwohl sie zu einem Ende gekommen ist.

### For Schleifen und die range Funktion

While Schleifen werden ausgeführt solange ihre Bedingung wahr ist. For Schleifen sind ähnlich, hier kann aber festgelegt werden, wie viel mal sie ausgeführt werden sollen. Dies geschieht mit der range funktion:

```py
for i in range(1, 6):
    print(i)
Output: 1, 2, 3, 4, 5
#!!6 ist ausgeschlossen!!
```

In for Schleifen mit range stehen in Klammern immer der Startpunkt, Endpunkt (der aber nicht inklusive ist) und das Intervall. 

Der Befehl range(0, 10, 2) fängt also bei 0 an und geht in 2er Schritten bis 10, wobei 10 aber eben nicht inklusive ist. Die Ausgabe wäre also:
0, 2, 4, 6, 8