# Pandas
Pandas ist eine leistungsstarke Open-Source-Bibliothek in Python, die speziell für die Datenmanipulation und -analyse entwickelt wurde. Sie bietet flexible und effiziente Datenstrukturen, die es ermöglichen, mit strukturierten und unstrukturierten Daten zu arbeiten, wie sie häufig in Tabellen, Datenbanken oder Zeitreihen vorkommen. 
## DatenFrame
Ein DataFrame ist eine zweidimensionale, tabellarische Datenstruktur, die aus Zeilen und Spalten besteht. Jede Spalte kann einen anderen Datentyp haben (z. B. Integer, Float, String). DataFrames sind ein wichtiger Bestandteil von Pandas und bieten viele eingebaute Funktionen zur Datenmanipulation.

### DataFrame erstellen
Mittels des Befehls **pd.dataFrame()** kann ein DataFrame erstellt werden.
```python
import pandas as pd

data = {
    'Name': ['Elena','Fabio','Ryandi'],
    'Sportart': ['Volleyball','Handball','Fussball'],
    'Punkte': [99, 69, 42]
 }    

df = pd.DataFrame(data)                             # hier wird mit den Daten des obigen Dictionarys ein DataFrame mit dem Namen "df" erstellt 
```

### Index und Column
Sowohl der Index als auch der Header können nach Bedarf definiert werden.
```python
import pandas as pd

data = {
    'Name': ['Elena','Fabio','Ryandi'],
    'Sportart': ['Volleyball','Handball','Fussball'],
    'Punkte': [99, 69, 42]
 }    

df = pd.DataFrame(data)

df = df.set_index('Name')           # hierbei wird die Spalte mit dem Header 'Name' als Index definiert

df = df.rename(columns={'Punkte': 'Punkte Total'})      # hier wird der Header der Spalte 'Punkte' neu definiert
```
### Daten abfragen und ändern
In Pandas können auf verschiedene Arten Daten abgefragt und verändern werden. Mit Methoden wie iloc[], loc[], und einfachen Bedingungen können Daten gefiltert, verändert und manipuliert werden. Dies ermöglicht eine effiziente Datenanalyse und -verarbeitung.
#### `iloc()`
Iloc ist eine Abkürzung für "Index Location" und beschreibt eine Funktion, mit der über die numerischen Indizes von Zeilen und Spalten auf ein bestimmtes Element innerhalb eines DataFrames zugegriffen wird.
```python
import pandas as pd

data = {
    'Name': ['Elena','Fabio','Ryandi'],
    'Sportart': ['Volleyball','Handball','Fussball'],
    'Punkte': [99, 69, 42]
 }    

df = pd.DataFrame(data)

spec_data = df.iloc[1,2]                    # spec_data = 70 in diesem Fall
```

