import numpy as np
import pandas as pd
from pathlib import Path

def experiment_setup(xlsx_path):
    # Data for the experiment setup
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
    
    # Create a DataFrame
    df = pd.DataFrame(data).transpose()
    
    # Save the DataFrame as an Excel file
    df.to_excel(xlsx_path)
    return None



def load_relevant_data(file_name):
    return None


if __name__ == '__main__':
    experiment_setup('output.xlsx')
    load_relevant_data('labs/lab/data/lab301_sport/data.csv')
    


