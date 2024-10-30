# Pandas in Python

Pandas ist eine leistungsstarke Bibliothek für die Arbeit mit Tabellen- und Zeitreihendaten. Sie bietet zwei zentrale Datenstrukturen: **Series** (1D) und **DataFrame** (2D).

### Installation
Um Pandas zu verwenden, muss es zunächst installiert werden. Dies kann über die Kommandozeile erfolgen:

```python
pip install pandas
```

### Verwendung
Nach der Installation kann Pandas importiert und verwendet werden, um Daten zu analysieren und zu manipulieren.

```python
import pandas as pd
```

Mit dem Alias `pd` lässt sich die Bibliothek effizient und übersichtlich im Code verwenden.


## DatenFrame

Ein DataFrame ist eine 2D-Datenstruktur (ähnlich einer Tabelle) mit beschrifteten Zeilen und Spalten.

DataFrames sind das Kernstück von Pandas und bieten viele nützliche Funktionen für die Datenanalyse.


## DatenFrame erstellen

Ein DataFrame kann aus einer Liste von Dictionaries, einer Liste von Listen oder direkt aus einer Datei erstellt werden.

### Beispiel: DataFrame aus einem Dictionary erstellen

```python
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [24, 27, 22],
    'City': ['Berlin', 'Hamburg', 'Munich']
}
df = pd.DataFrame(data)
print("DataFrame erstellt aus Dictionary:\n", df)
```


## Index und Columns

DataFrames haben einen Index (Zeilenbeschriftung) und Spaltennamen (Columns), die für den Datenzugriff und die Organisation verwendet werden.

# Pandas in Python: Zugriff und Manipulation von DataFrames

Pandas bietet umfangreiche Möglichkeiten, Daten in DataFrames zu organisieren, zu manipulieren und zu analysieren. Hier sind grundlegende Operationen und Methoden zur Arbeit mit DataFrames.

## Zugriff auf die Spaltennamen und den Index

```python
print("Spalten:", df.columns)
print("Index:", df.index)
```

### Festlegen eines benutzerdefinierten Index

Ein benutzerdefinierter Index kann festgelegt werden, um die Daten effizienter zu organisieren und zu durchsuchen.

```python
df.set_index('Name', inplace=True)
print("DataFrame mit benutzerdefiniertem Index:\n", df)
```

### Rückgängigmachen des benutzerdefinierten Index

```python
df.reset_index(inplace=True)
print("DataFrame mit zurückgesetztem Index:\n", df)
```


## Daten abfragen und ändern

Daten lassen sich über den Spaltennamen oder den Index abfragen und ändern.

### Zugriff auf eine Spalte

```python
print("Spalte 'Age':\n", df['Age'])
```

### Zugriff auf eine Zeile (mit `loc` für den Label-basierten Zugriff)

```python
print("Zeile mit Index 1:\n", df.loc[1])
```

### Zugriff auf mehrere Zeilen und Spalten

```python
print("Name und City für alle:\n", df[['Name', 'City']])
```

### Ändern eines Werts

```python
df.at[1, 'Age'] = 28
print("DataFrame nach Änderung von 'Age' für Bob:\n", df)
```


## Group By

`groupby()` wird verwendet, um Daten zu gruppieren und aggregierte Berechnungen durchzuführen.

### Beispiel: Gruppieren der Daten nach 'City' und Berechnung des Durchschnittsalters

```python
grouped = df.groupby('City')['Age'].mean()
print("Durchschnittsalter pro Stadt:\n", grouped)
```


##Pivot

Mit `pivot()` können Daten umstrukturiert werden, um Spalten- und Zeilenstrukturen anzupassen.

### Beispiel: Pivotieren des DataFrames

```python
data_pivot = {
    'Date': ['2024-01-01', '2024-01-02', '2024-01-01', '2024-01-02'],
    'City': ['Berlin', 'Berlin', 'Hamburg', 'Hamburg'],
    'Temperature': [5, 7, 6, 8]
}
df_pivot = pd.DataFrame(data_pivot)
pivot_df = df_pivot.pivot(index='Date', columns='City', values='Temperature')
print("Pivotierter DataFrame:\n", pivot_df)
```


## Transpose

Die `transpose()`-Methode dreht Zeilen und Spalten eines DataFrames.

### Transponieren eines DataFrames

```python
transposed_df = df.transpose()
print("Transponierter DataFrame:\n", transposed_df)
```


## Daten importieren

Daten können aus verschiedenen Dateiformaten wie CSV, Excel, SQL, usw. importiert werden.

### CSV-Datei importieren

```python
df = pd.read_csv('data.csv')
```

### Excel-Datei importieren

```python
# df = pd.read_excel('data.xlsx', sheet_name='Sheet1')
```


# Tabellenbereiche

Bei der Arbeit mit großen Dateien kann man bestimmte Tabellenbereiche importieren, um nur die benötigten Daten zu laden.

### Beispiel: Nur bestimmte Spalten laden

```python
df = pd.read_csv('data.csv', usecols=['Name', 'Age'])
```

### Beispiel: Nur eine bestimmte Anzahl Zeilen laden

```python
df = pd.read_csv('data.csv', nrows=10)
```


## Unbekannte Werte

Manchmal enthalten Daten fehlende Werte. Pandas kann diese Werte beim Importieren erkennen und verarbeiten.

### Beispiel: Fehlende Werte festlegen

```python
df = pd.read_csv('data.csv', na_values=['N/A', 'NA', '--'])$
```


## Daten exportieren

Nach der Bearbeitung können die Daten in verschiedene Formate exportiert werden, z.B. CSV, Excel, SQL.

### CSV-Datei exportieren

```python
df.to_csv('exported_data.csv', index=False)
```

### Excel-Datei exportieren

```python
df.to_excel('exported_data.xlsx', sheet_name='Sheet1', index=False)
```