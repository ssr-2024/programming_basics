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

## Kapitel 3: Funktionen

In Python gibt es neben den Basic Funktionen wie print(),input() oder len(). In Python sind Funktionen wiederverwendbare Codeblöcke, die eine bestimmte Aufgabe ausführen. Funktionen helfen, den Code übersichtlicher zu gestalten und wiederholte Abläufe zu vermeiden.
Funktionen werden in Python immer mit dem Schlüsselwort ***def** definiert. 

Es folgt wieder ein einfaches Beispiel einer Funktion:

```py
def addiere(a, b):
    return a + b

ergebnis = addiere(3, 5)
print(ergebnis)

Output: 8
```
### Scope


In Python bezieht sich der Scope (Gültigkeitsbereich) auf den Bereich des Codes, in dem eine Variable zugänglich ist. Es gibt zwei Hauptarten von Scope:

1. Local Scope:
- Variablen, die innerhalb einer Funktion definiert werden, befinden sich im local scope.
- Sie sind nur innerhalb der Funktion verfügbar und können außerhalb der Funktion nicht verwendet werden.

```py
def meine_funktion():
    x = 10  # lokale Variable
    print(x)

meine_funktion()
# print(x) würde hier einen Fehler auslösen, weil x außerhalb der Funktion nicht existiert
```

2. Global Scope:
- Variablen, die außerhalb aller Funktionen definiert werden, befinden sich im global scope.
- Sie sind überall im Programm zugänglich, auch innerhalb von Funktionen (außer wenn sie dort überschrieben werden).

```py
x = 10  # globale Variable

def meine_funktion():
    print(x)  # kann auf die globale Variable zugreifen

meine_funktion()  # Ausgabe: 10
print(x)  # Ausgabe: 10
```

**Unterschied:**

- Lokale Variablen existieren nur innerhalb der Funktion, in der sie definiert wurden.
- Globale Variablen können überall im Code verwendet werden, es sei denn, sie werden innerhalb einer Funktion überschrieben.


### Exception Handling

Im Text-Book wird in einem kurzen Abschnitt ein wichtiger Aspekt aufgegriffen: Exception Handling, zu Deutsch: Behandlung von Ausnahmen. Das Beispiel und die Erklärungen in Text-Book sind so gut, dass ich sie hier übernehmen werde.

Im folgenden Python Programm wird an einer Stelle durch 0 dividiert, was zu einem Error führt:

```py
def spam(divideBy):
    return 42 / divideBy
# hier wird eine Funktion "spam" definiert und ihr der Parameter "divideBy" zugeschrieben. Mit den print Befehlen unten wird für divideBy eine Zahl eingesetzt.

print(spam(2))
print(spam(12))
print(spam(0))
print(spam(1))

```

Folgender Ouput wird erzeugt in Python:

```py 
21.0
3.5
Traceback (most recent call last):
  File "C:/zeroDivide.py", line 6, in <module>
    print(spam(0))
  File "C:/zeroDivide.py", line 2, in spam
    return 42 / divideBy
ZeroDivisionError: division by zero
# das return statmement in spam(0) verursacht einen Error. 
```

Solche Fehlermeldungen kann man mit **try** und **except** statements in den Griff bekommen. Man schreibt dazu den Code um, wie folgt:

```py
def spam(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        print('Error: Invalid argument.') # damit wird eine 'costum' fehlermeldung herausgegeben, ohne dass das programm crashed und nicht weiterläuft.

print(spam(2))
print(spam(12))
print(spam(0))
print(spam(1))
```

Damit sieht der Ouput so aus:

```py
21.0
3.5
Error: Invalid argument.
None
42.0
```

## Kapitel 4: Listen

Eine Liste in Python ist eine geordnete Sammlung von Elementen, die unter einem gemeinsamen Namen gespeichert werden. Diese Elemente können verschiedene Datentypen haben, wie Zahlen, Zeichenketten oder sogar andere Listen. Listen sind veränderbar, das heisst wir können sie nachträglich ändern, beispielsweise Elemente hinzufügen, entfernen oder ändern.

### Merkmale von Listen in Python:

- Listen werden mit eckigen Klammern erstellt: []
- Die Werte innerhalb einer Liste werden Items oder Elemente genannt
- Sie können beliebige Datentypen enthalten: [1, "Hallo", True]
- Elemente in einer Liste sind indiziert. Der erste Index ist 0.
- Listen sind veränderbar, d. h. du kannst Elemente ändern, hinzufügen oder entfernen.

Dazu wieder ein Beispiel:

