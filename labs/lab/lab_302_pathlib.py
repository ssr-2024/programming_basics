from pathlib import Path
from typing import Union, Dict


# erwartet entweder str oder path und gibt vor, was er als Rückgabewert erwartet
def vpns_exp01(path: Union[str, Path] = 'lab/data/exp01') -> Dict[str, Path]:
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
    path = Path(path) # convert to Path object

    exp_setup = {} # create empty dict

    # for each file in the path, write the file name as key and the path as value
    for file in path.iterdir():
        # check if file is a csv file
        if file.is_file() and file.suffix == '.csv':
            exp_setup[file.stem] = file

    return exp_setup
    


def vpns_exp02(path: Union[str, Path] = 'lab/data/exp02') -> Dict[str, Dict[int, Path]]:
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
    path = Path(path) # convert to Path object
    exp_setup = {} # create empty dict

    # for each vpn_folder in the path, write the folder name as key and the path as value
    for vpn_folder in path.iterdir():
        if vpn_folder.is_dir():
            vpn_setup = {}
            # for each file in the vpn_folder, write the last 2 digits of the file name as key and the path as value
            for file in vpn_folder.iterdir():
                if file.is_file() and file.suffix == '.csv':
                    mzp = int(file.stem[-2:])
                    vpn_setup[mzp] = file
            exp_setup[vpn_folder.stem] = vpn_setup
    return exp_setup
    


if __name__ == '__main__':
    vpns_exp01('labs/lab/data/exp01')
    vpns_exp02('labs/lab/data/exp02')
