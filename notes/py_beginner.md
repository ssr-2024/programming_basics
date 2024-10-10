# Zeichenfolge in Python

Zeichenfolgenmethoden sind einer der gängigsten Methodentypen in Python. Sie müssen häufig Zeichenfolgen bearbeiten, um Informationen zu extrahieren oder ein bestimmtes Format einzuhalten. Python umfasst mehrere Zeichenfolgenmethoden, die für die Durchführung der gängigsten und nützlichsten Transformationen konzipiert sind.

Zeichenfolgenmethoden sind Bestandteil des str-Typs. Dies bedeutet, dass die Methoden als Zeichenfolgenvariablen oder direkt als Teil der Zeichenfolge vorhanden sind. Die .title()-Methode gibt beispielsweise die Zeichenfolge in großen Anfangsbuchstaben zurück und kann direkt mit einer Zeichenfolge verwendet werden:

```py
print("temperatures and facts about the moon".title())
```
    Ausgabe: Temperatures And Facts About The Moon

Das gleiche Verhalten und die gleiche Verwendung treten bei einer Variablen auf:

```py
heading = "temperatures and facts about the moon"
heading_upper = heading.title()
print(heading_upper)
```


## Teilen einer Zeichenfolge

Eine gängige Zeichenfolgenmethode ist .split(). Ohne Argumente teilt die Methode die Zeichenfolge an jedem Leerzeichen. Dadurch würde eine Liste aller Wörter oder Zahlen erstellt, die durch ein Leerzeichen getrennt sind:

```py
temperatures = "Daylight: 260 F Nighttime: -280 F"
temperatures_list = temperatures.split()
print(temperatures_list)
```

     Ausgabe: ['Daylight:', '260', 'F', 'Nighttime:', '-280', 'F']

In diesem Beispiel haben Sie es mit mehreren Zeilen zu tun, sodass das (implizite) Zeilenvorschubzeichen verwendet werden kann, um die Zeichenfolge am Ende jeder Zeile zu teilen und so einzelne Zeilen zu erstellen:

```py
temperatures = "Daylight: 260 F\n Nighttime: -280 F"
temperatures_list = temperatures.split('\n')
print(temperatures_list)
```

    Ausgabe: ['Daylight: 260 F', 'Nighttime: -280 F']

Diese Art des Teilens ist praktisch, wenn Sie eine Schleife zum Verarbeiten oder Extrahieren von Informationen benötigen, oder wenn Sie Daten aus einer Textdatei laden.
Suchen nach einer Zeichenfolge

Einige Zeichenfolgenmethoden können vor der Verarbeitung und ohne eine Schleife nach Inhalt suchen. Angenommen, Sie haben zwei Sätze, in denen die Temperaturen auf verschiedenen Planeten und Monden besprochen werden. Sie interessieren sich jedoch nur für Temperaturen, die im Zusammenhang mit unserem Mond stehen. Das heißt, wenn sich die Sätze nicht auf den Mond beziehen, sollten sie bei der Informationsextraktion nicht verarbeitet werden.

Die einfachste Möglichkeit, um zu ermitteln, ob ein bestimmtes Wort, Zeichen oder eine Gruppe von Zeichen in einer Zeichenfolge vorhanden ist, stellt die Verwendung des in-Operators dar:

```py
print("Moon" in "This text will describe facts and challenges with space travel")
```

    Ausgabe: False

```py
print("Moon" in "This text will describe facts about the Moon")
```

    Ausgabe: True

Ein Ansatz zum Suchen der Position eines bestimmten Worts in einer Zeichenfolge ist die Verwendung der .find()-Methode:

```py
temperatures = """Saturn has a daytime temperature of -170 degrees Celsius, while Mars has -28 Celsius."""
print(temperatures.find("Moon"))
```

    Ausgabe: -1

Die .find()-Methode gibt -1 zurück, wenn das Wort nicht gefunden wurde, oder sie gibt den Index (die Zahl, die die Position in der Zeichenfolge darstellt) zurück. Wie sie sich verhält, wenn Sie nach dem Wort Mars suchen, sehen Sie hier:

```py
temperatures = """Saturn has a daytime temperature of -170 degrees Celsius, while Mars has -28 Celsius."""
print(temperatures.find("Mars"))
```

    Ausgabe: 64

64 ist die Position, an der "Mars" in der Zeichenfolge vorkommt.

Eine weitere Möglichkeit zum Suchen nach Inhalten ist die Verwendung der .count()-Methode, die die Gesamtzahl der Vorkommen eines bestimmten Worts in einer Zeichenfolge zurückgibt:

```py
temperatures = """Saturn has a daytime temperature of -170 degrees Celsius, while Mars has -28 Celsius."""
print(temperatures.count("Mars"))
print(temperatures.count("Moon"))
```

    Output

    1
    0

Bei Zeichenfolgen in Python wird die Groß-/Kleinschreibung beachtet, was bedeutet, dass Mond und mond als unterschiedliche Wörter betrachtet werden. Für einen Vergleich ohne Beachtung der Groß-/Kleinschreibung können Sie eine Zeichenfolge mithilfe der .lower()-Methode vollständig in Kleinbuchstaben konvertieren:

```py
print("The Moon And The Earth".lower())
```

    Ausgabe: the moon and the earth

Ähnlich wie bei der .lower()-Methode verfügen Zeichenfolgen über eine .upper()-Methode, die das Gegenteil bewirkt und jeden Buchstaben in Großbuchstaben konvertiert:

```py
print("The Moon And The Earth".upper())
```

    Ausgabe: THE MOON AND THE EARTH

### Tipp

    Wenn Sie nach Inhalten suchen und diese überprüfen möchten, besteht ein stabilerer Ansatz darin, eine Zeichenfolge in Kleinbuchstaben zu konvertieren, damit ein Treffer nicht durch Groß-/Kleinschreibung verhindert wird. Wenn Sie z. B. zählen, wie oft das Wort der vorkommt, würde die Methode die Vorkommen von Der nicht mitzählen, obwohl beide dasselbe Wort sind. Sie können die .lower()-Methode verwenden, um alle Buchstaben in Kleinbuchstaben zu ändern.
## Überprüfen von Inhalten

Wenn Sie Text verarbeiten, um Informationen zu extrahieren, kann es vorkommen, dass dessen Darstellung uneinheitlich ist. Die folgende Zeichenfolge lässt sich beispielsweise einfacher verarbeiten als ein unstrukturierter Absatz:

```py
temperatures = "Mars Average Temperature: -60 C"
```

Um die durchschnittliche Temperatur auf dem Mars zu extrahieren, können Sie gut die folgenden Methoden verwenden:

```py
temperatures = "Mars Average Temperature: -60 C"
parts = temperatures.split(':')
print(parts)
print(parts[-1])
```

    Output

    ['Mars average temperature', ' -60 C']
    ' -60 C'

Im obigen Code wird blind darauf vertraut, dass alles nach dem Doppelpunkt (:) eine Temperatur ist. Die Zeichenfolge wird an dem : geteilt, wodurch eine Liste mit zwei Elementen erzeugt wird. Durch die Verwendung von [-1] mit der Liste wird das letzte Element zurückgegeben, bei dem es sich in diesem Beispiel um die Temperatur handelt.

Wenn der Text uneinheitlich ist, können Sie nicht dieselben Teilungsmethoden verwenden, um den Wert abzurufen. Sie müssen die Elemente mit einer Schleife durchlaufen und überprüfen, ob die Werte einen bestimmten Typ aufweisen. Python verfügt über Methoden, mit denen der Typ der Zeichenfolge überprüft werden kann:

```py
mars_temperature = "The highest temperature on Mars is about 30 C"
for item in mars_temperature.split():
    if item.isnumeric():
        print(item)
```

    Ausgabe: 30

Wie die .isnumeric()-Methode kann .isdecimal() nach Zeichenfolgen suchen, die wie Dezimalzahlen aussehen.