```py
# Eine einfache Liste
meine_liste = [1, 2, 3, "Hallo", True]

# mit dem Befehl print(Name der Liste[Nummer des Elements]) kann dieses Element ausgegeben werden.
print(meine_liste[3])  
Output: Hallo

# Mit dem Befehl .append können Items/Elemente hinzugefügt werden
meine_liste.append("Welt")
```

Um individuelle Werte aus der Liste zu erhalten, werden eckige Klammern verwendet nach folgendem Schema:

```py
NameDerListe[Wert] #Werte beginnen immer bei 0!
```
Eine Liste kann auch mehrere kleinere Listen enthalten. Der Umgang damit geschieht wie folgt:

```py
spam = [['cat', 'bat'], [10, 20, 30, 40, 50]]
# Der erste Index spricht die entsprechende Liste an und der Zweite Index das darin enthaltene Element. Wenn ich also 30 als Ausgabe erhalten will muss ich folgende Eingabe tätigen:
spam[0,2]
```
### Negative Indexe

Mit negativen Indexen können ebenfalls Elemente aus einer Liste abgerufen werden. Mit dem Wert -1 wird das letzte Element der Liste abgerufen, mit -2 das zweitletzte usw.

### Slices

Mit Slices (zu Deutsch Scheiben) können mehrere Elemente aus einer Liste gleichzeitig abgerufen werden. Dazu wird zwischen den Elementen ein Doppelpunkt gesetzt:

```py
meine_liste = ['Hund', 'Katze', 'Maus', 'Fuchs', 'Hirsch']

print(meine_liste[1:3])

Output: ['Katze', 'Maus']
# Mit der Ausgabe werden die Elemente 1 (also 'Katze') und 2 (also 'Maus')
```

### Elemente hinzufügen

In einer Liste können Elemente auch hinzugefügt werden. Einerseits wie angesprochen mit dem Befehl '.append', dann wird das Element am Ende der Liste hinzugefügt. Alternativ gibt es auch diese Variante:

```py
meine_liste = ['Hund', 'Katze', 'Maus', 'Fuchs', 'Hirsch']

meine_liste[1]='Hamster'
#Mit diesem Befehl wird das erste Element in der Liste ersetzt durch 'Hamster'.
print(meine_liste)

Output: ['Hund', 'Hamster', 'Maus', 'Fuchs', 'Hirsch']
```

### Elemente löschen

So wie Elemente hinzugefügt werden können, können auch Elemente aus einer Liste gelöscht werden. Dies geschieht mit dem Befehl 'del'.

```py
meine_liste = ['Hund', 'Katze', 'Maus', 'Fuchs', 'Hirsch']

del meine_liste[3]

print(meine_liste)

Output: ['Hund', 'Katze', 'Maus', 'Hirsch']
```

### in und not Operatoren für Listen

Mit den Befehlen 'in' und 'not' kann geprüft werden, ob sich ein Element in der Liste befindet:

```py 
'howdy' in ['hello', 'hi', 'howdy', 'heyas']
True

spam = ['hello', 'hi', 'howdy', 'heyas']
'cat' in spam
False
```
### Einige nützliche Tricks beim Arbeiten mit Listen

Im Text-Book wir eine Reihe an nützlichen Tricks aufgeführt beim Arbeiten mit Listen. Diese möchte ich hier zum Nachschlagen festhalten:

#### Der multiple Assignment Trick

Mit diesem Trick können mehrere Variablen gleichzeitig den Werten in einer Liste hinzugefügt werden:

Anstatt diese Zeilen zu schreiben: 
```py
cat = ['fat', 'orange', 'loud']
size = cat[0]
color = cat[1]
disposition = cat[2]
```
Kann direkt folgende Variante gewählt werden:

```py
cat = ['fat', 'orange', 'loud']
size, color, disposition = cat
```
Dazu müssen jedoch die Anzahl Variablen und Werte in der Liste übereinstimmen, ansonsten entsteht ein Fehlercode in Python. 

#### Augmented Assignment Operators

Augmented Assignment Operators in Python sind spezielle Operatoren, die eine Kombination aus einer mathematischen Operation und einer Zuweisung darstellen. Sie werden verwendet, um den Wert einer Variablen zu ändern und gleichzeitig das Ergebnis der Operation zurück in die gleiche Variable zu speichern. Dies ist eine kompakte Schreibweise, die sowohl den Code kürzer als auch lesbarer macht.

Hier sind einige gängige Beispiele für solche Operatoren:

