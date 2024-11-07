from typing import Union
from pathlib import Path
import pandas as pd

def run(folder: Union[Path, str], export_file: Union[Path, str] = "output.xlsx") -> None:
    # read folder
    folder_path = Path(folder)
    files = list(folder_path.glob("*.csv"))

    # create a list to save the data
    all_data = []

    # iterate through the files in the folder
    for file in files:
        # create a dataframe for the file
        df = pd.read_csv(
            file,
            skiprows=60,              # skip the first 60 rows
            header=0,                 # use the 61st row as header (it is now row 0)
            sep=';',                  # define ; to split data
            usecols=["HEART RATE (bpm)", "SECONDS"]  # only use the useful columns
        )

        # add Minutes to the dataframe
        df['Minute'] = (df['SECONDS'] // 60)

        # drop rows with missing values
        df = df.dropna(subset=['HEART RATE (bpm)'])  

        # group by MINUTES
        df_grouped = df.groupby('Minute')['HEART RATE (bpm)'].mean().reset_index()

        # create a row for vp-number
        df_grouped['VPN'] = file.stem

        # add the data to the list
        all_data.append(df_grouped)

    # add it to the dataframe
    result_df = pd.concat(all_data, ignore_index=True)

    # make the output match the expected output
    result_df = result_df.pivot(index='VPN', columns='Minute', values='HEART RATE (bpm)')

    result_df.columns.name = None

    # Export data to excel
    result_df.to_excel(export_file, header=True, index=True)

if __name__ == '__main__':
    run('labs/lab/data/suunto', 'ergebnisse.xlsx')
