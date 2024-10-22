# Pandas
Pandas ist eine Abkürzung von Panaldata. Basierend auf NumPy und MatPlotLib. Ist geeignet um schnell in grosse Datensätze Einblick bekommen kann und darauf Arbeiten kann.
## DatenFrame
Grundstruktur für Datensätze. Format eigentlich wie ein Excel-Sheet (Zeilen und Spalten). `Index` ist die Zeilennummer und `Column` die Spalte.

### DatenFrame erstellen
Aus einem bereits existierenden Dokument kann man ein Datenframe erstellen. Dafür braucht man Informationen zum Datenformat (.csv, .xlsx, ...) und dem Pfad.
```Python
import pandas as pd
df = pd.read_csv("path/to/data.csv", 
    sep=';', # sagt welches Zeichen die Daten separiert
    header=3, # sagt, dass es 3 Zeilen gibt, welche nicht zu den Daten gehören
    nrows=2 # wie viele Zeilen
    usecols=[1,3], # von bis welche Spalte
    na_values=[999,-], # definiert 999 und - Werte durch NAN (Not a Number)
    ).dropna(0, how='any') # löscht alle indexes (0) oder columns (1) mit NAN Werte aus dem df
```

### Index und Column
Index ist die Zeile und Column die Spalte.
### Daten abfragen und ändern

### Group By

### Pivot

### Transpose

## Daten importieren

### Tabellenbereiche

### Unbekannte Werte

## Daten exportieren
