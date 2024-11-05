from typing import Union, Dict
from pathlib import Path
import glob
import pandas as pd

def process_suunto_data(file_path: Path = 'labs/lab/data/suunto/31_1.csv') -> pd.DataFrame:
    """
    Processes a single Suunto CSV file to calculate minute-wise average heart rates.
    
    Parameters
    ----------
    file_path : Path
        Path to the CSV file to process.

    Returns
    -------
    pd.DataFrame
        DataFrame containing minute-wise averages of heart rates.
    """
    # Load the CSV file, focusing on the relevant columns (time and heart rate)
    df = pd.read_csv(Path(file_path), sep = ";",skiprows = 60, na_values=' ')
    df = df[['HEART RATE (bpm)', 'SECONDS']] 
    # Drop rows with no values
    df.dropna(inplace=True)
    # Convert to integer
    df = df.astype({'HEART RATE (bpm)': 'int32', 'SECONDS': 'int32'})  
    # Add a new column for minutes
    df['minutes'] = df['SECONDS'] // 60  # Integer Division, to calculate the minute

    # Group by minute and calculate the average heart rate
    avg_df = df.groupby('minutes')['HEART RATE (bpm)'].mean().reset_index()

    return avg_df

def run(folder_dir: Union[Path, str], export_file: Union[Path, str] = 'lab/export.xlsx') -> None:
    """
    Processes all Suunto CSV files in a directory and exports the minute-wise average heart rates to an Excel file.

    Parameters
    ----------
    folder_dir : Union[Path, str]
        Directory containing the Suunto CSV files.
    export_file : Union[Path, str]
        Path to the Excel file to export the results.
    """
    
    # Gather all CSV files in the directory
    folder_dir = Path(folder_dir)
    file_paths = folder_dir.glob('*.csv')
    
    # Create dataframes to store the DataFrames
    data = pd.DataFrame()
    all_data = pd.DataFrame()
    
    # Process each file and store the resulting DataFrame in the dictionary
    for file_path in file_paths:
        file_name = Path(file_path).stem  # Extract the file name from the filename
        avg_df = process_suunto_data(Path(file_path))
        all_data[file_name] = avg_df['HEART RATE (bpm)']  # Store the 'HEART RATE (bpm)' column
    # Transpose the dataframe    
    all_data = all_data.transpose()
    # Export the result to an Excel file
    all_data.to_excel(export_file)


if __name__ == '__main__':
    run('labs/lab/data/suunto')