- `+=` (Addition und Zuweisung): `x += 5` ist gleichbedeutend mit `x = x + 5`
- `-=` (Subtraktion und Zuweisung): `x -= 3` ist gleichbedeutend mit `x = x - 3`
- `*=` (Multiplikation und Zuweisung): `x *= 2` ist gleichbedeutend mit `x = x * 2`
- `/=` (Division und Zuweisung): `x /= 4` ist gleichbedeutend mit `x = x / 4`
- `%=` (Modulo und Zuweisung): `x %= 7` ist gleichbedeutend mit `x = x % 7`


### Die `index()`-Methode

Die `index()`-Methode wird verwendet, um den Index des ersten Vorkommens eines bestimmten Elements in einer Liste zu finden. Wenn das Element nicht gefunden wird, löst sie einen `ValueError` aus.

Ein Beispiel in Python: 

```py
fruits = ['Apfel', 'Banane', 'Kirsche', 'Banane']
index_banane = fruits.index('Banane')

print(index_banane)  
Output: 1
```

### Die `append()`- und `insert()`-Methode

Mit den Befehlen `append()` und `insert()` können Elemente einer Liste hinzugefügt werden. 

Mit `append()` wird das Element am Ende der Liste angehängt:

```py
fruits = ['Apfel', 'Banane', 'Kirsche']
fruits.append('Orange')

print(fruits)
Output: ['Apfel', 'Banane', 'Kirsche', 'Orange']
```

Mit `insert()` kann das Elemenent an einer bestimmten Position eingefügt werden:

```py
fruits = ['Apfel', 'Banane', 'Kirsche']
fruits.insert(1, 'Orange')

print(fruits)  
Output: ['Apfel', 'Orange', 'Banane', 'Kirsche']
```

### Der `remove()`-Methode

Mit dem `remove()`-Befehl können Elemente aus einer Liste gelöscht werden:

```py
fruits = ['Apfel', 'Banane', 'Kirsche', 'Banane']
fruits.remove('Banane')

print(fruits) 
Output: ['Apfel', 'Kirsche', 'Banane']
```

### Listen-ähnliche Typen: Strings und Tupel

Listen sind nicht die einzigen Datentypen, die geordnete Sequenzen von Werten darstellen. Zum Beispiel sind Strings und Listen ähnlich, wenn man einen String als "Liste" einzelner Textzeichen betrachtet. Viele Dinge, die man mit Listen machen kann, funktionieren auch mit Strings: Indexierung, Slicing, for-Schleifen, `len()`, sowie die Operatoren `in` und `not in`.

Beispiele:

```python
name = 'Zophie'
print(name[0])      # Ausgabe: 'Z'
print(name[-2])     # Ausgabe: 'i'
print(name[0:4])    # Ausgabe: 'Zoph'
print('Zo' in name) # Ausgabe: True
```

### Veränderbare und unveränderbare Datentypen

Listen sind veränderbar (mutable), das heisst, wir können ihre Werte verändern, Werte hinzugefügen oder entfernen. Im Gegensatz dazu sind Strings unveränderbar (immutable), das bedeutet, man kann ihren Inhalt nicht ändern.

```py
name = 'Zophie a cat'
name[7] = 'the'  
Output ist ein Fehler: TypeError
```
Um einen String zu verändern, erstellt man einen neuen String durch Verkettung und Slicing. Dies gezeigt an einem Beispiel:

```py
name = 'Zophie a cat'
new_name = name[0:7] + 'the' + name[8:12]

print(new_name)
Ouput: 'Zophie the cat'
```

### Tupel
Tupel funktionieren nach dem gleichen Prinzip wie Listen, sie sind jedoch unveränderbar. Sie werden mit runden Klammern () statt eckigen Klammern [] definiert:

```py 
eggs = ('hello', 42, 0.5)

print(eggs[0])
Output: 'hello'

print(eggs[1:3])   
Output: (42, 0.5)
```

## Kapitel 5: Dictionaries und Datenstrukturierung


`Dictionaries` sind ähnlich wie Listen eine Samllung von Werten. Im Gegensatz zu den Indizes für Listen können die indizes für Dictionaries viele verschiedene Datentypen verwenden, nicht nur ganze Zahlen. In Dictionaries werden dafür sogennannte **Schlüssel** / **keys** verwendet, diesme Schlüssel wird ein Wert zugeordnet. Dadurch ensteht ein Schlüssel-Wert-Paar.

### Eigenschaften von Dictionaries:
- **Unveränderliche Schlüssel**: Die Schlüssel in einem Dictionary müssen unveränderlich sein (z.B. Strings, Zahlen, Tupel). Listen können nicht als Schlüssel verwendet werden.
- **Veränderliche Werte**: Die Werte eines Dictionaries können beliebig veränderlich sein, d.h. sie können Listen, andere Dictionaries, Strings oder beliebige Objekte sein.
- **Ungeordnete Struktur**: Dictionaries sind ungeordnet, was bedeutet, dass die Reihenfolge der Einträge nicht garantiert ist.

