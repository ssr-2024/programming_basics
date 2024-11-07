from pathlib import Path

def vpns_exp01(path='lab/data/exp01'):
    """Lädt alle CSV-Dateien im angegebenen Verzeichnis und erstellt ein Wörterbuch mit Dateinamen als Schlüsseln.

    Parameters
    ----------
    directory : str, optional
        Pfad zum Verzeichnis, in dem die Dateien gesucht werden (Standard ist 'lab/data/exp01').

    Returns
    -------
    dict
        Ein Wörterbuch mit den Dateinamen (ohne Erweiterung) als Schlüssel und den Datei-Pfaden als Werte.
    """


    exp_setup = {} # Initialisiert das Wörterbuch für die Daten
    base_path = Path(path)
    
    # Durchsucht alle CSV-Dateien im Verzeichnis und speichert sie im Wörterbuch
    for file in base_path.glob("*.csv"):
        key = file.stem # Nutzt den Dateinamen (ohne Erweiterung) als Schlüssel
        exp_setup[key] = file

    return exp_setup


def vpns_exp02(path='lab/data/exp02'):
    """Lädt CSV-Dateien aus Unterverzeichnissen, die mit 'vp_' beginnen, und organisiert sie nach VP-Nummer und Datei.

    Parameters
    ----------
    directory : str, optional
        Pfad zum Verzeichnis, in dem die VP-Ordner gesucht werden (Standard ist 'lab/data/exp02').

    Returns
    -------
    dict
        Ein verschachteltes Wörterbuch, das die VP-Ordnernamen als Schlüssel und die CSV-Dateien darin als weitere Schlüssel speichert,
        wobei der Schlüssel auf die MZP-Nummer basiert.
    """


    exp_setup = {} # Initialisiert das Wörterbuch für die Daten
    base_path = Path(path)

    # Durchsucht alle CSV-Dateien im Verzeichnis und speichert sie im Wörterbuch
    for folder in base_path.iterdir():
        if folder.is_dir() and folder.name.startswith("vp_"):
            vp_name = folder.name # Nutzt den VP-Ordnername als Schlüssel
            vp_data = {}

            # Durchsucht alle CSV-Dateien im VP-Ordner und speichert sie im Wörterbuch
            for file in folder.glob("mzp_*.csv"):
                try:
                    # Extrahiert die MZP-Nummer aus dem Dateinamen
                    mzp_number = int(file.stem.split("_")[-1])
                    vp_data[mzp_number] = file
                except ValueError:
                    # Ignoriert Dateien, die nicht dem Namen entsprechen
                    continue

            exp_setup[vp_name] = vp_data

    return exp_setup