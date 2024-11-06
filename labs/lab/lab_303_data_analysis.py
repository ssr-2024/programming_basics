from typing import Union, Dict
from pathlib import Path
import pandas as pd

def process_file(file_path: Path) -> pd.DataFrame:
    """
    Process a .csv file containing heart rate data and return a DataFrame with minute averages.

    Parameters
    ----------
    file_path : Path
        The path to the .csv file.
    
    Returns
    -------
    pd.DataFrame
        A DataFrame containing the minute averages of the heart rate data.
    """
    # Load the desired section of the .csv file into a DataFrame
    df = pd.read_csv(file_path, sep=';', skiprows=60, usecols=['HEART RATE (bpm)', 'SECONDS'])
    
    # Drop rows with any NaN values
    df = df.dropna(axis=0, how='any')
    
    # Add a column for the grouping feature 'minutes'
    df['MINUTES'] = df['SECONDS'] // 60
    
    # Group by 'MINUTES' and calculate the mean heart rate
    minute_avg_row = df.groupby('MINUTES')['HEART RATE (bpm)'].mean().reset_index()
    
    return minute_avg_row

# Test the function with a sample file
example_file = Path('labs/lab/data/suunto/31_1.csv')
result = process_file(example_file)
print(result)

def run(folder: Union[Path, str], export_file: Union[Path, str] = 'labs/lab/export.xlsx') -> None:
    """
    Process all .csv files in the specified folder and export the combined data to an Excel file.

    Parameters
    ----------
    folder : Union[Path, str]
        The path to the folder containing the .csv files.
    export_file : Union[Path, str], optional
        The path to the Excel file where the combined data will be exported, by default 'labs/lab/export.xlsx'

    Returns
    -------
    None
    """
    folder = Path(folder)
    all_data = pd.DataFrame()
    
    # Iterate over all files in the specified folder
    csv_files = folder.iterdir()
    
    for file in csv_files:
        if file.suffix == '.csv':
            # Process the .csv file and get the DataFrame with minute averages
            minute_avg_row = process_file(file)
            
            # Add the filename as a column
            minute_avg_row['FILENAME'] = file.stem
            
            # Pivot the DataFrame to have minutes as columns and filenames as rows
            pivot_df = minute_avg_row.pivot(index='FILENAME', columns='MINUTES', values='HEART RATE (bpm)')
            
            # Append the processed data to the all_data DataFrame
            all_data = pd.concat([all_data, pivot_df], axis=0)
    
    # Export the combined DataFrame to an Excel file
    all_data.to_excel(export_file)
    
    return None

if __name__ == '__main__':
    run('labs/lab/data/suunto')