### Erstellung eines Dictionaries:
Ein Dictionary wird mit geschweiften Klammern `{}` erstellt, wobei die Schlüssel und Werte durch Doppelpunkte getrennt und die Paare durch Kommata getrennt werden:

```python
person = {
    "Name": "Robert",
    "Alter": 32,
    "Beruf": "Architekt"
}
```

Im Text-Book wird ein sehr anschauliches Beispiel beschrieben, mit dem man sich das Geburtsdatum von Freunden merken kann. Dieses möchte ich hier gerne festhalten:

```py
birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}
# Dies ist ein Dictionary, welches den jeweiligen Namen (Schlüssel) mit Geburtstagen (Werten) verknüpft.

while True:
    print('Enter a name: (blank to quit)')
    name = input()
    if name == '':
        break
    # Es wird eine Endlosschleife kreiert, die den Benutzer nach einem Namen fragt.
    # Wenn der Benutzer einen leeren String eingibt, wird die Schleife beendet.

    if name in birthdays:
        # Überprüft, ob der eingegebene Name bereits im Dictionary `birthdays` vorhanden ist.

        print(birthdays[name] + ' is the birthday of ' + name)
        # Wenn der Name gefunden wird, wird der entsprechende Geburtstag aus dem Dictionary abgerufen und ausgegeben.
    else:
        print('I do not have birthday information for ' + name)
        print('What is their birthday?')
        bday = input()
        # Wenn der Name nicht im Dictionary ist, wird der Benutzer nach dem Geburtstag der Person gefragt.
    
        birthdays[name] = bday
        # Der neue Name und der zugehörige Geburtstag werden dem Dictionary hinzugefügt.

        print('Birthday database updated.')
        # Eine Bestätigungs-Nachricht, dass der Dictionary aktualisiert wurde.
```

### Die Methoden keys(), values() und items()

Es gibt die Möglichkeit sich die Schlüssel, Werte und Schlüssel und Werte eines Dictionaries ausgeben zu lassen. Dazu werden die Befehle `keys()`, `values()` und `items()`verwendet. Die von diesen Methoden zurückgegebenen Werte werden in einer Art Liste aufgeführt, es handelt sich dabei jedoch um keine echten Listen: Sie können nicht verändert werden und besitzen keine `append()`-Methode. Diese Datentypen (**dict_keys**, **dict_values** und **dict_items**) können jedoch in `for`-Schleifen verwendet werden. Dies zeigt sich am Besten an Beispielen:

```python
spam = {'color': 'red', 'age': 42}

for v in spam.values():
        print(v)
Output: 
red
42


for k in spam.keys():
        print(k)
Output:
color
age

for i in spam.items():
        print(i)
Output:
('color', 'red')
('age', 42)
```

Um eine richtige Liste zu erhalten, müssen die Werte in eine Liste umgewandelt werden:

```py
spam = {'color': 'red', 'age': 42}
spam.keys()
# Die Methode 'keys()' gibt alle Schlüssel des Dictionaries 'spam' zurück.Allerdings gibt sie kein echtes Listenobjekt zurück, sondern ein 'dict_keys'-Objekt, das ähnlich wie eine Liste verwendet werden kann, z.B. in Schleifen.

# Zwischenzeitliche Ausgabe wäre:
# dict_keys(['color', 'age'])
# Dies zeigt, dass das 'dict_keys'-Objekt die beiden Schlüssel 'color' und 'age' enthält.

>>> list(spam.keys())
# Der Befehl 'list()' wird verwendet, um das 'dict_keys'-Objekt in eine echte Liste umzuwandeln.

Output:
['color', 'age']
# Das Ergebnis ist eine echte Liste, die nur die Schlüssel des Dictionaries enthält.
```

### Überprüfung der Inhalte eines Dictionaries

Mit den `in`und `not`Operatoren kann überprüft werden, ob ein Key oder ein Wert in einem Dictionary existiert. Dazu können beispielsweise folgende Abfragen in der interaktiven Shell in Visual Studio Code gemacht werden:

```py
>>> test = {'Ort': 'Bern', 'Quartier': 'Breitenrain'}
>>> 'Quartier' in test.keys()
True

>>> 'Bern' in test.values()
True

>>> 'Land' in test.keys()
False
```

### Die `get()`-Methode

