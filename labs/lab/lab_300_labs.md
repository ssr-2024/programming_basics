# Übungen Termin 5

## [lab_301_pandas](lab_301_pandas.py)

### Excel export

Folgendes Experiment Setup soll in Python erstellt und als **Excel-Tabelle** exportiert werden.

|       | Gruppe | Trial_01   | Trial_02   | Trial_03   | Trial_04   |
| :---- | :----- | :--------- | :--------- | :--------- | :--------- |
| vpn01 | A      | vid_01.mp4 | vid_02.mp4 | vid_03.mp4 | vid_04.mp4 |
| vpn02 | B      | vid_03.mp4 | vid_04.mp4 | vid_01.mp4 | vid_02.mp4 |

Implementiere dazu die Funktion `experiment_setup(xlsx_path)`. Das Excel soll an den `xlsx_path` abgespeichert werden.

Achtung, die Einträge müssen **exakt** stimmen!

#### Tipps

```py
data = {
    'random_1_4': {
        'range': [1, 4],
        'random1': 3,
        'random2': 2,
        'random3': 3
    },
    'random_1_100': {
        'range': [1, 100],
        'random1': 69,
        'random2': 77,
        'random3': 13
    }
}
```

- Wird obenstehendes `dict` in ein `DataFrame` übersetzt (`pd.DataFrame(data)`) und zu einem Excel exportiert, entsteht folgende Ausgabe:

|         | random_1_4 | random_1_100 |
| :------ | :--------- | :----------- |
| range   | [1, 4]     | [1, 100]     |
| random1 | 3          | 69           |
| random2 | 2          | 77           |
| random3 | 3          | 13           |

- Mit der Funktion `df.transpose()` können die Spalten und Zeilen getauscht werden:

|             | range   | random1 | random2 | random3 |
| :---------- | :------ | :------ | :------ | :------ |
| range_1_4   | [1,4]   | 3       | 2       | 3       |
| range_1_100 | [1,100] | 69      | 77      | 13      |

### Daten einlesen

Der Datensatz [lab301_sport/data.csv](data/lab301_sport/data.csv) soll eingelesen und aufbereitet werden:

- Es interessieren nur die Spalten `country code`, `height [cm]`, `weight [kg]` und `main sport`
- Die Spalten sollen im Datenframe `country`, `height`, `weight` und `sport` heissen
- `UNKNOWN` Werte sollen als `NaN` eingelesen werden
- Zeilen mit mindestens einem `NaN` sollen gelöscht werden

Implementiere die Funktion `load_relevant_data(file_name)`, welche den DAtensatz einliest, bereinigt und dann zurückgibt (`return` ist also ein `DataFrame`).

[Nützliche Quelle](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html)

## [lab_302_pathlib](lab_302_pathlib.py)

Implementiere die beiden Funktionen `vpns_exp01` und `vpns_exp02` anhand der folgenden docstrings:

### `vpns_exp01`

````py
def vpns_exp01():
    """
    Returns a dictionary containing the experiment setup based on
    all CSV files in the provided path.

    CSV files nested in subfolders are ignored.
    The names are derived from the CSV file names.

    Parameters
    ----------
    path : str, optional
        path to the experiment folder, by default 'lab/data/exp01'

    Returns
    -------
    dict
        the exp setup dict{ str : Path }

    Examples
    --------
    expect the following folder structure:

    lab/data/exp01/
             ├───vpn_01.csv
             └───vpn_02.csv

    ```py
    >>> vpns_exp01('lab/data/exp01')

    {
        'vpn_01': Path(lab/data/vpn_01.csv),
        'vpn_02': Path(lab/data/vpn_02.csv)
    }
    ```
    """
````

### `vpns_exp02`

````py

