import numpy as np
import pandas as pd
from pathlib import Path



def experiment_setup(xlsx_path):
    data = {
        'vpn01': {
        'Gruppe': "A",
        'Trial_01': "vid_01.mp4",
        'Trial_02': "vid_02.mp4",
        'Trial_03': "vid_03.mp4",
        'Trial_04': "vid_04.mp4"
        
    },
    'vpn02': {
        'Gruppe': "B",
        'Trial_01': "vid_03.mp4",
        'Trial_02': "vid_04.mp4",
        'Trial_03': "vid_01.mp4",
        'Trial_04': "vid_02.mp4"
        }
    }

    df = pd.DataFrame(data)

    df = df.transpose()
    df.to_excel(xlsx_path)
    
    return None

import pandas as pd

def load_relevant_data(file_name):
    # create a dataframe from the csv file
    df = pd.read_csv(file_name,
                     sep=';',  # define the separation symbol
                     skiprows=2,  # ignore the first two rows
                     usecols=["country code", "height [cm]", "weight [kg]", "main sport"],
                     na_values=["UNKNOWN"])  # NaN for 'UNKNOWN'
    
    # rename columns
    df = df.rename(columns={
        "country code": "country", 
        "height [cm]": "height", 
        "weight [kg]": "weight", 
        "main sport": "sport"
    })
    
    df = df.dropna(axis=0, how='any')  
    return df



df = load_relevant_data('labs/lab/data/lab301_sport/data.csv')
df.to_excel("text.xlsx")

if __name__ == '__main__':
    experiment_setup('output.xlsx')
    load_relevant_data('labs/lab/data/lab301_sport/data.csv')