Mit der `get()`-Methode können direkt der Schlüssel und der Wert aus einem Dictionary gezogen werden. Ausserdem kann ein Ausweichswert angegeben werden, falls der Key nicht existiert.

```py
>>> officeSupplies = {'pens': 10, 'notebooks': 3}
>>> 'I have ' + str(officeSupplies.get('notebooks', 0)) + ' notebooks.'
# 0 ist der Ausweichswert, der ausgegeben wird, wenn der Key 'notebooks' nicht im Dictionary sein sollte.
'I have 3 notebooks.'

>>> 'I have ' + str(officeSupplies.get('markers', 0)) + ' markers.'
# Hier wird der Ausweichswert 0 ausgegeben, weil 'markers' nicht im Dictionary vorkommt.
'I have 0 markers.'
```

### Die `setdefault()`-Methode 

Mit der `setdefault()`-Methode kann einem Key einen Wert zugewiesen werden, aber nur wenn dieser nicht schon einen Wert besitzt. Dies ist wiederum am besten an einem Beispiel erklärt:

```py
>>> person = {'name': 'Anna', 'age': 30}
>>> person.setdefault('city', 'Bern')
# Weil der Key 'city' im Dictionary noch nicht exisiert, wird er hinzugefügt und ihm der Wert 'Bern' zugewiesen.
>>> person

{'city': 'Bern', 'age': 30, 'name': 'Anna'}
# Dem Dictionary wurde der Key 'city' mit dem Wert 'Bern hinzugefügt.

>>> person.setdefault('city', 'Zurich')
# Wird jetzt versucht auf die gleiche Art dem Dictionary nochmals 'city' hinzuzufügen und der Wert 'Zurich', passiert aber nichts. Der Wert von 'city' wird auch nicht geändert. Wenn der Key schon exisitiert, hat die setdefault-Methode keinen Effekt. 

>>> person
{'city': 'Bern', 'age': 30, 'name': 'Anna'}
```

Im Text-Book wird wieder ein sehr anschauliches Beispiel beschrieben, welches ich hier gerne zum Nachschlagen festhalten möchte:

Die `setdefault()`-Methode ist eine praktische Abkürzung, um sicherzustellen, dass ein Schlüssel existiert. Hier ist ein kurzes Programm, das die Anzahl der Vorkommen jedes Buchstabens in einem String zählt:

```python
message = 'Es war ein heller kalter Tag im April, und die Uhren schlugen dreizehn.'
# Nachricht, deren Buchstaben gezählt werden sollen

count = {}
# Dictionary, das die Zählungen der Buchstaben speichert

for character in message:
    # Diese Schelife speichert die Zählung der Buchstaben und stellt sicher, dass der Buchstabe im Dictionary existiert, mit einem Standardwert von 0
    count.setdefault(character, 0)
    
    count[character] = count[character] + 1
    # Erhöht den Zähler für diesen Buchstaben um 1

print(count)
# Gibt die Zählungen aller Buchstaben aus

Output:
{' ': 13, ',': 1, '.': 1, 'A': 1, 'I': 1, 'a': 4, 'c': 3, 'b': 1, 'e': 5, 'd': 3, 'g': 2, 'i': 6, 'h': 3, 'k': 2, 'l': 3, 'o': 2, 'n': 4, 'p': 1, 's': 3, 'r': 5, 't': 6, 'w': 2, 'y': 1}
```

Der Output zeigt an, wie viel mal jeder Buchstabe in der Nachricht vorkommt: Leerschlag 13 Mal, 'A' 1 Mal usw.

Im Text-Book wurde ausserdem ein Beispiel gemacht für ein Tic-Tac-Toe Board, anhand von dem Datenstrukturen zur Repräsentation von Dingen im echten Leben erklärt wurden. Dieses Beispiel wird im Rahmen der Dokumentatin ausgelassen.

### Verschachtelte Dictionaries und Listen

Das Beispield es Tic-Tac-Toe Boards geht in die Richtung von verschachtelten Dictionaries und Listen. Um für kompliziertere Dinge ein Modell zu erstellen, wird es nötig sein Listen und Dictionaries innerhalb von anderen Listen und Dictionaries zu erstellen.Listen sind nützlich, um eine geordnete Reihe von Werten zu enthalten, und Wörterbücher sind nützlich, um Schlüssel mit Werten zu verknüpfen. Dieses Thema wird im Text-Book wieder anhand eines Beispiels erklärt. Im Beispiel geht es um ein Picknick und wer was dazu mitbringt. 

Die Funtkion `totalBrought()`kann diese Datenstruktur lesen und die Gesamtzahl der von allen Gästen mitgebrachten Gegenstände berechnen:

