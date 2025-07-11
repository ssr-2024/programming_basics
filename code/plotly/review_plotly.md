# Review Plotly
## Das war gut
Das Tutorial war sehr gut und einfach verständlich aufgebaut. Ich habe das Gefühl, dass ich einen guten Einblick in das Package bekommen habe.

Die Aufgaben konnte ich auch alleine mit dem Tutorial umsetzen, ohne auf externe Hilfsmittel zugreifen zu müssen.

Der Einblick in das interaktive Dashboard war eine interessante Ergänzung. Es scheint eine coole Mögliche Erweiterung zum Package zu sein.
## Verbesserungsvorschläge
Ein Hinweis darauf, dass man das Package noch über pip installieren sollte, wäre hilfreich gewesen (daran habe ich vor der ersten Ausführung nicht gedacht). 

Da die Lösungen direkt unter den Aufgaben platziert worden sind, habe ich diese schon vor dem Lösen gesehen. Ein zweites Lösungsfile wäre vermutlich eine bessere Lösung gewesen. So hätte ich die Aufgaben ohne Einfluss der Lösungen lösen können.

Persönlich finde ich es etwas übersichtlicher, wenn längere Code-Befehle auf mehrere Zeilen verteilt wird. So kann die Lesbarkeit etwas verbessert werden.

Zum Beispiel:
```Python
fig = px.line(x=monate,
     y=besucherzahlen,
    title="Monatliche Besucherzahlen des Museums")
```
anstatt: 
```Python
fig = px.line(x=monate, y=besucherzahlen, title="Monatliche Besucherzahlen des Museums")
```