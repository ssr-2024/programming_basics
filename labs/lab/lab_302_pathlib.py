from pathlib import Path
from typing import Union, Dict # um zu spezifizieren, ob str oder Path direkt eingelesen werden solll


# erwartet entweder str oder path und gibt vor, was er als Rückgabewert erwartet
def vpns_exp01(path: Union[str, Path] = 'labs/lab/data/exp01') -> Dict[str, Path]:
    """
    Returns a dictionary containing the experiment setup based on
    all CSV files in the provided path.

    CSV files nested in subfolders are ignored.
    The names are derived from the CSV file names.

    Parameters
    ----------
    path : str, optional
        path to the experiment folder, by default 'labs/lab/data/exp01'

    Returns
    -------
    dict
        the exp setup dict{ str : Path }

    Examples
    --------
    expect the following folder structure:

    labs/lab/data/exp01/
             ├───vpn_01.csv
             └───vpn_02.csv

    ```py
    >>> vpns_exp01('labs/lab/data/exp01')

    {
        'vpn_01': Path(labs/lab/data/vpn_01.csv),
        'vpn_02': Path(labs/lab/data/vpn_02.csv)
    }
    ```
    """
    path = Path(path) # konvertiert den Pfad in ein Path-Objekt
    exp_setup = {} # erstellt ein leeres dictionary
    for file in path.glob('*.csv'): # sucht alle csv-Dateien im angegebenen Pfad, geht auch mit iterdir()
        name=file.stem  
        exp_setup[name]=file # fügt den Dateinamen und den Pfad zur Datei in das dictionary ein
    return exp_setup



def vpns_exp02(path: Union[str, Path]= 'labs/lab/data/exp02') -> Dict[str, Dict[int, Path]]:
    """
    Returns a dictionary containing the experiment setup based on
    the folder structure of the provided path and the containing CSV files.


    CSV files located elsewhere than in the vpn folders are ignored.
    The vpn names are derived from the folder names.
    The mzp is derived from the last 2 characters of the CSV file name: e.g. mzp_14.csv => 14

    Parameters
    ----------
    path : str, optional
        path to the experiment folder, by default 'labs/lab/data/exp02'

    Returns
    -------
    dict
        the exp setup dict{ str : dict{ int : Path } }

    Examples
    --------
    expect the following folder structure:

    labs/lab/data/exp02/
             ├───vpn_01/
             │   ├───mzp_01.csv
             │   ├───mzp_02.csv
             │   ├───mzp_03.csv
             │   └───mzp_04.csv
             └───vpn_02/
                 ├───mzp_01.csv
                 ├───mzp_02.csv
                 ├───mzp_03.csv
                 └───mzp_04.csv
    ```py
    >>> vpns_exp02('labs/lab/data/exp02')
    {
        'vpn_01': {
            1: Path(labs/lab/data/vpn_01/mzp_01.csv),
            2: Path(labs/lab/data/vpn_01/mzp_02.csv),
            3: Path(labs/lab/data/vpn_01/mzp_03.csv),
            4: Path(labs/lab/data/vpn_01/mzp_04.csv)
        },
        'vpn_02': {
            1: Path(labs/lab/data/vpn_02/mzp_01.csv),
            2: Path(labs/lab/data/vpn_02/mzp_02.csv),
            3: Path(labs/lab/data/vpn_02/mzp_03.csv),
            4: Path(labs/lab/data/vpn_02/mzp_04.csv)
        }
    }
    ```
    """
    path = Path(path) # Path konvertieren
    exp_setup = {}
    for vpn_folder in path.iterdir():
        if vpn_folder.is_dir():
            vpn_name = vpn_folder.name
            exp_setup[vpn_name] = {} # erstellt ein leeres dictionary für die VPNs
            for csv_file in vpn_folder.glob('*.csv'):
                mzp = int(csv_file.stem.split('_')[-1])
                exp_setup[vpn_name][mzp] = csv_file
    return exp_setup
    


if __name__ == '__main__':
    print(vpns_exp01('labs/lab/data/exp01'))
    print(vpns_exp02('labs/lab/data/exp02'))