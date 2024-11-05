from typing import Union, Dict
from pathlib import Path
import pandas as pd



def run(folder: Union[Path, str], export_file: Union[Path, str] = 'lab/export.xlsx') -> None:
    data = pd.read_csv(export_file, skiprows=60, header=61, names={})

    
    
    return None


if __name__ == '__main__':
    run('labs/lab/data/suunto')