#### Wichtig!

Es kann überraschend sein, zu erfahren, dass "-70".isnumeric()False zurückgeben würde. Dies liegt daran, dass alle Zeichen in der Zeichenfolge numerisch sein müssten, und der Bindestrich (-) nicht numerisch ist. Wenn Sie negative Zahlen in einer Zeichenfolge überprüfen müssen, würde die .isnumeric()-Methode nicht funktionieren.

Es gibt zusätzliche Überprüfungen, die Sie auf Zeichenfolgen anwenden können, um nach Werten zu suchen. Bei negativen Zahlen wird der Bindestrich der Zahl vorangestellt, was sich mit der .startswith()-Methode erkennen lässt:

```py
print("-60".startswith('-'))
```

    Ausgabe: True

Auf ähnliche Weise hilft die .endswith()-Methode beim Überprüfen des letzten Zeichens einer Zeichenfolge:

```py
if "30 C".endswith("C"):
print("This temperature is in Celsius")
```

    Ausgabe: This temperature is in Celsius

# Transformieren von Text

Es gibt andere Methoden, die in Situationen helfen, in denen Text in etwas anderes transformiert werden muss. Bisher haben Sie Zeichenfolgen gesehen, die C für Celsius und F für Fahrenheit verwenden können. Sie können die .replace()-Methode verwenden, um Vorkommen eines Zeichens oder einer Zeichengruppe zu suchen und zu ersetzen:

```py
print("Saturn has a daytime temperature of -170 degrees Celsius, while Mars has -28 Celsius.".replace("Celsius", "C"))
```

    Ausgabe: Saturn has a daytime temperature of -170 degrees C, while Mars has -28 C.

Wie bereits erwähnt, ist .lower() eine gute Möglichkeit zum Normalisieren von Text, um eine Suche ohne Beachtung von Groß-/Kleinschreibung durchzuführen. Lassen Sie uns schnell überprüfen, ob in einigen Texten Temperaturen behandelt werden:

```py
text = "Temperatures on the Moon can vary wildly."
print("temperatures" in text)
```

    Ausgabe: False

```py
text = "Temperatures on the Moon can vary wildly."
print("temperatures" in text.lower())
```

    Ausgabe: True

Möglicherweise müssen Sie die Groß-/Kleinschreibung nicht ständig überprüfen, aber jeden Buchstaben in Kleinbuchstaben umzuwandeln, ist ein guter Ansatz, wenn der Text gemischte Groß-/Kleinschreibung verwendet.

Nachdem Sie den Text geteilt und die Transformationen ausgeführt haben, müssen Sie möglicherweise alle Teile wieder zusammensetzen. So, wie die .split()-Methode Zeichen trennen kann, kann die .join()-Methode sie wieder zusammensetzen.

Die .join()-Methode erfordert ein iterierbares Element (z. B. eine Python-Liste) als Argument, weshalb sich seine Verwendung von anderen Zeichenfolgenmethoden unterscheidet:

```py
moon_facts = ["The Moon is drifting away from the Earth.", "On average, the Moon is moving about 4cm every year."]
print(' '.join(moon_facts))
```

    Ausgabe: The Moon is drifting away from the Earth. On average, the Moon is moving about 4cm every year.

In diesem Beispiel wird ' ' verwendet, um alle Elemente in der Liste zu verknüpfen.



# Zeichenfolgenformat in Python

Neben der Transformation von Text und der Durchführung grundlegender Vorgänge wie Abgleich und Suche ist es wesentlich, den Text zu formatieren, wenn Sie Informationen darstellen. Die einfachste Möglichkeit zum Darstellen von Textinformationen mit Python ist die Verwendung der print()-Funktion. Es ist wichtig, in Variablen und anderen Datenstrukturen enthaltene Informationen in Zeichenfolgen zu überführen, die von print() verwendet werden können.

In dieser Lerneinheit lernen Sie mehrere gültige Methoden zum Einschließen von Variablenwerten in Text mithilfe von Python kennen.
Formatierung mit Prozentzeichen (%)

