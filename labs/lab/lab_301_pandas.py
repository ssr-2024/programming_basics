import numpy as np
import pandas as pd
from pathlib import Path


def experiment_setup(xlsx_path):
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
# create and transpose data frame
    df=pd.DataFrame(data).transpose()

# export to excel
    df.to_excel(xlsx_path)

    return None


def load_relevant_data(file_name):
    df=pd.read_csv(
        'labs/lab/data/lab301_sport/data.csv',
        sep=';',
        skiprows=3,
        usecols=[0,1,2,5],
        names=['country', 'height', 'weight', 'sport'],
        na_values=['UNKNOWN']
    ).dropna(axis=0,how='any')
    return df


# modul: nur funktionalität nutzen, stellt funktionen zur verfügung
# dient dazu, ob datei als modul importiert wird oder als hauptdatei ausgeführt
if __name__ == '__main__':
    experiment_setup('output.xlsx')
    load_relevant_data('labs/lab/data/lab301_sport/data.csv')