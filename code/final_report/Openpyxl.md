# Openpyxl 

Das Python-Paket **openpyxl** bietet eine vielseitige Möglichkeit, programmgesteuert mit Excel-Dateien (.xlsx) zu arbeiten. Es ist besonders nützlich für die Automatisierung von Aufgaben wie das Einfügen, Bearbeiten und Analysieren von Daten, das Formatieren von Zellen oder das Erstellen von Diagrammen. Dieses Tutorial bietet eine Einführung in die wichtigsten Funktionen von openpyxl, um dir den Einstieg in die Arbeit mit Excel-Dateien zu erleichtern.

### Inhaltsverzeichnis

1. [Einführung in openpyxl](#openpyxl)
   - [Praktische Relevanz](#praktische-relevanz)
   - [Ziele des Tutorials](#tutorial-einstieg-in-openpyxl-für-die-arbeit-mit-excel-dateien-in-python)
2. [Installation](#1-installation)
3. [Grundlegende Operationen](#2-grundlegende-operationen)
    - [Neue Excel-Datei erstellen](#21-eine-neue-excel-datei-erstellen)
    - [Bestehende Excel-Datei öffnen](#22-eine-bestehende-excel-datei-öffnen)
   - [Arbeitsblätter verwalten](#23-arbeitsblätter-verwalten)
   - [Maximale Zeilen und Spalten bestimmen](#24-maximale-zeilen-und-spalten-bestimmen)
   - [Daten iterieren](#25-daten-iterieren)
   - [Spalten dynamisch finden](#27-spalten-dynamisch-finden)
4. [Daten mit Schleifen einfügen](#3-daten-mit-schleifen-einfügen)
5. [Zellen formatieren](#4-zellen-formatieren)
6. [Mit Formeln arbeiten](#5-mit-formeln-arbeiten)
7. [Diagramme erstellen](#6-diagramme-erstellen)
8. [Übungsaufgaben](#übungsaufgaben)
   - [Aufgabe 1: Daten nach Vereinsnamen sortieren](#aufgabe-1)
   - [Aufgabe 2: Datenaufbereitung und Diagramme](#aufgabe-2)

## Praktische Relevanz
Das **openpyxl**-Paket ist äusserst relevant, wenn es darum geht, Excel-Dateien effizient und automatisiert zu bearbeiten. Es ermöglicht, wiederkehrende Aufgaben wie das Einfügen von Daten, das Formatieren von Zellen oder das Erstellen von Diagrammen zu automatisieren, was Zeit und manuelle Arbeit spart. 

## Tutorial: Einstieg in **openpyxl** für die Arbeit mit Excel-Dateien in Python

Mit **openpyxl** kannst du Microsoft Excel-Dateien (\*.xlsx) erstellen, bearbeiten und analysieren. Es ist besonders praktisch, wenn du programmgesteuert mit Excel-Dateien arbeiten möchtest. In diesem Tutorial lernst du die grundlegenden Funktionen von **openpyxl** kennen.

---

#### **1. Installation**
Installiere das Paket zunaechst mit `pip`:
```bash
pip install openpyxl
```
---
#### **2. Grundlegende Operationen**

##### **2.1 Eine neue Excel-Datei erstellen**
Mit **openpyxl** kannst du ganz einfach eine neue Excel-Arbeitsmappe erstellen:
```python
import openpyxl as px

# Eine neue Arbeitsmappe erstellen
workbook = px.Workbook()

# Auf das Standard-Arbeitsblatt zugreifen
sheet = workbook.active
sheet.title = "Meine Daten"

# Daten in Zellen schreiben
sheet["A1"] = "Name"
sheet["B1"] = "Alter"
sheet["A2"] = "Elias"
sheet["B2"] = 24

# Die Datei speichern
workbook.save("neue_datei.xlsx")
```
---
##### **2.2 Eine bestehende Excel-Datei öffnen**
Du kannst auch bestehende Excel-Dateien öffnen:
```python
import openpyxl as px

# Eine Arbeitsmappe laden
workbook = px.load_workbook("neue_datei.xlsx")

# Auf ein Arbeitsblatt zugreifen
sheet = workbook.active  

# Daten auslesen
print(sheet["A1"].value)  # Name
print(sheet["B2"].value)  # 24
```
Hier ist ein zusätzliches Beispiel, bei dem das `pathlib`-Modul verwendet wird, um den Pfad zur Excel-Datei zu verwalten und diese dann mit `openpyxl` zu öffnen:

```python
import openpyxl as px
from pathlib import Path

# Den Pfad zur Excel-Datei mit Pathlib erstellen
datei_pfad = Path("neue_datei.xlsx")

# Eine Arbeitsmappe laden
workbook = px.load_workbook(datei_pfad)

# Auf ein Arbeitsblatt zugreifen
sheet = workbook.active

# Daten auslesen
print(sheet["A1"].value)  # Name
print(sheet["B2"].value)  # 24
```
---

##### **2.3 Arbeitsblätter verwalten**
Mit **openpyxl** kannst du Arbeitsblätter hinzufügen, umbenennen oder löschen:
```python
import openpyxl as px

# Eine Arbeitsmappe laden
workbook = px.load_workbook("neue_datei.xlsx")

# Ein neues Arbeitsblatt hinzufügen
workbook.create_sheet(title="Zusatzdaten")

# Ein Arbeitsblatt umbenennen
sheet = workbook["Zusatzdaten"]
sheet.title = "Weitere Daten"

# Ein Arbeitsblatt löschen
del workbook["Weitere Daten"]

# Die Arbeitsmappe speichern
workbook.save("neue_datei.xlsx")
```
---

##### **2.4 Maximale Zeilen und Spalten bestimmen**
Um Daten aus einem Arbeitsblatt dynamisch auszulesen oder zu verarbeiten, ist es oft nützlich, die Anzahl der verwendeten Zeilen und Spalten zu kennen:
```python
import openpyxl as px

# Eine Arbeitsmappe laden
workbook = px.load_workbook("neue_datei.xlsx")
sheet = workbook.active

# Maximale Zeilen und Spalten bestimmen
max_row = sheet.max_row
max_col = sheet.max_column
```
---

##### **2.5 Daten iterieren**
Wenn du Daten aus mehreren Zeilen oder Spalten verarbeiten möchtest, kannst du mit Schleifen durch das Arbeitsblatt iterieren:
```python
import openpyxl as px

# Eine Arbeitsmappe laden
workbook = px.load_workbook("neue_datei.xlsx")
sheet = workbook.active

# Durch alle Zeilen iterieren und Spalten auslesen
for row in sheet.iter_rows(min_row=2, max_row=sheet.max_row, min_col=1, max_col=sheet.max_column):
    for cell in row:
        print(cell.value)
```
---

##### **2.7 Spalten dynamisch finden**
Um bestimmte Spalten basierend auf deren Namen zu identifizieren, kannst du wie folgt vorgehen:
```python
import openpyxl as px

# Eine Arbeitsmappe laden
workbook = px.load_workbook("neue_datei.xlsx")
sheet = workbook.active

# Ermitteln der Spaltennamen aus der Kopfzeile
header = [cell.value for cell in sheet[1]]  # Werte der ersten Zeile

# Spalten mit bestimmten Präfixen finden
target_columns = []  
for col_idx, col_name in enumerate(header, start=1):  # 
    if col_name and col_name.startswith("Zufriedenheit_"):  # Überprüfe, ob der Spaltenname existiert und mit "Zufriedenheit_" beginnt
        target_columns.append((col_name, px.utils.get_column_letter(col_idx)))  # Füge den Spaltennamen und den entsprechenden Spaltenbuchstaben zur Liste hinzu

print("Gefundene Spalten beginnend mit Zufriedenheit_:", target_columns)
```
---

#### **3. Daten mit Schleifen einfügen**
Oft möchtest du Daten dynamisch hinzufügen. Mit Schleifen kannst du dies effizient umsetzen:
```python
import openpyxl as px

# Eine Arbeitsmappe laden
workbook = px.load_workbook("neue_datei.xlsx")
sheet = workbook.active

# Beispiel: Mehrere Zeilen einfügen
data = [
    ["Name", "Alter", "Stadt"],
    ["Anna", 30, "Berlin"],
    ["Ben", 28, "Muenchen"],
    ["Carla", 35, "Hamburg"]
]
# Daten zeilenweise hinzufuegen
for row in data:
    sheet.append(row)
# Speichern
workbook.save("neue_datei.xlsx")
```
---

#### **4. Zellen formatieren**
Mit **openpyxl** kannst du die Formatierung von Zellen ändern:
```python
import openpyxl as px
from openpyxl.styles import Font, Alignment

# Eine Arbeitsmappe laden
workbook = px.load_workbook("neue_datei.xlsx")
sheet = workbook.active

# Schriftart ändern
bold_font = Font(bold=True)
sheet["A1"].font = bold_font

# Zellen ausrichten
center_alignment = Alignment(horizontal="center")
sheet["A1"].alignment = center_alignment

# Speichern
workbook.save("neue_datei.xlsx")
```
---

#### **5. Mit Formeln arbeiten**
Du kannst Excel-Formeln hinzufügen, die in Excel automatisch berechnet werden:
```python
import openpyxl as px

# Eine Arbeitsmappe laden
workbook = px.load_workbook("neue_datei.xlsx")
sheet = workbook.active

# Formel hinzufügen
sheet["C1"] = "Summe"
sheet["C2"] = "=SUM(B2:B4)"  # Excel-Formel

# Speichern
workbook.save("neue_datei.xlsx")
```
---

#### **6. Diagramme erstellen**
Mit **openpyxl** kannst du Diagramme hinzufügen, um deine Daten zu visualisieren. Weitere Informationen findest du unter dem [Link](https://openpyxl.readthedocs.io/en/3.1/charts/bar.html).
```python
import openpyxl as px
from openpyxl.chart import BarChart, Reference

# Eine Arbeitsmappe laden
workbook = px.load_workbook("neue_datei.xlsx")
sheet = workbook.active

# Datenbereich für das Diagramm definieren
values = Reference(sheet, min_col=2, min_row=2, max_col=2, max_row=4)

# Ein Balkendiagramm erstellen
chart = BarChart()
chart.add_data(values, titles_from_data=True)

# Diagramm auf das Arbeitsblatt setzen
sheet.add_chart(chart, "E2")

# Speichern
workbook.save("neue_datei.xlsx")
```

---

## Übungsaufgaben

Der Schweizerische Fussballverband (SFV) hat bei ausgewählten Vereinen eine Mitgliederumfrage durchgeführt und erwartet nun von dir eine professionelle Datenaufbereitung. Deine Aufgabe ist es, die Ergebnisse so zu strukturieren, dass sie leicht ausgewertet werden können. Dabei kommt es besonders darauf an, die Daten nachvollziehbar und übersichtlich in einer bearbeiteten Excel-Datei darzustellen. Die Vereinsfunktionäre zählen auf deine Unterstützung – also los geht’s! 

### Aufgabe 1

Schreibe ein Python-Skript, das die Excel-Datei **"Beispieldaten_Tutorial.xlsx"** verarbeitet und die Daten nach Vereinsnamen sortiert. Lies zunächst die Datei ein und benenne das Haupt-Arbeitsblatt in **"Gesamtdaten"** um. Erstelle dann für jeden Verein ein eigenes Arbeitsblatt mit den dazugehörigen Daten. Zum Schluss speicherst du die Datei unter dem Namen **"Beispieldaten_Ergebnis"** als neue Excel-Datei ab.

Du kannst das nachfolgende Template ergänzen oder ein neues .py File mit den entsprechenden Schritten erstellen. Sei kreativ bei der Umsetzung und sorge dafür, dass das Ergebnis klar und nachvollziehbar ist – der SFV wird es dir danken!

```python
# Step 1: Import the necessary libraries
import openpyxl as px
from pathlib import Path

# Step 2: Define the paths to the input and output files
input_path = 
output_path = 

# Step 3: Load the workbook and select the active worksheet


# Step 4: Rename the active worksheet to "Gesamtdaten"


# Step 5: Define the column to evaluate (club names)
verein_spalte =
max_col =
max_row =

# List of known clubs
known_clubs = [
    "FC Alle", "FC Attiswil", "FC Azzurri Bienne", "FC Bremgarten", "FC Bülach", 
    "FC Celerina", "FC Dielsdorf", "FC Erguël", "FC Frenkendorf", "FC Frutigen", 
    "FC La Combe", "FC Lutry", "FC Münchwilen", "FC Münsingen", "FC Muri", 
    "FC Sarine-Ouest", "FC Savièse", "FC Volketswil", "FC Wallisellen", 
    "FC Wetzikon", "FFV Basel", "SC Cham", "SC Düdingen"
]

# Collect data per club
vereinsdaten = {club: [] for club in known_clubs}
for row in range(2, max_row + 1):
    verein = sheet.cell(row=row, column=verein_spalte).value
    if verein in vereinsdaten:
        # Collect all data in the row for the club
        vereinsdaten[verein].append([sheet.cell(row=row, column=col).value for col in range(1, max_col + 1)])

# Step 6: Create a new worksheet for each club
for verein, daten in vereinsdaten.items():
    # Create a new sheet with the club name 
    
    # Copy the header
    

    # Insert the data
    

# Step 7: Save the workbook


print(f"Ergebnisdatei gespeichert unter: {output_path}")

````

### Aufgabe 2
Nachdem die Daten erfolgreich nach Vereinen sortiert und in separate Arbeitsblätter aufgeteilt wurden, möchte der SFV die Ergebnisse weiter verfeinern und visuell aufbereiten.

Deine Aufgabe ist es, in jedem Arbeitsblatt die Durchschnittswerte für alle Spalten zu berechnen, die mit "Zufriedenheit_" oder "Wichtigkeit_" beginnen. Diese Werte sollen am Ende jeder Spalte eingetragen werden, damit die Auswertung klar und strukturiert bleibt. Ausserdem erwartet der SFV, dass du die Ergebnisse anschaulich visualisierst. Erstelle dazu pro Arbeitsblatt zwei Balkendiagramme: eines für die Durchschnittswerte der Zufriedenheit-Spalten und eines für die Wichtigkeit-Spalten. Platziere die Diagramme direkt unter den Daten, sodass sie die wichtigsten Erkenntnisse auf einen Blick vermitteln. Speichere die fertige Datei unter dem Namen "**Beispieldaten_Ergebnis_mit_Durchschnitt und Balkendiagrammen**" als neue Excel-Datei ab. 

Du kannst wiederum das nachfolgende Template ergänzen oder ein neues .py File mit den entsprechenden Schritten erstellen.

```python
# Step 1: Import the necessary libraries
import openpyxl as px
from openpyxl.chart import BarChart, Reference, Series
from pathlib import Path

# Step 2: Define the path to the input file
input_path = 
output_path =

# Step 3: Load the workbook


# Step 4: Iterate through all sheets in the workbook
for sheet_name in workbook.sheetnames:
    sheet = workbook[sheet_name]

    # Find columns that start with "Zufriedenheit_" or "Wichtigkeit_"
    zufriedenheit_columns = 
    wichtigkeit_columns = 
    header = [cell.value for cell in sheet[1]]

    for col_idx, col_name in enumerate(header, start=1):
        if 
            
        elif 
            

    # Get the maximum row number
    

    # Iterate through the specified columns to calculate averages
    for col_name, col_letter in zufriedenheit_columns + wichtigkeit_columns:
        col_index = px.utils.column_index_from_string(col_letter)
        values = []
        for row in range(2, max_row + 1):
            cell_value = sheet.cell(row=row, column=col_index).value
            if cell_value is not None:
                try:
                    values.append(float(cell_value))
                except ValueError:
                    continue

        # Step 5: Calculate the average if there are values
       

    # Step 6: Function to create a bar chart
   







        for col_name, col_letter in columns:
            # Use the last value in each column for the chart
            data = Reference(sheet, min_col=px.utils.column_index_from_strin (col_letter), min_row=max_row + 1, max_row=max_row + 1)
            series = Series(data, title=col_name)  
            # Use column names as legend titles
            chart.series.append(series)
            chart.set_categories(Reference(sheet, min_col=px.utils.column_index_from_string(col_letter), min_row=1, max_row=1))
           
        # Place the chart on the sheet
        sheet.add_chart(chart, position)

    # Step 7: Create charts for "Zufriedenheit" and "Wichtigkeit"
    

# Step 8: Save the workbook with the charts and averages


print(f"Zweite Ergebnisdatei gespeichert unter: {output_path}. Herzliche Gratulation. Du hast nun beide Übungsaufgaben gelöst.")

```
Hinweis: die generierten Balkendiagramme dienen als Übersicht. Man kann schnell sehen, wo die Mitglieder (un)zufrieden sind oder was ihnen besonders wichtig ist. Klicke hierfür einfach auf die Balken und es wird dir angezeigt, welcher Aspekt gemeint ist.
