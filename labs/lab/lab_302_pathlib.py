from pathlib import Path
from typing import Union, Dict


# erwartet entweder str oder path und gibt vor, was er als Rückgabewert erwartet
def vpns_exp01(path: Union[str, Path]) -> Dict[str, Path]:
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
    


def vpns_exp02(path: Union[str, Path]) -> Dict[str, Dict[int, Path]]:
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
    


if __name__ == '__main__':
    vpns_exp01('labs/lab/data/exp01')
    vpns_exp02('labs/lab/data/exp02')