```py
allGuests = {'Alice': {'apples': 5, 'pretzels': 12},
             'Bob': {'ham sandwiches': 3, 'apples': 2},
             'Carol': {'cups': 3, 'apple pies': 1}}
# Hier sind Dictionaries innerhalb von anderen Dictionaries, die die jeweiligen Dinge beinhalten, die die Personen zum Picknick bringen.              

# Funktion, die die Gesamtanzahl eines bestimmten Items über alle Gäste hinweg berechnet
def totalBrought(guests, item):
    numBrought = 0
    # Schleife durch jeden Gast (k) und ihre mitgebrachten Items (v)
    for k, v in guests.items():
        # Addiere die Anzahl des gesuchten Items, falls es existiert, andernfalls 0
        numBrought = numBrought + v.get(item, 0)
    return numBrought

# Ausgabe der Gesamtanzahl der mitgebrachten Items für jedes Item
print('Number of things being brought:')
print(' - Apples         ' + str(totalBrought(allGuests, 'apples')))
print(' - Cups           ' + str(totalBrought(allGuests, 'cups')))
print(' - Cakes          ' + str(totalBrought(allGuests, 'cakes')))
print(' - Ham Sandwiches ' + str(totalBrought(allGuests, 'ham sandwiches')))
print(' - Apple Pies     ' + str(totalBrought(allGuests, 'apple pies')))

Output:
Number of things being brought:
- Apples 7
- Cups 3
- Cakes 0
- Ham Sandwiches 3
- Apple Pies 1
```

## Kapitel 6: Arbeiten mit Strings

Text (und damit Strings) ist einer der am häufigsten verwendeten Datentypen in Python. Deshalb ist der korrekte Umgang damit essenziell. 

Strings können grundsätzlich mit einfachen Anführungszeichen `'Beispieltext'` geschrieben werden. Dadurch können aber einige Probleme auftreten. Tritt in einem Textabschnitt nämlich ein solches Anführungszeichen auf, dann führt das zu Problemen in Python.

```py
print('Das ist Tim's Hut')
#Hier wird nur der Text "Das ist Tim" ausgegeben, die 3 einfachen Anführungszeichen verursachen ein Problem in Python.
```

Zum Glück gibt es mehrere Varianten wie Strings geschrieben werden können:
- mit einem Anführungszeichen `'Beispieltext1'`
- mit doppelten Anführungszeichen `"Beispieltext2"`
- Mehrezeilige Strings mit dreifachen Anführungszeichen `'''Beispieltext3'''/"""Beispieltext3"""`

### Escape characters

