# Vergleich polars und pandas
`Polars` ist eine leistungsstarke DataFrame-Bibliothek für die Programmiersprache Rust, die auch Bindings für Python bietet. Sie wurde entwickelt, um die Verarbeitung großer Datenmengen effizienter und schneller zu gestalten. In diesem Bericht werden ein paar Grundlegende Funktionen vorgestellt und die Ausführungszeit mit der von `Pandas` verglichen.

## Warum könnte Polars besser geeignet sein als Pandas?

1. **Leistung**: `Polars` ist in Rust geschrieben, einer Systemsprache, die für ihre Geschwindigkeit und Effizienz bekannt ist. Dies führt zu einer schnelleren Datenverarbeitung im Vergleich zu `Pandas`, das in Python geschrieben ist.
2. **Speichereffizienz**: `Polars` verwendet speichereffiziente Algorithmen und Datenstrukturen, was zu einem geringeren Speicherverbrauch führt.
3. **Parallelverarbeitung**: `Polars` unterstützt die parallele Verarbeitung von Daten, was die Leistung auf modernen Mehrkernprozessoren weiter verbessert.
4. **API-Design**: `Polars` bietet eine intuitive und benutzerfreundliche API, die sich an der von `Pandas` orientiert, aber zusätzliche Funktionen und Optimierungen bietet.

## Grundlegende Operationen
Beide Packages können über `pip` installiert werden.
**Installation mit pip**
```cmd
pip install pandas
pip install polars
```
**Importieren der Packages**
```Python
import pandas as pd
import polars as pl
```

**Erstellen eines DataFrames**
```Python
# pandas
df_pandas = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [24, 27, 22]
})

# polars
df_polars = pl.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [24, 27, 22]
})
```
**Importieren einer existierenden Datei:**
CSV:
```Python
# pandas
df_pandas = pd.read_csv('sample.csv')

# polars
df_polars = pl.read_csv('sample.csv')
```

EXCEL:
```Python
# pandas
df_pandas = pd.read_excel('sample.xlsx')

# polars
df_polars = pl.read_excel('sample.xlsx')

```

JSON:
```Python
# pandas
df_pandas = pd.read_json('sample.json')

# polars
df_polars = pl.read_json('sample.json')
```

**Speichern des Dataframes**

Speichern als CSV
```Python
# pandas
df_pandas.to_csv('output.csv', index=False)

# polars
df_polars.write_csv('output.csv')
```

Speichern als Excel
```Python
# pandas
df_pandas.to_excel('output.xlsx', index=False)

# polars
df_polars.write_excel('output.xlsx')
```

Speichern als JSON
```Python
# pandas
df_pandas.to_json('output.json', orient='records')

# polars
df_polars.write_json('output.json')
```

**Grundlegende Operationen und Vergleiche**

Filtern
```Python
# pandas
filtered_pandas = df_pandas[df_pandas['Age'] > 25]

# polars
filtered_polars = df_polars.filter(pl.col('Age') > 25)
```


**Gruppierung**
```Python
# pandas
grouped_pandas = df_pandas.groupby('Age').size()

# polars
grouped_polars = df_polars.group_by('Age').count()
```
**Aggregatsfunktion**
```Python

# pandas
mean_age_pandas = df_pandas['Age'].mean()
min_age_pandas = df_pandas['Age'].min()
max_age_pandas = df_pandas['Age'].max()

# polars
mean_age_polars = df_polars.select(pl.col('Age').mean()).item()
min_age_polars = df_polars.select(pl.col('Age').min()).item()
max_age_polars = df_polars.select(pl.col('Age').max()).item()

```
**Between**
```Python
# pandas
between_pandas = df_pandas[df_pandas['Age'].between(23, 26)]

# polars
between_polars = df_polars.filter(pl.col('Age').is_between(23, 26))
```

**Join**
```Python

# pandas
df1_pandas = pd.DataFrame({'key': ['A', 'B', 'C'], 'value1': [1, 2, 3]})
df2_pandas = pd.DataFrame({'key': ['A', 'B', 'D'], 'value2': [4, 5, 6]})
joined_pandas = pd.merge(df1_pandas, df2_pandas, on='key', how='inner')

# polars
df1_polars = pl.DataFrame({'key': ['A', 'B', 'C'], 'value1': [1, 2, 3]})
df2_polars = pl.DataFrame({'key': ['A', 'B', 'D'], 'value2': [4, 5, 6]})
joined_polars = df1_polars.join(df2_polars, on='key', how='inner')

```
## Arbeitsaufträge
### Auftrag 1
Im Ordner `code/Abschlussbericht/sample_data` sind verschieden grosse Datensätze mit der Herzfrequenz (`heart_rate`) von Athleten zu einem Zeitstempel (`time`) in Ruhe, beim Aufwärmen und während einem Hauptteil (`activity`) gespeichert. Es sollen die Dateien von `athlete_1` und `athlete_2` als Dataframe importiert, die beiden zusammengefügt und anschliessend Ausreisser der Herzfrequenzen herausgefiltert werden. Anschliessend soll die Durchschnittliche HF für beide Athleten für jede Aktivität berechnet werden. Zum Schluss soll das gefilterte Dataframe als csv-Datei gespeichert werden.

Implementiere dazu die nötigen Methoden im File `hf_pandas_vs_polars.py` (für pandas und für polars). 

## Auftrag 2
Nun sollen die Zeiten für verschiedene Funktionalitäten der beiden Packages verglichen werden. Führe dazu das File `hf_pandas_vs_polars.py` für die verschiedenen samples aus und beantworte die folgenden Fragen.

### Hat die Grösse des Datensatzes einen Einfluss auf das Geschwindigkeitsverhältnis zwischen den beiden Packages?

 

### Welche Funktionen sind in polars optimiert?



### Wieso könnte das sein?