Der Platzhalter für die Variable in der Zeichenfolge ist %s. Verwenden Sie nach der Zeichenfolge ein weiteres %-Zeichen, gefolgt vom Variablennamen. Im folgenden Beispiel wird gezeigt, wie sie mithilfe des %-Zeichens Formatierungen vornehmen:

```py
mass_percentage = "1/6"
print("On the Moon, you would weigh about %s of your weight on Earth." % mass_percentage)
```

    Ausgabe: On the Moon, you would weigh about 1/6 of your weight on Earth.

Durch die Verwendung mehrerer Werte ändert sich die Syntax, da Klammern erforderlich sind, um die übergebenen Variablen einzuschließen:

```py
print("""Both sides of the %s get the same amount of sunlight, but only one side is seen from %s because the %s rotates around its own axis when it orbits %s.""" % ("Moon", "Earth", "Moon", "Earth"))
```

    Ausgabe: Both sides of the Moon get the same amount of sunlight, but only one side is seen from Earth because the Moon rotates around its own axis when it orbits Earth.

## Tipp

Obwohl diese Methode immer noch eine gültige Methode zum Formatieren von Zeichenfolgen ist, kann sie zu Fehlern und einer verschlechterten Übersichtlichkeit im Code führen, wenn Sie mit mehreren Variablen arbeiten. Jede der beiden anderen Formatierungsoptionen, die in dieser Lerneinheit beschrieben werden, eignet sich besser für diesen Zweck.
Die format() -Methode

Die .format()-Methode verwendet geschweifte Klammern ({}) als Platzhalter innerhalb einer Zeichenfolge, und sie verwendet Variablenzuweisung zum Ersetzen von Text.

```py
mass_percentage = "1/6"
print("On the Moon, you would weigh about {} of your weight on Earth.".format(mass_percentage))
```

    Ausgabe: On the Moon, you would weigh about 1/6 of your weight on Earth.

Sie müssen wiederholte Variablen nicht mehrmals zuweisen, was es weniger ausführlich macht, da weniger Variablen zugewiesen werden müssen:

```py
mass_percentage = "1/6"
print("""You are lighter on the {0}, because on the {0} you would weigh about {1} of your weight on Earth.""".format("Moon", mass_percentage))
```

    Ausgabe: You are lighter on the Moon, because on the Moon you would weigh about 1/6 of your weight on Earth.

Anstelle leerer geschweifter Klammern besteht die Ersetzung in der Verwendung von Zahlen. {0} bedeutet, dass das erste Argument (Index 0) für .format() verwendet wird, was in diesem Fall Moon ist. Für schlichte Wiederholungen funktioniert {0} gut, verschlechtert aber die Lesbarkeit. Um die Lesbarkeit zu verbessern, verwenden Sie Schlüsselwortargumente in .format(), und verweisen Sie dann innerhalb geschweifter Klammern auf dieselben Argumente:

```py
mass_percentage = "1/6"
print("""You are lighter on the {moon}, because on the {moon} you would weigh about {mass} of your weight on Earth.""".format(moon="Moon", mass=mass_percentage))
```

    Ausgabe: You are lighter on the Moon, because on the Moon you would weigh about 1/6 of your weight on Earth.

## Informationen zu f-Zeichenfolgen

Ab Python-Version 3.6 ist es möglich, f-Zeichenfolgen (f-strings) zu verwenden. Diese Zeichenfolgen sehen wie Vorlagen aus und verwenden die Variablennamen aus Ihrem Code. Die Verwendung von f-Zeichenfolgen im vorherigen Beispiel sähe wie folgt aus:

```py
print(f"On the Moon, you would weigh about {mass_percentage} of your weight on Earth.")
```

    Ausgabe: On the Moon, you would weigh about 1/6 of your weight on Earth.

Die Variablen werden in geschweifte Klammern gesetzt, und die Zeichenfolge muss das Präfix f verwenden.

