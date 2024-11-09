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
Index ist die Zeile und Column die Spalte. Der Index identifiziert die Zeilen, während die Spalten die verschiedenen Datenattribute darstellen.

### Daten abfragen und ändern
Auf das Dataframe kann einfach durch `[]`zugegriffen werden (z.B. `df["Name"]` gibt die Werte der Spalte `"Name"` aus)
### Group By
Die `groupby`-Methode ermöglicht es, Daten nach bestimmten Kriterien zu gruppieren und Aggregatfunktionen anzuwenden. 

Beispiel:
```Python
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'Alice'],
    'Age': [25, 30, 35, 25],
    'Score': [85, 90, 95, 88]
}
df = pd.DataFrame(data)
grouped = df.groupby('Name').mean()
print(grouped)
```

### Pivot
Mit der `pivot`-Funktion können Zeilen in Spalten und Spalten in Zeilen umgewandelt werden.

Beispiel:
```Python
data = {
    'Date': ['2023-01-01', '2023-01-02', '2023-01-01', '2023-01-02'],
    'City': ['New York', 'New York', 'Los Angeles', 'Los Angeles'],
    'Temperature': [30, 32, 75, 78]
}
df = pd.DataFrame(data)
pivoted = df.pivot(index='Date', columns='City', values='Temperature')
print(pivoted)
```
### Transpose
Mit `transpose` können Zeilen und Spalten vertauscht werden.

## Daten importieren
Verschiedensten Daten können eingelesen und zu Dataframes umgewandelt werden (Excel, csv, SQL, ...).

Für Excel und csv-Dateien funktioniert es sehr einfach:
```Python
# CSV-Datei importieren
df = pd.read_csv('data.csv')

# Excel-Datei importieren
df = pd.read_excel('data.xlsx')
```
Für eine SQL-Datenbank-Datei ist es etwas aufwändiger:
```Python
import pandas as pd
import sqlite3

# Verbindung zur SQLite-Datenbank herstellen
conn = sqlite3.connect('example.db')

# SQL-Abfrage definieren
query = "SELECT * FROM tablename"

# Daten aus der SQL-Datenbank in ein DataFrame importieren
df = pd.read_sql_query(query, conn)

# Verbindung schließen
conn.close()
```

### Tabellenbereiche
Es können auch nur bestimmte Bereiche einer Datei importiert werden. Mit `usecols` kann dieser Bereich spezifiziert werden.
### Unbekannte Werte
Unbekannte Werte können ersetzt oder die Zeilen, die unbekannte Werte enthalten nicht eingelesen werden:

```python
import pandas as pd

data = {
    'Name': ['Alice', 'Bob', None],
    'Age': [25, None, 35]
}
df = pd.DataFrame(data)

# Fehlende Werte anzeigen
print("Vor dem Ersetzen der fehlenden Werte:")
print(df)

# Fehlende Werte ersetzen
df.fillna({'Name': 'Unknown', 'Age': 0}, inplace=True)
```

## Daten exportieren
Das Dataframe kann am Schluss in verschiedenen Formaten exportiert und gespeichert werden.
```Python
df.to_csv('output.csv', index=False)
df.to_excel('output.xlsx', index=False)
```
`index = False` sagt, dass der Index des Dataframes nicht in die Ausgabe geschrieben werden soll.