def vpns_exp02():
    """
    Returns a dictionary containing the experiment setup based on
    the folder structure of the provided path and the containing CSV files.


    CSV files located elsewhere than in the vpn folders are ignored.
    The vpn names are derived from the folder names.
    The mzp is derived from the last 2 characters of the CSV file name: e.g. mzp_14.csv => 14

    Parameters
    ----------
    path : str, optional
        path to the experiment folder, by default 'lab/data/exp02'

    Returns
    -------
    dict
        the exp setup dict{ str : dict{ int : Path } }

    Examples
    --------
    expect the following folder structure:

    lab/data/exp02/
             ├───vpn_01/
             │   ├───mzp_01.csv
             │   ├───mzp_02.csv
             │   ├───mzp_03.csv
             │   └───mzp_04.csv
             └───vpn_02/
                 ├───mzp_01.csv
                 ├───mzp_02.csv
                 ├───mzp_03.csv
                 └───mzp_04.csv
    ```py
    >>> vpns_exp02('lab/data/exp02')
    {
        'vpn_01': {
            1: Path(lab/data/vpn_01/mzp_01.csv),
            2: Path(lab/data/vpn_01/mzp_02.csv),
            3: Path(lab/data/vpn_01/mzp_03.csv),
            4: Path(lab/data/vpn_01/mzp_04.csv)
        },
        'vpn_02': {
            1: Path(lab/data/vpn_02/mzp_01.csv),
            2: Path(lab/data/vpn_02/mzp_02.csv),
            3: Path(lab/data/vpn_02/mzp_03.csv),
            4: Path(lab/data/vpn_02/mzp_04.csv)
        }
    }
    ```
    """
````

# [lab_303_data_analysis.py](lab_303_data_analysis.py)

Für eine Studie zum Einfluss von körperlicher Aktivität auf die Kognition werden für die Überprüfung der körperlichen Aktivität Pulsuhren von Suunto eingesetzt.
Das Fileformat ist für diese Studie immer gleich aufgebaut:

- Informationen zu der Uhreinstellung und zusammengefasste Ergebnisse
- Beschreibung der _13_ Messwerte (Header)
- Für jeden Messzeitpunkt eine Zeile

Jede Datei ist über den Dateinamen zu einer VPN zugeordnet. Die Abtastrate der Uhren liegt bei `2s`, für die Auswertung möchten wir aber eine Abtastrate von `60s`.

## Ziel

Alle Daten im Ordner [suunto](data/suunto) sollen so prozessiert, dass immer der Minutendurchschnitt berechnet und in ein Excel geschrieben wird, so dass folgender Output entsteht:

|      | 0     | 1     | 2    | ... | 91   | 92    | 93    |
| :--- | :---- | :---- | :--- | :-- | :--- | :---- | :---- |
| 31_1 | 90.2  | 80.33 | 78.1 | ... | 81.3 | 78.26 | 86.71 |
| 31_2 | 75.16 | 71.5  | 77.4 | ... |      |       |       |
| ...  |       |       |      |     |      |       |       |

## Vor dem Programmieren...

Überlege dir, wie du eine ein Spalte hinzufügen kannst, in welcher der Zeitwert als Minute gespeichert ist.

| SECONDS | Minute |
| ------: | -----: |
|     `0` |    `0` |
|     `2` |    `0` |
|     ... |    ... |
|    `58` |    `0` |
|    `60` |    `1` |
|    `62` |    `1` |
|     ... |    ... |
|   `118` |    `1` |
|   `120` |    `2` |
|     ... |    ... |
|   `178` |    `2` |
|   `180` |    `3` |
|     ... |    ... |

**Tipp**: mit `int()` kann einfach abgerundet werden, also `int(2.9)` ergibt `2`.

**Advanced**: mit dem Operator `//` kann eine Integer-Division gemacht werden, also `5 // 2` entspricht `int(5 / 2)` und ergibt `2`.

## Vorgehen

Es braucht mehrere Schritte um die Daten auszuwerten:

- Prototyp der Auswertung für eine Datei schreiben
  - gewünschter Bereich der `.csv`-Datei (Puls und Zeit) als `DataFrame` laden
  - Zeilen mit leere Werten löschen (vgl. `dropna()` für DataFrames)
  - Spalte für Gruppierungsmerkmal `minutes` hinzufügen
  - Gruppieren und die Mittelwerte des Pulses berechnen
  - Excel Zusammenfassung exportieren
- Generalisieren
  - Alle `.csv`-Dateinamen im Ordner `lab/data/suunto` abfragen
  - alle Dateien prozessieren und die Resultate zu einem `DataFrame` zusammenfügen
- Daten exportieren
  - Resultate-DataFrame als `.xlsx` exportieren

## Aufbau der Datenauswertung

Die ganze Datenauswertung soll in Gang gesetzt werden, wenn die Funktion `run(folder_dir, export_file)` aufgerufen wird.

`folder_dir` gibt dabei an, wo sich der Ordner mit den Daten befindet.

`export_file` gibt den Pfad zur Excel-Datei an, die exportiert wird.