Abgesehen davon, dass f-Zeichenfolgen weniger ausführlich sind als jede andere Formatierungsoption, ist es möglich, Ausdrücke innerhalb der geschweiften Klammern zu verwenden. Diese Ausdrücke können Funktionen oder direkte Vorgänge sein. Wenn Sie beispielsweise den Wert 1/6 als Prozentsatz mit einer Dezimalstelle darstellen möchten, können Sie die round()-Funktion direkt verwenden:

```py
print(round(100/6, 1))
```

    Ausgabe: 16.7

Bei F-Zeichenfolgen müssen Sie einer Variablen keinen Wert im Voraus zuweisen:

```py
print(f"On the Moon, you would weigh about {round(100/6, 1)}% of your weight on Earth.")
```

    Ausgabe: On the Moon, you would weigh about 16.7% of your weight on Earth.

Die Verwendung eines Ausdrucks erfordert keinen Funktionsaufruf. Alle der Zeichenfolgenmethoden sind ebenfalls gültig. Beispielsweise kann die Zeichenfolge eine bestimmte Groß-/Kleinschreibung für die Erstellung einer Überschrift erzwingen:

```py
subject = "interesting facts about the moon"
heading = f"{subject.title()}"
print(heading)
```

    Ausgabe: Interesting Facts About The Moon

# Zusammenfassung


Python-Zeichenfolgen sind einer der gängigsten Typen, die in der Sprache verwendet werden. In diesem Modul haben Sie einige seiner Zeichenfolgeneigenschaften und die gängigsten Methoden für deren Bearbeitung kennen gelernt. Schließlich haben Sie Möglichkeiten zum Formatieren von Zeichenfolgen mithilfe von drei verschiedenen Methoden kennen gelernt:

    Verwenden des %-Formatierers.
    Verwenden von .format() in einer Zeichenfolge.
    Verwenden von f-Zeichenfolgen.

Diese grundlegenden Kenntnisse helfen Ihnen bei anderen Datenstrukturen in Python, die gut mit Zeichenfolgen wie Wörterbüchern und Listen funktionieren.

# Operatoren in Python

Summieren: +, Subtrahieren -, Multiplizieren: *, Dividieren: /, Floor-Division (Abrundung): //, Modulo-Operator*: %
*In computing, the modulo operation returns the remainder or signed remainder of a division, after one number is divided by another, called the modulus of the operation.

## Runden
Die integrierte Python-Funktion round ist ebenfalls hilfreich. Sie verwenden sie, um auf die nächste ganze Zahl aufzurunden, wenn der Dezimalwert größer als .5 ist, oder abzurunden, wenn er kleiner als .5 ist. Wenn der Dezimalwert gleich .5 ist, rundet die Funktion auf die nächste gerade ganze Zahl auf. --> Das kann nicht stimmen, es wird abgerundet!!

## math-Bibliothek

Python bietet Bibliotheken, um komplexere Operationen und Berechnungen durchzuführen. Eine der gängigsten ist die math-Bibliothek. math ermöglicht Ihnen, mit floor und ceil zu runden, den Wert von Pi anzugeben und zahlreiche weitere Operationen auszuführen. Im Folgenden erfahren Sie, wie Sie diese Bibliothek zum Auf- oder Abrunden verwenden.

Durch das Runden von Zahlen können Sie den Dezimalteil eines Gleitkommawerts entfernen. Mit ceil können Sie festlegen, dass immer auf die nächste ganze Zahl aufgerundet werden soll, und mit floor, dass stets abgerundet werden soll.

```py
from math import ceil, floor

round_up = ceil(12.5)
print(round_up)

round_down = floor(12.5)
print(round_down)
```

# Einführung in Listen
Liste = Typus zum Speichern von Werten

### Zugreifen auf Listenelemente nach Index

Sie können auf jedes Element in einer Liste zugreifen, indem Sie den Index in Klammern [ ] hinter den Namen der Listenvariablen setzen. **Alle Indizes beginnen bei 0!**

