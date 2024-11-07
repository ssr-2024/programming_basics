import numpy as np
import pandas as pd
from pathlib import Path

def experiment_setup(xlsx_path: str)->None:
    """Erstellt ein Experiment-Setup und speichert es als Excel-Datei.

    Parameters
    ----------
    output_path : str
        Der Dateipfad, unter dem das Setup als Excel-Datei gespeichert wird.

    Returns
    -------
    None
    """
    # Daten für das Experiment definieren, die jede Versuchsperson und ihre Gruppen-/Trial-Zuweisung enthalten
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
    
    # Erstellt ein DataFrame aus den Experimentdaten und transponiert es, um die Versuchspersonen als Zeilen anzuzeigen
    df = pd.DataFrame(data).transpose()
    
    # Speichert das DataFrame als Excel-Datei unter dem angegebenen Pfad
    df.to_excel(xlsx_path)
    return None



def load_relevant_data(file_name:str)->pd.DataFrame:
    """Lädt relevante Daten aus einer CSV-Datei, bereinigt und strukturiert sie.

    Parameters
    ----------
    file_path : str
        Der Dateipfad der CSV-Datei, die geladen werden soll.

    Returns
    -------
    pd.DataFrame
        Ein DataFrame mit gefilterten und umbenannten Daten.
    """

    # Lädt die CSV-Datei, überspringt die ersten zwei Zeilen und wählt bestimmte Spalten aus
    df = pd.read_csv(file_name, sep=';', skiprows=2, usecols= ['country code', 'height [cm]', 'weight [kg]', 'main sport'], na_values='UNKNOWN')
    
    # Benennt die Spalten um, um sie leichter lesbar zu machen
    df = df.rename(columns={'country code': 'country', 'height [cm]': 'height', 'weight [kg]': 'weight', 'main sport': 'sport'})
    
    # Entfernt Zeilen mit fehlenden Werten
    df = df.dropna(axis=0, how='any')

    return df

if __name__ == '__main__':
    # Führt das Experiment-Setup aus und speichert die Daten in einer Excel-Datei
    experiment_setup('output.xlsx')

    # Lädt die relevanten Daten aus der angegebenen CSV-Datei und gibt das bereinigte DataFrame aus 
    df = load_relevant_data('labs/lab/data/lab301_sport/data.csv')    
    print(df)