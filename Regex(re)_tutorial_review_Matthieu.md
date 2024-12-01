# Feedback zum Päckli

## Übersicht
Die Einteilung in Abstract, praktische Relevanz und Tutorial erscheint sinnvoll. Eine Zusammenführung der Dokumente 501, 502 und 503 wäre möglich gewesen um ein einzelnes Markdown-Dokument offen zu halten, wobei die Übungen ebenfalls als Markdown-Dokumente gespeichert wurden.

### Verbesserungsvorschlag

*Ein Markdown-Dokument* mit den Dokumenten 501, 502 und 503 sowie *ein Dokument im Python-Format* um die Übungen zu lösen. Dies würde eine bessere Übersicht verschaffen und eine schnellere Bearbeitung der Python-Files ermöglichen da das switchen zwischen beiden Dateien ohne Suche der korrekten betreffenden Anleitung ermöglichen.


### Abstract
Sinnvoll aufgebaut, die Verwendbarkeit von Regex wird aufgezeigt. Konkrete Beispiele welche erwähnt wurden werden bereits im Abstract aufgezeigt, somit kann ein direkter Einblick für die Verwendbarkeit des Moduls aufgeziegt werden.

Es wird klar aufgezeigt, dass das Funktion des Moduls auf eine andere Weise ebenfalls erreicht werden könnte, das `re`-Modul den zeitlichen Aufwand sowie die Komplexität um einges verringert.

### Praktische Relevanz
Die Strukturierung verschiedener Datei-Formaten wird angesprochen, die Beispiele für die praktische Relevanz werden deutlich aufgezeigt. Nicht ganz nachvollziehbar ist für mich wie die Datenqualität durch Regex verbessert werden kann. Eine Spezifizierung inwiefern die Datenqualität durch Regex verbessert werden kann ist meinerseits erwünscht.

### Tutorial
Sehr guter Überblick, start mit der Importation. Die Grundlegenede Funktionsweise ist ebenfalls gut erläutert, könnte jedoch noch mit einem Beispiel verdeutlicht werden. Die Beispiele kommen  dann direkt bei den literalen Zeichen sowie bei den Metazeichen, darum völlig zufriedenstellend.

#### Literale Zeichen
Beim Beispiel wird erwähnt, dass das Wort "Hallo" gefunden wird. Wird der String "Hallo Welt" ebenfalls gefunden?

#### Metazeichen
Bei den Metazeichen `.`, `^` und `$`wird ein konkretes Beispiel angegeben, bei den restlichen mittels des `+`jedoch sind diese weniger greifbar. 

#### Quantifizierer
Gute Darstellung und gute Beispiele.

#### Zeichengruppen und Alternativen
Die Syntax `[]` für Zeichengruppen wird auch mittels Beispiels optisch schön dargestellt. Bei den Alternativen gibt es keine gute optische Darstellung. Das Beispiel von Katze und Hund wird nicht angezeigt. 

### Grundlegende Funktionen in Regex
Die wichtigsten acht Funktionen werden erläutert sowie mittels eines jeweiligen, greifbaren Beispiel dargestellt. Nicht nur die Bedeutung der Funktion wird aufgezeigt, die Anwendungsmöglichkeit wird ebenfalls dargestellt. Die Anwendungsmöglichkeiten werden mittels sinnvoller Beispiele für diesen Kurs dargestellt.

### Übungen
Übung 1 bietet mit Musterlösung keine optimale Ausgabe:
Extrahierte Traumberichtsdaten (siehe Emotions und Themes):

Date: ['07-11-2023']

Emotions: ['Furcht', 'Neugier', 'Freiheit\n\nHauptthemen']

Themes: ['Vergangenheit', 'Freundschaft', 'Unbekanntes\n\nOrte']

Places: ['Altes Haus', 'Flur', 'Feld', 'Tal']

Die Übung 2 bietet eine optimale Anwendung des Erlernten.


## Fazit
- Sehr gute Beschreibung von Regex-Funktionen sowie zahleiche, sinnvolle Beispiele
- Achtsamkeit ist bei der Syntax zu empfehlen um minimale Fehler zu beheben
- Der Beanspruchungsgrad ist optimal, zusätzliche (vielleicht als unnötig empfundene) Informationen schaden nie.
- Der Hinweis auf das Cheetsheet für Regex ist durchaus sinnvoll.