### Ermitteln der Länge einer Liste

Verwenden Sie die integrierte Funktion len(), um die Länge einer Liste abzurufen. Der folgende Code erstellt eine neue Variable, number_of_planets. Der Code weist diese Variable mit der Anzahl der Elemente in der Liste planets (8) zu.

### Hinzufügen von Werten zu Listen

Listen in Python sind dynamisch: Sie können Elemente hinzufügen und entfernen, nachdem sie erstellt wurden. Um einer Liste ein Element hinzuzufügen, verwenden Sie die Methode .append(value).

### Entfernen von Werten aus Listen

Sie können das letzte Element in einer Liste entfernen, indem Sie die Methode .pop() für die Listenvariable aufrufen. --> **Frage: es ist nur möglich, das letze Element einer Liste zu entfernen?**

#### Negative Indizes
Indizes beginnen bei 0 (Null) und erhöhen sich. Negative Indizes beginnen am Ende der Liste und funktionieren rückwärts

### Suchen eines Werts in einer Liste

Um zu bestimmen, wo in einer Liste ein Wert gespeichert wird, verwenden Sie die Methode index der Liste. Diese Methode sucht nach dem Wert und gibt den Index dieses Elements in der Liste zurück. Wenn keine Übereinstimmung gefunden wird, wird -1 zurückgegeben.


### Verwenden von min() und max() mit Listen

Python verfügt über integrierte Funktionen zum Berechnen der größten und kleinsten Zahlen in einer Liste. Die max()-Funktion gibt die größte und min() die kleinste Zahl zurück.

### Aufteilen von Listen

Sie können einen Teil einer Liste mithilfe eines Slices abrufen. Ein Slice verwendet Klammern, verfügt aber anstatt eines einzelnen Elements über den Start- und Endindex. Wenn Sie ein Slice verwenden, erstellen Sie eine neue Liste, die mit dem Startindex beginnt und vor dem Endindex endet (und diesen **nicht** enthält).

### Sortieren von Listen

Um eine Liste zu sortieren, wenden Sie die Methode .sort() auf die Liste an. Python sortiert eine Liste von Zeichenketten in alphabetischer Reihenfolge und eine Liste von Zahlen in numerischer Reihenfolge. Rufen Sie .sort(reverse=True) für die Liste auf, um sie in umgekehrter Reihenfolge zu sortieren.

**Die Verwendung von sort ändert die aktuelle Liste.**

# Verwenden von while- und for-Schleifen

## while-Schleifen
Um das Ausführen einer unbekannten Anzahl von Schleifen zu unterstützen, können Sie eine while-Schleife verwenden.

Eine while-Schleife führt einen Vorgang aus, während (while) eine bestimmte Bedingung erfüllt ist. Sie können eine while-Schleife für folgende Zwecke verwenden:

- Suchen Sie in einer Datei nach einer anderen Zeile.
- Prüfen Sie, ob ein Flag festgelegt wurde.
- Prüfen Sie, ob ein Benutzer die Eingabe von Werten abgeschlossen hat.
- Prüfen Sie, ob sich etwas anderes geändert hat, um anzugeben, dass der Code die Ausführung des Vorgangs beenden kann.

**Wenn Sie while-Schleifen erstellen, müssen Sie vor allem darauf achten, dass sich die Bedingung ändert. Wenn die Bedingung immer „true“ (wahr) ergibt, wird Python Ihren Code so lange ausführen, bis das Programm abstürzt.** 

Eine while-Schleife besteht aus drei wichtigen Teilen:
1. Das Schlüsselwort while, gefolgt von einem Leerzeichen.
2. Bedingung, die Sie testen: Wenn die Bedingung „true“ entspricht, wird der Code innerhalb der while-Schleife ausgeführt.
3.  Der Code, den Sie für jede Iteration ausführen möchten, eingerückt mit geschachtelten Leerzeichen. Beispiel:
   
```py
while <condition>:
    # code here
```
## for-Schleifen