#### `loc()`
Loc, ist eine Abkürzung für "Label Location" und wird ebenfalls verwendet, um spezifische Daten aus einem DataFrame zu extrahieren. Im Gegensatz zu iloc() basiert der Zugriff hier jedoch auf den benannten Spalten- oder Zeilenbezeichnern anstatt auf den numerischen Indizes.
```python
import pandas as pd

data = {
    'Name': ['Elena','Fabio','Ryandi'],
    'Sportart': ['Volleyball','Handball','Fussball'],
    'Punkte': [99, 69, 42]
 }    

df = pd.DataFrame(data)
df = df.set_index('Name')                   # damit auch der Zeilenindex mit alphabetischen Indices angesprochen werden kann, wird hier die Spalte 'Name' zum Index

spec_data = df.loc['Fabio','Punkte']                    # spec_data = 69 in diesem Fall
```
### Group By
Der `groupby()` Befehl dient dazu, Daten nach einem bestimmten Kriterium zu gruppieren. Dies ist besonders hilfreich, um beispielsweise Durchschnittswerte von verschiedenen Gruppen innerhalb eines Datensatzes zu berechnen.
```python
import pandas as pd

data = {
    'Name': ['Elena','Fabio','Ryandi'],
    'Sportart': ['Volleyball','Handball','Fussball'],
    'Punkte': [99, 69, 42]
 }    

df = pd.DataFrame(data)
df = df.set_index('Name')

punkteschnitte_sportart = df.groupby('Sportart')['Punkte'].mean()       # die Daten werden nach der Variable Sportart gruppiert. Anhand davon wird dann für jede Sportart der Punkteschnitt berechnet.
```
### Pivot
Die Pivot-Funktion `pivot()` ist eine Methode in Pandas, die es ermöglicht, ein DataFrame so zu transformieren, dass eine Spalte zu neuen Spalten wird, und die Daten anhand einer Index-Spalte neu organisiert werden. Dabei bleibt der ursprüngliche Datenrahmen intakt und es wird eine neue Ansicht auf die Daten erstellt.
```python
import pandas as pd

# Beispiel-DataFrame
data = {
    'Monat': ['Jan', 'Jan', 'Feb', 'Feb', 'Mär', 'Mär'],
    'Region': ['Nord', 'Süd', 'Nord', 'Süd', 'Nord', 'Süd'],
    'Verkäufe': [200, 150, 220, 180, 250, 190]
}

df = pd.DataFrame(data)

print(df)
```
### Transpose
Mit dem Befehl `transpose()`können Zeilen und Spalten getauscht werden.
```python
import pandas as pd

data = {
    'Name': ['Elena','Fabio','Ryandi'],
    'Sportart': ['Volleyball','Handball','Fussball'],
    'Punkte': [99, 69, 42]
 }    

df = pd.DataFrame(data)                
transposed_df = df.transpose

"""    
der "normale" DataFrame sieht wie folgt aus:
     Name  Sportart  Punkte
0    Elena  Volleyball    99
1    Fabio  Handball      69
2    Ryandi Fussball      42

der transponierte DataFrame sieht dann so aus:
            0         1         2
Name        Elena    Fabio      Ryandi
Sportart  Volleyball Handball  Fussball
Punkte        99       69      42
"""
```
## Daten importieren
Um mit in Pandas und Python erstellten Daten weiterzuarbeiten, können diese in ein DataFrame importiert werden. Pandas unterstützt das Einlesen von verschiedenen Dateiformaten. In diesem Beispiel konzentrieren wir uns jedoch auf das CSV-Format. Häufig ist es der Fall, dass die Daten aus der CSV-Datei nicht sofort ideal in das gewünschte DataFrame passen, sodass eine Anpassung erforderlich ist. Die read_csv-Funktion bietet hierfür zahlreiche Parameter, die an dieser Stelle jedoch nicht näher erklärt werden.
```python
import pandas as pd

importierte_daten = pd.read_csv('Pfad_zur_Datei')       # hier wird eine CSV Datei eingelesen und in ein DataFrame gespeichert
```
### Tabellenbereiche

### Unbekannte Werte
Verschiedene Methoden werden von Pandas zur Verfügung gestellt um mit umbekannten oder fehlenden Werten umzugehen. Zwei wichtige Befehle, die dabei verwendet werden, sind `dropna()` und `fillna()`. Der Befehl `dropna()` ermöglicht es, fehlende Werte aus den Daten zu entfernen. Mit `fillna()` können fehlende Werte durch von uns festgelegte Werte ersetzt werden.
```python
import pandas as pd
import numpy as np

    data = {
    'Name': ['Kurt','Alissa','Fiona'],
    'Sportart': ['Tennis','Fussball','Tennis'],
    'Punkte': [25, 70,np.nan]
}    

df = pd.DataFrame(data)
df = df.fillna(0)              # die unbekannten Daten werden durch eine 0 ersetzt hier

"""
Der hier generierte DataFrame würde wie folgt aussehen:
     Name  Sportart  Punkte
0    Elena    Volleyball    99.0
1  Fabio  Handball    69.0
2   Ryandi    Fussball     0.0

falls der Befehl df = df.dropna() verwendet werden würde, würde der df dann so aussehen:
     Name  Sportart  Punkte
0    Elena    Volleyball    99.0
1  Fabio  Handball    69.0
der fehlende Wert wurde mit samt der ganzen Zeile, in der er drinstand gedropt.
"""
```
## Daten exportieren
Exporte können in unterschiedlichen Dateiformaten erfolgen, auf die jedoch nicht alle im Detail eingegangen werden können. In diesem Zusammenhang werden die Befehle `DataFrame.to_csv()` und `DataFrame.to_excel()` erläutert.
Mit dem Befehl `DataFrame.to_excel()` kann ein DataFrame in eine Excel-Datei exportiert werden, wobei ebenfalls verschiedene Parameter genutzt werden können, um den Export anzupassen.
```python
import pandas as 
from pathlib import Path

data = {
    'Name': ['Elena','Fabio','Ryandi'],
    'Sportart': ['Volleyball','Handball','Fussball'],
    'Punkte': [99, 69, 42]
}    

df = pd.DataFrame(data)

pfad = Path('Pfad\zum\Dateispeicherort')

df.to_excel(pfad, index=True)       #mit index=True wird der im DataFrame vorhandene Index ebenfalls in die Excel-Datei übertragen
```