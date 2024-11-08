import numpy as np
import pandas as pd
from pathlib import Path

def experiment_setup(xlsx_path):
    """
    Creates an experiment setup structure and exports it as an Excel file.
    
    Parameters:
    - xlsx_path (str or Path): Path where the output Excel file will be saved.
    
    The function generates a predefined structure with participant identifiers ('vpn01', 'vpn02')
    and experimental trials. It then creates a DataFrame with this structure, transposes it to
    match the expected format, and exports the data to the specified Excel file.
    
    Returns:
    - None
    """
    
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
    
    # Convert data structure to DataFrame
    df = pd.DataFrame(data)
    
    # Transpose DataFrame to match desired format
    df_transposed = df.transpose()
    
    # Export transposed DataFrame to Excel file
    df_transposed.to_excel(xlsx_path, index=True)


def load_relevant_data(file_name):
    """
    Loads and filters relevant data from a CSV file.
    
    Parameters:
    - file_name (str): Path to the CSV file containing the data.
    
    The function reads the specified CSV file, selects only the columns for 'country', 
    'height', 'weight', and 'sport', and drops rows with missing values.
    
    Returns:
    - pd.DataFrame: A DataFrame containing the filtered data.
    """

    df = pd.read_csv(
        file_name,
        sep=';',                  # Set delimiter to semicolon
        skiprows=3,               # Skip first 3 rows to get to data
        usecols=[0, 1, 2, 5],     # Only load specified columns
        names=['country', 'height', 'weight', 'sport'],  # Set custom column names
        na_values=['UNKNOWN']     # Treat 'UNKNOWN' values as NaN
    ).dropna(axis=0, how='any')   # Remove rows with any missing values

    return df


if __name__ == '__main__':
    # Call experiment_setup function to create and save the experiment setup file
    experiment_setup('input.xlsx')
    
    # Call load_relevant_data function to load and filter data from CSV file
    df_relevant = load_relevant_data('labs/lab/data/lab301_sport/data.csv')
