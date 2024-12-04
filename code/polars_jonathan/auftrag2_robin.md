### Hat die Grösse des Datensatzes einen Einfluss auf das Geschwindigkeitsverhältnis zwischen den beiden Packages?

Ja die Grösse des Datensatzes hat einen Einfluss auf die Geschwindigkeit zwischen den beiden Packages. Bei grossen Datensätzen ist Polars deutlich schneller als Pandas.


### Welche Funktionen sind in polars optimiert?

1. Lesen und Schreiben von Daten (schnelleres Einlesen grosser Dateien).
2. Filter- und Auswahloperationen (Polars filtert parallel und effizient).
3. Transformationen (schnelle Arithmetik und Funktionen auf ganzen Spalten).
4. Gruppierungen und Aggregation (Schnelle Gruppierung und Berechnung von Summen, Mittelwerten, Medianen usw).
5.  Arbeiten mit fehlenden Werten (Effizientes Erkennen, Filtern und Füllen fehlender Werte).
   

### Wieso könnte das sein?

Unter anderem liegt das sicherlich daran, dass Polars Rust als Systemsprache nutzt. Dazu kommen weitere Faktoren wie spaltenbasierte Speicherung und Multithreading, um maximale Leistung aus moderner Hardware herauszuholen. 