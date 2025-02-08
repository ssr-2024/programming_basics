from pathlib import Path

print(Path.cwd()) # Current working directory für VS Code ist der Ordner, der aktuell geöffnet ist

print(Path.home()) # Home directory

dir_name=Path('code') # Erstellt ein Path-Objekt für den Ordner "code"
for item in dir_name.iterdir(): # Listet alle Dateien und Ordner im Verzeichnis auf
    print(item.name) 
# Im interactive window sind wir in einem anderen directory 

dir_name=Path('code/data')
for item in dir_name.glob('*.csv'): # Listet alle Dateien mit der Endung .csv im Verzeichnis auf
    print(item.name)  