Ausserdem können mit sogenannten Escape characters Zeichen verwendet werden, die sonst nicht in Strings verwendet werden können. Dazu wird ein Backslash `\` benutzt.
Das Beispiel von vorhin kann also so gelöst werden:

```py
print('Das ist Tim\'s Hut')
# Dadurch stimmt der Ouput: Das ist Tim's Hut.
```
Escape-Sequenzen wie \' und \" ermöglichen es, Anführungszeichen innerhalb von Strings zu verwenden, ohne die String-Begrenzung zu stören.
Dazu gibt es eine Reihe von verschiedenen Escape characters, die nützlich sind:

| Escape-Sequenz   | Wird dargestellt als |
|------------------|----------------------|
| \'               | Einfaches Anführungszeichen |
| \"               | Doppelte Anführungszeichen |
| \t               | Tabulator             |
| \n               | Neue Zeile (Zeilenumbruch) |
| \\               | Rückwärtsschrägstrich |

### Rohstrings

Rohstrings (in Python mit r gekennzeichnet) interpretieren Escape-Sequenzen wie \n oder \t nicht, sondern behandeln sie als normale Zeichen.
Wie in diesem Beispiel dargestellt:

```py
text = r"Dies ist ein Rohstring, \n wird nicht als Zeilenumbruch behandelt"
```

### Mehrzeilige Kommentare

Mit 3 doppelten Anführungszeichen `"""` können mehrzeilige Kommentare in Python eingefügt werden.

```py
text = r"Dies ist ein Rohstring, \n wird nicht als Zeilenumbruch behandelt"

"""Dies ist ein mehrzeiliger Kommentar,
der nicht ausgegeben wird."""
```

### Indexierung und Slicing von Strings

Strings verwenden Indizes und Slices genauso wie Listen. 
Wir können uns den String `'Hello world!'` als Liste vorstellen, bei der jedes Zeichen im String einen entsprechenden Index hat:

Hier ein Beispiel, das absichtlich als Bild aus dem Text-Book eingefügt wurde:
<img src='imgs/hello_world.PNG'>

Der Leerschlag und das Ausrufezeichen werden mitgezählt. Insgesamt sind es also 12 Zeichen, von Index 0 bis Index 11.

### Die `upper()`, `lower()`, `isupper()` und `islower()`-Methoden

Mit den Befehlen `upper()` und `lower()` kann ein String in Grossbuchstaben, bzw. Kleinbuchstaben umgewandelt werden.
Dazu wird der Variablenname verwendet und dann die entsprechende Variante dahinter gesetzt:

```py
test1 = 'mein name ist ben'
test1 = test1.upper()

print(test1)
Ausgabe:
MEIN NAME IST BEN

test2 = 'Mein Name ist Gwen'
test2 = test2.lower()

print(test2)
Ausgabe:
'mein name ist gwen'
```
**Beispiel: Verwendung von `upper()` und `lower()`**

Die Methoden `upper()` und `lower()` sind nützlich, wenn wir mit Benutzereingaben arbeiten, bei denen die Gross- und Kleinschreibung keine Rolle spielen soll.
Angenommen, wir möchten überprüfen, ob ein Benutzer "ja" eingibt, unabhängig davon, wie er es schreibt (z. B. "Ja", "JA", "jA", etc.). 

```py
antwort = input("Möchten Sie fortfahren? (ja/nein): ")

#Durch das konvertieren von antwort in Kleinbuchstaben mit .lower() können wir es leicht mit "ja" vergleichen.
if antwort.lower() == "ja":
    print("Fortfahren...")
else:
    print("Abbrechen...")
```

Die Methoden `islower()` und `isupper()` werden verwendet, um zu überprüfen,
ob alle Buchstaben in einem String entweder in Klein- oder Grossbuchstaben vorliegen.

**`islower()`**
`islower()` gibt `True` zurück, wenn alle alphabetischen Zeichen im String klein geschrieben sind.
Wenn es keine Buchstaben gibt oder der String gemischte Groß- und Kleinbuchstaben enthält, gibt es `False` zurück.

Beispiel:
```python
text = "hallo welt"
print(text.islower()) 

Output: True
```
**`isupper()`**
`isupper()` gibt `True` zurück, wenn alle alphabetischen Zeichen im String groß geschrieben sind.
Andernfalls gibt es `False` zurück.

Beispiel:
```py
text = "HALLO WELT"
print(text.isupper())

Output: True
```

### Die isX-String-Methoden

Neben `islower()` und `isupper()` gibt es mehrere String-Methoden, die mit "is" beginnen und einen booleschen Wert zurückgeben, der die Natur des Strings beschreibt. Hier sind einige gängige isX-Methoden:

- **`isalpha()`**: Gibt `True` zurück, wenn der String nur aus Buchstaben besteht und nicht leer ist.
- **`isalnum()`**: Gibt `True` zurück, wenn der String nur aus Buchstaben und Zahlen besteht und nicht leer ist.
- **`isdecimal()`**: Gibt `True` zurück, wenn der String nur aus Dezimalziffern besteht und nicht leer ist.
- **`isspace()`**: Gibt `True` zurück, wenn der String nur aus Leerzeichen, Tabs oder Zeilenumbrüchen besteht und nicht leer ist.
- **`istitle()`**: Gibt `True` zurück, wenn jedes Wort im String mit einem Großbuchstaben beginnt und nur aus Kleinbuchstaben besteht.

Beispiele:
```py
print('hallo'.isalpha())       # True
print('hallo123'.isalnum())    # True
print('123'.isdecimal())       # True
print('   '.isspace())         # True
print('Das Ist Ein Titel'.istitle())  # True
```

Anwendung zur Eingabevalidierung:

Die isX-Methoden sind hilfreich, um Benutzereingaben zu validieren. Hier ein Beispiel, 
das den Benutzer wiederholt nach seinem Alter und einem neuen Passwort fragt, 
bis eine gültige Eingabe erfolgt:

```py
while True:
    print('Geben Sie Ihr Alter ein:')
    alter = input()
    if alter.isdecimal():
        break
    print('Bitte geben Sie eine Ganzzahl für Ihr Alter ein.')

while True:
    print('Wählen Sie ein neues Passwort (nur Buchstaben und Zahlen):')
    passwort = input()
    if passwort.isalnum():
        break
    print('Passwörter dürfen nur Buchstaben und Zahlen enthalten.')
```

### Die Methoden `startswith()` und `endswith()` für Strings

Die Methoden `startswith()` und `endswith()` geben `True` zurück, wenn der String, auf dem sie aufgerufen werden,
mit dem angegebenen String beginnt bzw. endet. Andernfalls geben sie `False` zurück.

Beispiele:

```python
print("supercode.py".endswith(".py"))                 # True
print("supercode.txt".endswith(".py"))                # False
print("12345".endswith("45"))      # True
print("12345".endswith("5"))       # True
print("12345".endswith("123"))     # False
```

### Die `join()` und `split()`-Methoden

Mit `join()` können Strings miteinander kombiniert werden, mit `split()` können  sie getrennt werden.

```python
# Verbindet eine Liste von Wörtern zu einem String mit Leerzeichen. Die einzelnen Elemente werden zusammengeführt.
woerter = ['Das', 'ist', 'ein', 'Test']
satz = ' '.join(woerter)

print(satz)
Output: "Das ist ein Test"
```

Am Platz des Leerzeichens vor `.join(woerter)` kann beliebig etwas eingefügt werden. Im Beispiel wurde ein Leerzeichen verwendet,
es kann aber auch ein Buchstabe sein, dieser wird aber zwischen jedem einzelnen Element ausgegeben. 
Wird also beispielsweise `'s'` eingefügt, sieht der Output so aus:

```python
# Verbindet eine Liste von Wörtern zu einem String mit Leerzeichen. Die einzelnen Elemente werden zusammengeführt.
woerter = ['Das', 'ist', 'ein', 'Test']
satz = 's'.join(woerter)

print(satz)
Output: "DassistseinsTest"
```

Die `split()`-Methode macht genau das umgekehrte:

```py
satz = "Das ist ein Test"
woerter = satz.split()

print(woerter)  
Output: ['Das', 'ist', 'ein', 'Test']

# Zerlegt einen String anhand eines Kommas
daten = "Apfel,Banane,Kirsche"
fruechte = daten.split(',')

print(fruechte)  
Output: ['Apfel', 'Banane', 'Kirsche']
```

### `rjust()`, `ljust()`, `center()`

**`rjust(width, fillchar)`**: Rechtsbündelt den String. In Klammern kann angegeben werden, mit wie vielen Zeichen und welchem der Abstand gefüllt wird,
sodass der String die angegebene Breite erreicht.

Beispiel:
```py
text = "Hallo"
print(text.rjust(10, '-'))

Output: 
-----Hallo
```

**`ljust(width, fillchar)`**: Linksbündelt den String. In Klammern kann angegeben werden, mit wie vielen Zeichen und welchem der Abstand gefüllt wird,
sodass der String die angegebene Breite erreicht.

Beispiel:
```py
text = "Hallo"
print(text.ljust(10, '-'))

Output: 
Hallo-----
```

**`center(width, fillchar)`**: Zentriert den String und füllt beide Seiten mit einem angegebenen Zeichen, sodass der String die angegebene Breite erreicht.

Beispiel:
```py
text = "Hallo"
print(text.center(10, '-'))

Output: 
--Hallo---
```

### `strip()`,`rstrip()` und `lstrip()`

Die drei Befehle `strip()`,`rstrip()` und `lstrip()` machen genau das umgekehrte von `rjust()`, `ljust()`, `center()` und löschen angegebene Zeichen oder Leerschläge. 

Beispiele:

```py
#strip()
text = "---Hallo---"
print(text.strip('-'))

Output: Hallo

#rstrip()
text = "---Hallo---"
print(text.rstrip('-'))

Output: ---Hallo

#lstrip()
text = "---Hallo---"
print(text.lstrip('-'))

Output: Hallo---
```

### Kopieren und Einfügen von Strings mit `pyperclip`

**`pyperclip.copy(text)`**: Kopiert den angegebenen String in die Zwischenablage.
Damit können wir den kopierten Text überall einfügen, wo das Einfügen von Text möglich ist.

Beispiel:
```py
import pyperclip
pyperclip.copy("Hallo, Welt!")
```

**`pyperclip.paste()`**: Fügt den aktuellen Inhalt der Zwischenablage ein und gibt diesen als String zurück.

Beispiel:
```py
import pyperclip
text = pyperclip.paste()
print(text)
```

Diese Funktionen sind praktisch, um automatisch Text zu kopieren oder aus der Zwischenablage zu holen.


## Übungen während den Lektionen (needs to be udpated)

### 08.10.2024 Pypi

Versionskontrolle = 0.0.1 allererste Version
Höhere Version "6.4.5" = weiterentwickelt


#### Art Python

Auf der Seite von Art Python kann direkt der Link kopiert werden, der zur Installation verwendet wird. 