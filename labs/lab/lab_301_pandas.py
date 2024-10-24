import numpy as np
import pandas as pd
from pathlib import Path

def experiment_setup(xlsx_path):
    # Create the experiment setup data
    data = {
        'vpn01': {
        'Gruppe': 'A',
        'Trial_01': 'vid_01.mp4', 
        'Trial_02': 'vid_02.mp4', 
        'Trial_03': 'vid_03.mp4', 
        'Trial_04': 'vid_04.mp4', 
    },
    'vpn02': {
        'Gruppe': 'B',
        'Trial_01': 'vid_03.mp4', 
        'Trial_02': 'vid_04.mp4', 
        'Trial_03': 'vid_01.mp4', 
        'Trial_04': 'vid_02.mp4', 
    },
    }
    df = pd.DataFrame(data).transpose()
    df.to_excel(xlsx_path)

import pandas as pd

def load_relevant_data(file_name):
    # Lade den Datensatz und ersetze 'UNKNOWN' durch NaN
    df = pd.read_csv(file_name, delimiter=';', skiprows=2, na_values='UNKNOWN')
    
    # Behalte nur die relevanten Spalten und benenne sie um
    df = df[['country code', 'height [cm]', 'weight [kg]', 'main sport']]
    df.columns = ['country', 'height', 'weight', 'sport']
    
    # Entferne alle Zeilen mit mindestens einem NaN-Wert
    df_cleaned = df.dropna()
    
    return df_cleaned

if __name__ == '__main__':
    file_path = 'lab301_sport/data.csv'
    cleaned_data = load_relevant_data(file_path)

# Das bereinigte DataFrame ausgeben
print(cleaned_data)