Sie verwenden eine for-Schleife mit iterierbaren Typen, in der Sie eine bekannte Anzahl von Schleifen durchlaufen, einmal für jedes Element im iterierbaren Typ.

*For-Schleifen können mehrere variablen umschließen.* **Überprüfen ob an richtiger Stelle im Skript.**

Die for-Schleife ist eine Anweisung mit fünf wichtigen Teilen:
- Das Wort for, gefolgt von einem Leerzeichen.
- Der Variablenname, den Sie für jeden Wert in der Sequenz (number) erstellen möchten. Beachten Sie, dass mehrere Variablen durch Kommata getrennt werden müssen.
- Das Wort in, das von Leerzeichen umgeben ist.
- Der Name der Liste (countdown im vorherigen Beispiel) oder der iterierbare Typ, für den sie eine Schleife durchlaufen möchten, gefolgt von einem Doppelpunkt (:).
- Der Code, den Sie für jedes Element im iterierbaren Objekt ausführen möchten, getrennt durch geschachtelte Leerzeichen.

## Zusammenfassung

In diesem Modul haben Sie eine Anwendung erstellt, die Benutzer auffordert, eine Liste von Planetennamen einzugeben, diese Planetennamen zu speichern und sie dann anzuzeigen.
Da Sie nicht wussten, wie viele Planeten die Benutzer eingeben würden, haben Sie eine while-Schleife verwendet. Sie verwenden while-Schleifen, um einen Codeblock auszuführen, während eine Bedingung erfüllt bleibt.
Sie haben jeden Planetennamen in einer Liste gespeichert.
Nachdem die Planetenliste erstellt wurde, haben Sie eine for-Schleife verwendet, um sie zu durchlaufen. Sie verwenden for-Schleifen mit Listen und anderen iterierbaren Typen, um den Code eine bekannte Anzahl von Malen auszuführen, einmal für jedes Element in der Liste der Planetennamen.

In diesem Modul haben Sie Folgendes gelernt:
- Ermitteln Sie, wann eine while-Schleife oder eine for-Schleife verwendet werden muss.
- Verwenden Sie eine while-Schleife, um eine Aufgabe mehrfach auszuführen, solange eine bestimmte Bedingung erfüllt bleibt.
- Verwenden Sie eine for-Schleife zum Iterieren durch Listendaten.


# Verwalten von Daten mit Python-Wörterbüchern
Mit Python-Wörterbüchern können Sie mit verwandten Datensätzen arbeiten. Ein Wörterbuch ist eine Sammlung von Schlüssel-Wert-Paaren. Stellen Sie sich dies wie eine Gruppe von Variablen in einem Container vor, wobei der Schlüssel der Name der Variablen und der Wert der darin gespeicherte Wert ist.

## Erstellen eines Wörterbuchs

Python verwendet geschweifte Klammern ({ }) und den Doppelpunkt (:), um ein Wörterbuch zu kennzeichnen. Sie können entweder ein leeres Wörterbuch erstellen und später Werte hinzufügen oder es zum Zeitpunkt der Erstellung auffüllen. Jedes Schlüssel-Wert-Paar wird dabei durch einen Doppelpunkt getrennt, und der Name jedes Schlüssels steht als Zeichenfolgenliteral in Anführungszeichen. Da der Schlüssel ein Zeichenfolgenliteral ist, können Sie einen beliebigen geeigneten Namen verwenden, um den Wert zu beschreiben.

**Standardbenennungsregeln für Python --> nochmal herausfinden**

Sie können Werte in einem Wörterbuch lesen. Wörterbuchobjekte verfügen über eine get-Methode, mit der Sie über seinen Schlüssel auf einen Wert zugreifen können. Wenn Sie den name ausgeben möchten, können Sie folgenden Code verwenden:

Input
```py
print(planet.get('name'))
```

Output

    Earth

