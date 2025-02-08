# pyRserve Peer-Review
<span style="font-size: 0.9em;"><i>- Johanna</i>

## Allgemeines Feedback
1. Der gesamte Bericht ist sehr stringent geschrieben
2. Der Code ist gut und nachvollziehbar auskommentiert
3. Die Aufgaben sind anhand des Berichtes verständlich und lösbar und bilden eine schöne Verknüpfung
4. Hilfreich sind ebenfalls die Verlinkungen auf externe Websites
5. Die Schwachstellen des Pakets sind erkenntlich identifiziert und gelöst
6. Auch optisch ist der Bericht sehr übersichtlich gestaltet

&rarr; Insgesamt ist es mir schwergefallen, nicht am laufenden Band "gut gemacht" zu schreiben, sondern mein Feedback etwas eloquenter zu gestalten. 😉

## Fragen & Anmerkungen
- Für noch bessere Verständlichkeit wäre es ggf. hilfreich, etwas mehr zwischen der Sprache `R` und der Benutzendenoberfläche `RStudio` zu differenzieren und diese nicht synonym zu verwenden

- Bei dem Beispiel der Anwendung von Funktionen könnten welche verwendet werden, die vorher kreiert wurden. Das würde es vermutlich ein Nachvollziehen noch mehr beflügeln

- im Skript für Aufgabe 2 steht sowohl conn.close() als auch conn.shutdown() wofür mir ein Fehler aufgrund der Redundanz ausgegeben wurde. Ist beides drin, um etwas auszuwählen oder ist doch beides notwendig?


## Lösung der Aufgaben

### Aufgabe 1:
Das Skript zur Lösung von Aufgabe 1 ist [hier](pyrserve_plotting.py) zu finden.
Die Aufgabe war gut zu lösen. Ich wusste vorher auch nicht, dass es möglich ist, zufällige Daten zu generieren. Das auch noch dazuzulernen, war tatsächlich sehr faszinierend und zukünftig sicherlich hilfreich!
Leider kam bei mir wiederholt folgender Fehler, der auch durch ein Kopieren der zur Hand gegebenen sich nicht hat beheben lassen - allerdings habe ich mich auch nicht an den Tipp gehalten, den Ordner mit den Übungen außerhalb von OneDrive zu speichern.

    FileNotFoundError: [Errno 2] No such file or directory: 'scatter_plot.png'  
    PS C:\Users\jojol\OneDrive - Universitaet Bern\HS24\Programming Basics\programming_basics>


### Aufgabe 2:
Das Skript zur Lösung von Aufgabe 2 ist [hier](pyreserve_anova.py) zu finden.

Besonders mit der Hilfestellung hat sich Aufgabe 2 gut lösen lassen. Mehr gibt es eigentlich nicht zu sagen, das war wirklich easy going.

## Fazit
Könnte ich Noten vergeben, würde ich diesen Bericht und die Erarbeitung des `pyRserve-Pakets` mit einer 6,0 bewerten.  
Aus dem Bericht ließt sich deutlich heraus, dass sich gründlich mit dem Paket auseinandergesetzt  und dieses auch umfassend aufgearbeitet wurde.  
Der Bericht ist ausdifferenziert und einfach lesbar geschrieben. Ich würde behaupten, es braucht das sehr gute Verständnis eines Themas, um es anderen ebenfalls unkompliziert und eindeutig vermitteln zu können - das ist hier definitiv der Fall.  
Ein paar Fragen/Anmerkungen kamen beim Lesen auf, diese sind bereits oben aufgeführt, aber allgemein eher die *cherry on the top* als ein großartiges Manko.  
Insgesamt scheint `pyRserve` ein definitiv hilfreiches Paket zu sein, dessen Anwedung auch spätestens für die Masterarbeit relevant werden kann!