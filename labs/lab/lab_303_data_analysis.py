import pandas as pd
from pathlib import Path
from typing import Union

def process_file(file_path: Path) -> pd.DataFrame:
    # Laden der CSV-Datei mit entsprechenden Spalten
    df = pd.read_csv(file_path, sep=';', skiprows=60, usecols=['HEART RATE (bpm)', 'SECONDS'])
    
    # Entfernen von Zeilen mit leeren Werten, inplace=True, um die Daten direkt zu aktualisieren
    df.dropna(axis=0, how='any',inplace=True)
    
    # Spalte für Minuten hinzufügen, um 60s-Intervalle zu erstellen
    df['MINUTE'] = (df['SECONDS'] // 60).astype(int)
    
    # Berechnen des Durchschnitts der Herzfrequenz pro Minute
    df_minute_avg = df.groupby('MINUTE')['HEART RATE (bpm)'].mean().reset_index()
    
        
    return df_minute_avg

def run(folder: Union[Path, str], export_file: Union[Path, str] = 'lab/export.xlsx') -> None:
    folder = Path(folder)
    export_file = Path(export_file)
    
    # Liste aller CSV-Dateien im Verzeichnis
    csv_files = folder.glob('*.csv')
    
    # Erstellen eines leeren DataFrames für alle Daten
    all_data = pd.DataFrame()
    
    # Verarbeitung jeder Datei und Anhängen an die Liste
    for file in csv_files:
        # Verarbeitung der Datei und Berechnung der Minuten-Durchschnittswerte
        minute_avg_row = process_file(file)
        
        # Hinzufügen des Dateinamens als Spalte
        minute_avg_row['FILENAME'] = file.stem
        
        # Pivotieren der Daten, um Minuten als Spalten zu haben
        pivot_df = minute_avg_row.pivot(index='FILENAME', columns='MINUTE', values='HEART RATE (bpm)')
        
        # Anhängen der Daten an das Gesamtergebnis
        all_data = pd.concat([all_data, pivot_df], axis=0)
    
    # Speichern der Ergebnisse als Excel-Datei
    all_data.to_excel(export_file)

if __name__ == '__main__':
    run('labs/lab/data/suunto')