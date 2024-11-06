from pathlib import Path

def vpns_exp01(path='lab/data/exp01'):
    """
    Returns a dictionary containing the experiment setup based on
    all CSV files in the provided path.

    CSV files nested in subfolders are ignored.
    The names are derived from the CSV file names.

    Parameters
    ----------
    path : str, optional
        path to the experiment folder, by default 'lab/data/exp01'

    Returns
    -------
    dict
        the exp setup dict{ str : Path }
    """
    exp_setup = {}
    base_path = Path(path)
    
    for file in base_path.glob("*.csv"):
        key = file.stem  # Use the file name without the .csv extension as the dictionary key
        exp_setup[key] = file

    return exp_setup

def vpns_exp02(path='lab/data/exp02'):
    """
    Returns a dictionary containing the experiment setup based on
    the folder structure of the provided path and the containing CSV files.

    CSV files located elsewhere than in the vpn folders are ignored.
    The vpn names are derived from the folder names.
    The mzp is derived from the last 2 characters of the CSV file name: e.g. mzp_14.csv => 14

    Parameters
    ----------
    path : str, optional
        path to the experiment folder, by default 'lab/data/exp02'

    Returns
    -------
    dict
        the exp setup dict{ str : dict{ int : Path } }
    """
    exp_setup = {}
    base_path = Path(path)

    for folder in base_path.iterdir():
        if folder.is_dir() and folder.name.startswith("vp_"):
            vp_name = folder.name  # Use the exact folder name as key
            vp_data = {}

            for file in folder.glob("mzp_*.csv"):
                try:
                    mzp_number = int(file.stem.split("_")[-1])  # Extracts the last part as an integer
                    vp_data[mzp_number] = file
                except ValueError:
                    continue  # Skip files that do not end with a number

            exp_setup[vp_name] = vp_data

    return exp_setup