Wie Sie vielleicht schon vermuten, ist der Zugriff auf Werte in einem Wörterbuch ein gängiger Vorgang. Glücklicherweise gibt es eine „Abkürzung“. Sie können den Schlüssel auch mit der Notation in eckigen Klammern ([ ]) übergeben. Bei dieser Methode wird weniger Code als mit get verwendet, und die meisten Programmierer verwenden stattdessen diese Syntax.

**Wenn kein Schlüssel verfügbar ist, gibt getNone zurück und [ ] lösen einen KeyError aus.**

## Ändern von Wörterbuchwerten

Sie können auch Werte innerhalb eines Wörterbuchobjekts ändern, indem Sie die update-Methode verwenden. Diese Methode akzeptiert ein Wörterbuch als Parameter und aktualisiert alle vorhandenen Werte mit den neuen Werten, die Sie bereitstellen.
Ähnlich wie bei der Verwendung der Abkürzung mittels eckiger Klammern ([ ]) zum Lesen von Werten können Sie dieselbe Abkürzung verwenden, um Werte zu ändern. Der Hauptunterschied bei der Syntax besteht in der Verwendung von = (manchmal auch als Zuweisungsoperator bezeichnet), um einen neuen Wert zur Verfügung zu stellen. 
Der Hauptvorteil der Verwendung von update ist die Möglichkeit, mehrere Werte in einem Vorgang ändern zu können. 

## Hinzufügen und Entfernen von Schlüsseln

Sie müssen nicht alle Schlüssel erstellen, wenn Sie ein Wörterbuch initialisieren. Tatsächlich müssen Sie gar keine erstellen. Wenn Sie einen neuen Schlüssel erstellen möchten, weisen Sie ihn einfach so zu wie einen vorhandenen.

**Bei Schlüsselnamen wird, wie überall in Python, die Groß-/Kleinschreibung beachtet.**

Um einen Schlüssel zu entfernen, verwenden Sie pop. pop gibt den Wert zurück und entfernt den Schlüssel aus dem Wörterbuch.

## Komplexe Datentypen

Wörterbücher können jeden Typ eines Werts speichern, einschließlich anderer Wörterbücher. Auf diese Weise können Sie komplexe Daten nach Bedarf modellieren. 
**Achtung, abhäging vom Typ der Variablen, können Fehler im Code sein!**

Um Werte in einem geschachtelten Wörterbuch abzurufen, verketten Sie eckige Klammern oder rufen get auf.

```py
print(f'{planet["name"]} polar diameter: {planet["diameter (km)"]["polar"]}')
```

Output

    Jupiter polar diameter: 133709

*Das f' in dem Python-Code steht für ein f-String (formatierter String), eine praktische Möglichkeit, Variablen oder Ausdrücke direkt in einen String einzufügen. Es wurde in Python 3.6 eingeführt und ermöglicht es, den Inhalt von Variablen oder komplexeren Ausdrücken in geschweiften Klammern {} innerhalb eines Strings anzuzeigen.*

## Abrufen aller Schlüssel und Werte

Die keys()-Methode gibt ein Listenobjekt zurück, das alle Schlüssel enthält. Sie können diese Methode verwenden, um alle Elemente im Wörterbuch zu durchlaufen.

### Ermitteln, ob ein Schlüssel in einem Wörterbuch vorhanden ist

Wenn Sie einen Wert in einem Wörterbuch aktualisieren, überschreibt Python entweder den vorhandenen Wert oder erstellt einen neuen Wert, wenn der Schlüssel nicht vorhanden ist. Wenn Sie einem Wert etwas hinzufügen möchten, statt ihn zu überschreiben, können Sie mithilfe von in überprüfen, ob der Schlüssel vorhanden ist. 

### Abrufen aller Werte

Ähnlich wie keys() gibt values() die Liste aller Werte in einem Wörterbuch ohne deren entsprechende Schlüssel zurück. values() kann hilfreich sein, wenn Sie den Schlüssel zu Bezeichnungszwecken verwenden.

Und noch einmal für die ganz Schlauen: *keys() gibt **alle Schlüssel** im Wörterbuch zurück, values() gibt **alle Werte** im Wörterbuch zurück*
