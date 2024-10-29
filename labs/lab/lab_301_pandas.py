import numpy as np
import pandas as pd
from pathlib import Path

def experiment_setup(xlsx_path):
    # Definierte Datenstruktur ähnlich wie in deinem Beispiel
    data = {
        'vpn01': {
            'Gruppe': 'A',
            'Trial_01': 'vid_01.mp4',
            'Trial_02': 'vid_02.mp4',
            'Trial_03': 'vid_03.mp4',
            'Trial_04': 'vid_04.mp4'
        },
        'vpn02': {
            'Gruppe': 'B',
            'Trial_01': 'vid_03.mp4',
            'Trial_02': 'vid_04.mp4',
            'Trial_03': 'vid_01.mp4',
            'Trial_04': 'vid_02.mp4'
        }
    }
    
    # Konvertiere die Daten in ein DataFrame
    df = pd.DataFrame(data)
    
    # Transponiere das DataFrame, um die Struktur wie gefordert darzustellen
    df_transposed = df.transpose()
    
    # Exportiere das DataFrame als Excel-Datei
    df_transposed.to_excel(xlsx_path, index=True)


def load_relevant_data(file_name):
    # Liest die CSV-Datei ein und filtert relevante Spalten
    df = pd.read_csv('labs/lab/data/lab301_sport/data.csv',
        sep=';',  # Semikolon als Trennzeichen
        skiprows=3,  # Überspringt die ersten 2 Zeilen
        usecols=[0, 1, 2, 5],  # Verwendet nur die Spalten für country, height, weight und main sport
        names=['country', 'height', 'weight', 'sport'],  # Definierte Spaltennamen
        na_values=['UNKNOWN']  # 'UNKNOWN' wird als NaN behandelt
    ).dropna(axis=0, how='any')  # Entfernt Zeilen mit mindestens einem NaN-Wert
    return df


if __name__ == '__main__':
    # Führt die experiment_setup Funktion aus und speichert das Ergebnis
    df_experiment = experiment_setup('input.xlsx')
    
    # Führt die load_relevant_data Funktion aus und speichert das Ergebnis
    df_relevant = load_relevant_data('labs/lab/data/lab301_sport/data.csv')
    
