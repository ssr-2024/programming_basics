import numpy as np
import pandas as pd
from pathlib import Path

def experiment_setup(xlsx_path):
    """
    Creates an excel file of the experiment setup

    Parameters:
    -----------
    xlsx_path : str
        path to the excel file
    
    Returns:
    --------
    None
    """
    path = Path(xlsx_path)
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

    df = pd.DataFrame(data)
    df = df.transpose()
    df.to_excel(path)
    return None


def load_relevant_data(file_name):
    """
    loading the relevant data from the csv file, filtering and cleaning it

    Parameters:
    -----------
    file_name : str
        path to the csv file
    
    Returns:
    --------
    pd.DataFrame
        the cleaned and filtered data
    """
    # Importiere die Datei mit dem `;`-Trennzeichen und überspringe die ersten beiden Zeilen
    df = pd.read_csv(file_name, sep=';', skiprows=2, usecols=[0, 1, 2, 3, 4, 5], na_values="UNKNOWN")
    
    # Spalten auswählen
    df = df[["country code", "height [cm]", "weight [kg]", "main sport"]]
   
    # Spaltennamen anpassen
    df = df.rename({"country code":"country", "height [cm]":"height", "weight [kg]":"weight", "main sport":"sport"}, axis="columns")
    
    # Zeilen mit fehlenden Werten entfernen
    df.dropna(inplace=True)
    
    return df


if __name__ == '__main__':
    experiment_setup('output.xlsx')
    load_relevant_data('labs/lab/data/lab301_sport/data.csv')

    
