# pyRserve - `R`-Code in `Python` nutzen
- [Einleitung](#einleitung)
  - [Weshalb kann es von Vorteil sein, `R`-Code in `Python` zu nutzen?](#weshalb-kann-es-von-vorteil-sein-r-code-in-python-zu-nutzen)
- [Installation](#installation)
- [Vorbereitung](#vorbereitung)
- [Code ausführen](#code-ausführen)
  - [String-Evaluation in `R`](#string-evaluation-in-r)
  - [Variablen definieren und aufrufen](#variablen-definieren-und-aufrufen)
  - [Funktionen definieren und aufrufen](#funktionen-definieren-und-aufrufen)
  - [Umgang mit komplexen Ausgabe-Objekten von `R`-Funktionen](#umgang-mit-komplexen-ausgabe-objekten-von-r-funktionen)
  - [Trennung der Verbindung zum Server](#trennung-der-verbindung-zum-server)
- [Aufgaben](#aufgaben)
  - [Plotten mit `pyRserve` über `ggplot2`](#plotten-mit-pyrserve-über-ggplot2)
  - [Berechnung einer ANOVA und anschliessenden Post-Hoc-t-Tests](#berechnung-einer-anova-und-anschliessenden-post-hoc-t-tests)

## Einleitung
### Weshalb kann es von Vorteil sein, `R`-Code in `Python` zu nutzen?

Einige statistische Auswertungen sind in `Python` mit Hilfe von Packages möglich. Werden in einer Studie allerdings fortgeschrittenere statistische Auswerteverfahren benötigt, welche in `Python` nicht zur Verfügung stehen, bietet sich die Möglichkeit an, die Auswertung der Daten mit `R` vorzunehmen. Die ausgewerteten Daten können dann direkt in einem `Python`-Skript aufgegriffen und weiterverarbeitet werden, ohne diese zuerst aus `R` zu exportieren, um sie dann wieder in `Python` zu importieren. Diese Schnittstelle bietet zum einen das Package `rpy2` auf Linux und MacOS, zum anderen `pyRserve` zusätzlich zu den vorhin genannten auch auf Windows. Hierbei ist es so, dass das `rpy2` eigenständig auf den jeweiligen Systemen laufen kann, während `pyRserve` eine Verbindung zu einem Server benötigt. 

Wir beschäftigen uns im folgenden Teil mit `pyRserve`. Falls du allerdings noch mehr Infos zu `rpy2` haben möchtest, klicke hier: [`rpy2`-Dokumentation](https://rpy2.github.io/doc/v3.5.x/html/index.html)

## Installation 

Öffne als erstes ein `Terminal` und installiere das `Python`-Paket `pyRserve`: 
```sh 
pip install pyRserve
```
Als nächstes, öffne `R` und installiere das Package `Rserve`:
```r
install.packages("Rserve", dependencies = TRUE)
```
Nun hast du beide Pakete installiert, welche für das Ausführen von `R`-Code in `Python`benötigt werden.

## Vorbereitung 

Bevor jeweils `R`-Codeblöcke in `Python` verwendet werden können, muss zuerst `Rserve` geladen werden. Zudem muss eine Verbindung zum Server aufgebaut werden, in welchem die Berechnungen ausgeführt werden sollen. Führe dazu folgenden Code in `R` aus: 
```r
library("Rserve") # lade Rserve
Rserve() # baue Verbindung zu Server auf
```
Dabei wird standardmässig derselbe Standort der Server verwendet, welcher auch für die Installation der `R`-Packages genutzt wird. Auf Wunsch kann natürlich auch ein eigener Server verwendet werden. Mehr Infos dazu unter: [`pyRserve`-Dokumentation](https://pyrserve.readthedocs.io/en/latest/manual.html#string-evaluation-in-r)

Die Verbindung zum Server kann später in `Python` wieder getrennt werden, wenn diese nicht mehr benötigt wird.

Um später dem Server `R`-Code zu übergeben, muss im `Python`-Skript zuerst das Package importiert werden und danach mit der Funktion `connect` auch hier eine Verbindung zum Server aufgebaut werden. Um den Code etwas übersichtlicher zu halten, ist es hilfreich, eine Variable zu definieren, welche die Funkton `connect` beeinhaltet. 

```py
import pyRserve # importiere pyRserve
conn = pyRserve.connect() # baue Verbindung zu Server auf
```

Es ist ratsam, die Packages `numpy` und `pandas` ebenfalls zu importieren, falls mit Datensätzen gearbeitet wird. Leider ist `pyRserve` mit der Handhabung mit `pandas`-Dataframes etwas limitiert, jedoch funktioniert der Umgang mit `numpy`-Arrays problemlos. Aus diesem Grund ist es ratsam, Dataframes zuerst zu `numpy`-Arrays zu konvertieren, falls diese danach in `R` als Dataframes gebraucht werden. Hierfür kann die Funktion `to_numpy()` hilfreich sein, siehe auch [`pandas`-Dokumentation](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_numpy.html)

## Code ausführen

Nun kann mit dem Ausführen des `R`-Codes in `Python` gestartet werden.

### String-Evaluation in `R`

Um `R`-Code als String an den Server zu übermitteln und den evaluierten Wert zurück zu geben, gibt es folgenden Befehl: 
```py
conn.eval('3 + 5')
>>> 8.0
```

Um einen String zu evaluieren und gleichzeitig unnötige Kommunikation mit dem Server zu vermeiden, bietet sich folgende Funktion an:

```py 
conn.voidEval('3 + 5')
```

Dies bietet sich beispielsweise an, wenn eine Funktion definiert wird: 

```py 
conn.voidEval('doubleit <- function(x) { x*2 }') # definiere Funktion ohne Rückgabewert
conn.eval('doubleit(2)') # auswerten mit Rückgabewert vom Server
>>> 4.0
```

### Variablen definieren und aufrufen

Variablen zu definieren ist grundsätzlich auch über die String-Evaluation möglich, jedoch ist eine elegantere Variante die folgende:
```py
conn.r.aVar = "abc" # definiere String-Variable "aVar"
a = 2 # erstelle Python-Variable
conn.r.b = a * 2 # definiere Integer-Variable "b" unter Verwendung von a
```

### Funktionen definieren und aufrufen

Wie oben schon erwähnt, können Funktionen mittels String-Evaluation definiert werden:

```py
# definiere einige Funktionen
conn.voidEval('func0 <- function() { "hello world" }')
conn.voidEval('func1 <- function(v) { v*2 }')
conn.voidEval('funcKW <- function(a1=1.0, a2=4.0) { list(a1, a2) }')
```

Aufrufen der Funktionen geschieht ähnlich wie bei den Variablen: 

```py
conn.r.func0()
>>> "hello world"
conn.r.func1(5)
>>> 10
conn.r.funcKW(a2=6.0)
>>> [1.0, 6.0]
```

Ausserdem können auch in `R` integrierte Funktionen aufgerufen werden:

```py
conn.r.length([1,2,3]) # gebe Länge der Liste aus 
>>> 3
```

Um eine Funktion auf ein Element anzuwenden, kann `sapply` verwendet werden:

```py
conn.r.arr = numpy.array([1, 2, 3])

conn.r.sapply(conn.r.arr, conn.r.double) # wende "double" auf "arr" an
```

Allerdings ist die oben aufgeführt Variante etwas aufwändig, denn mit `conn.r.arr` wird zuerst ein Numpy-Array in `R` als `arr` definiert und an den Server gesendet, um ihn dann später wieder in der Funktion `sapply` wieder aufzurufen. Dabei wird `arr` zuerst vom Server an den Benutzer gesendet, um danach mittels `sapply` zu sagen, dass die Funktion `double` auf die `R`-Variable `arr` angewendet werden soll. Diese Information wird dann wiederum an den Server geschickt, der dann die Operation ausführt und das Resultat wieder an den Benutzer zurücksendet. 

Um die Menge an Datenverkehr einzugrenzen kann für die Variable `arr` eine Referenz angegeben werden, welche dann dem Server mitteilt, dass er auf die entsprechende Variable zurückgreifen soll, ohne diese hin und her zu senden. Dies ist folgendermassen möglich: 
```py
conn.r.arr = numpy.array([1, 2, 3])

conn.r.sapply(conn.ref.arr, conn.r.double) # wende "double" auf "arr" an, mit Vermeidung von unnötigem Datenverkehr
```

### Umgang mit komplexen Ausgabe-Objekten von `R`-Funktionen

Einige Funktionen in `R` - gerade statistische Tests - geben meist komplexe Ausgabe-Objekte zurück, welche einzelne Werte beinhalten, die man meist extrahieren möchte. 
Um dies zu tun, kann im Grunde die standardmässige Indexierung von `pandas` verwendet werden. 

Möchten wir beispielsweise einen t-Test berechnen und uns interessiert das Konfidenzintervall, können wir wie folgt darauf zugreifen: 

```py
res = conn.eval('t.test(c(1,2,3,1),c(1,6,7,8))') # berechne t-Test

res # Aufrufen der Testresultate
>>> <TaggedList(statistic=TaggedArray([-2.30541984]),
>>> parameter=TaggedArray([ 3.56389482], tags=['df']),
>>> p.value=0.090532640733331213,
>>> conf.int=TaggedArray([-8.49269413,  0.99269413], attr={'conf.level': array([ 0.95])}),
>>> estimate=TaggedArray([ 1.75,  5.5 ], tags=['mean of x', 'mean of y']),
>>> null.value=TaggedArray([ 0.], tags=['difference in means']),
>>> alternative='two.sided',
>>> method='Welch Two Sample t-test',
>>> data.name='c(1, 2, 3, 1) and c(1, 6, 7, 8)')>

res['conf.int'][0] # auf untere Schranke des Konfidenzintervalls zugreifen
>>> -8.49269413

res['conf.int'].attr['conf.level'] # auf Attribute des Konfidenzintervalls zugreifen
>>> array([ 0.95])
```

Von hier aus können dann natürlich die Informationen aus den Tests weiterverarbeitet und im `Python`-Skript eingebunden werden. 

### Trennung der Verbindung zum Server

Um nach einer Sitzung die Verbindung zum Server zu trennen, gibt es zwei Möglichkeiten: 

```py 
conn.close() # Verbindung schliessen
```
Schliesst die Verbindung zum Server, bietet sich an, am Ende des Skripts einzubauen. 
Um allerdings die Verbindung ganz zu trennen ist folgende Funktion vorhanden:
```py
conn.shutdown() # Verbindung ganz trennen
```
Wichtig ist hierbei, dass, falls `shutdown()` zu früh verwendet wird, dann auch die `R`-Funktion `Rserve()` wieder neu aufgerufen werden muss, um eine Verbindung zum Server aufzubauen. 

Mit diesen Infomationen, solltest du nun das Werkzeug haben, folgende zwei Aufgaben zu lösen: 

Falls dennoch etwas unklar sein sollte oder du gerne noch detailliertere Informationen zum vorgestellten Package haben würdest, siehe hier: [`pyRserve`-Dokumentation](https://pypi.org/project/pyRserve/)

## Aufgaben

### Plotten mit `pyRserve` über `ggplot2`

Verwende `ggplot2`, um in `R` einen Scatterplot zu erstellen, welcher eine Trendline beinhaltet. Der entstandene Plot soll als PNG-Datei exportiert und dann in `Python` angezeigt werden kann. 

Verwende dabei folgendes Template und ergänze die jeweiligen Schritte: 
```py
# Schritt 0: Importiere Packages
import pyRserve
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg # um Bild später zu laden

# Schritt 1: Mit Rserve verbinden


# Schritt 2: Erstelle zufällige Daten, welche eine lineare Abhängigkeit beinhalten
x = np.random.rand(50)
y = 2 * x + np.random.normal(0, 0.1, 50)  # lineare Abhängigkeit mit etwas Rauschen darin 

# Schritt 3: Erstelle zuerst die Variablen und dann ein Dataframe in R mit Variablen x,y


# Schritt 4: Verwende ggplot2 in R, um einen Scatterplot mit einer Trendlinie zu erstellen und speichere Plot
# Tipp: Verwende String-Evaluation


# Schritt 5: Schliesse die Verbindung zum Server wieder


# Schritt 6: Plot in Python einbinden
img = mpimg.imread("scatter_plot.png") # Bild in Python laden, in selbem Ordner

# Öffne den Plot in Python, Tipp: `imshow()`


```

### Berechnung einer ANOVA und anschliessenden Post-Hoc-t-Tests

Berechne eine ANOVA mit drei unterschiedlichen Gruppen in `R` und schreibe ein Programm, welches dann aufgrund des p-Werts entscheidet, ob noch Post-Hoc-t-Tests berechnet werden sollten. Gebe die Resultate der Tests jeweils aus. 

Verwende dabei folgendes Template und ergänze die jeweiligen Schritte: 
```py
import pyRserve
import numpy as np
from itertools import combinations # später für Anzahl Kombinationen der t-Tests 

# Schritt 1: Mit Rserve verbinden
conn = pyRserve.connect()

# Schritt 2: Erstelle 3 Gruppen mit randomiserten Daten
group1 = np.random.normal(50, 5, 30)  # Gruppe 1: Mean=50, SD=5
group2 = np.random.normal(55, 5, 30)  # Gruppe 2: Mean=55, SD=5
group3 = np.random.normal(50, 5, 30)  # Gruppe 3: Mean=55, SD=5

# Schritt 3: Erstelle Variablen und Dataframe in R, beachte dabei, dass die Gruppenzugehörigkeit als Faktoren definiert werden sollten


# Schritt 4: Führe ANOVA durch, extrahiere p-Wert und gebe ihn aus 


print(f"ANOVA p-value: {anova_p_value}")

# Schritt 5: Überprüfe, ob ANOVA signifikant war (p < 0.05)
alpha = 0.05
if anova_p_value < alpha:
    print("ANOVA ist signifikant. Durchführung von Post-Hoc-t-Tests mit Bonferroni-Korrektur.\n")
    
    # Definiere Dictionary für spätere Gruppenpaare für paarweise t-Tests 
    groups = {'Gruppe1': group1, 'Gruppe2': group2, 'Gruppe3': group3}
    
    # Berechne paarweise t-Tests und wende Bonferroni-Korrektur an
    num_tests = 3  # drei Tests paarweise
    bonferroni_alpha = alpha / num_tests  # Bonferroni-Korrektur
    
    # Durchführung paarweiser t-Tests und Anwendung der Bonferroni-Korrektur mit anschliessender Resultat-Ausgabe
    for (g1, g2) in combinations(groups.keys(), 2): # Kombinationen der drei Gruppen
        
        # Berechne t-Tests und extrahiere p-Wert
        
        
        # Wende Bonferroni-Korrektur auf p-Wert an
        corrected_p_value = p_value * num_tests
        corrected_p_value = min(corrected_p_value, 1)  # p-Wert kann nicht grösser 1 sein
        
        # Gebe jeweilige Resultate aus
        

else:
    print("ANOVA ist nicht signifikant. Keine weiteren Tests nötig.")

# Schliesse Verbindung mit Rserve


# Schliesse Verbindung zu Server ganz


```

