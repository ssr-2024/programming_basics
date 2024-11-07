from typing import Union
from pathlib import Path
import pandas as pd


def process_csv_file(file_path: Path) -> pd.DataFrame:
    """Liest eine CSV-Datei, bereinigt sie und berechnet die durchschnittliche Herzfrequenz pro Minute.

    Parameters
    ----------
    file_path : Path
        Pfad zur CSV-Datei.

    Returns
    -------
    pd.DataFrame
        DataFrame mit durchschnittlicher Herzfrequenz pro Minute.
    """
    # Lädt die CSV-Datei und wählt relevante Spalten aus
    df = pd.read_csv(file_path, sep=';', skiprows=60, usecols=['HEART RATE (bpm)', 'SECONDS'])

    # Entfernt Zeilen mit fehlenden Werten
    df = df.dropna(axis=0, how='any')

    # Berechnet die Minutenangabe basierend auf den Sekunden
    df['MINUTES'] = df['SECONDS'] // 60

    # Berechnet den Durchschnitt der Herzfrequenz pro Minute
    minute_avg = df.groupby('MINUTES')['HEART RATE (bpm)'].mean().reset_index()

    return minute_avg


def aggregate_folder_data(folder_path: Union[Path, str], export_file: Union[Path, str] = 'labs/lab/export.xlsx') -> None:
    """Aggregiert die Daten mehrerer CSV-Dateien in einem Ordner und exportiert das Ergebnis als Excel-Datei.

    Parameters
    ----------
    folder_path : Union[Path, str]
        Pfad zum Ordner mit den CSV-Dateien.
    export_file : Union[Path, str], optional
        Pfad zur Ausgabedatei (Standard: 'labs/lab/export.xlsx').

    Returns
    -------
    None
    """
    folder_path = Path(folder_path)
    combined_data = pd.DataFrame()  # Initialisiert das DataFrame für die aggregierten Daten

    # Durchläuft alle Dateien im Ordner
    for file in folder_path.iterdir():
        if file.suffix == '.csv':  # Prüft, ob die Datei eine CSV ist
            # Verarbeitet die CSV-Datei und berechnet den durchschnittlichen Herzschlag pro Minute
            minute_avg = process_csv_file(file)

            # Fügt den Dateinamen als Spalte hinzu
            minute_avg['FILENAME'] = file.stem

            # Pivotiert das DataFrame, um Minuten als Spalten und Dateinamen als Zeilen anzuzeigen
            pivot_df = minute_avg.pivot(index='FILENAME', columns='MINUTES', values='HEART RATE (bpm)')

            # Fügt die Daten zum kombinierten DataFrame hinzu
            combined_data = pd.concat([combined_data, pivot_df], axis=0)

    # Exportiert die aggregierten Daten in eine Excel-Datei
    combined_data.to_excel(export_file)

    return None


def run(folder_path: Union[Path, str], export_file: Union[Path, str]) -> None:
    """Wrapper function to call aggregate_folder_data."""
    aggregate_folder_data(folder_path, export_file)


if __name__ == '__main__':
    run('labs/lab/data/suunto')
