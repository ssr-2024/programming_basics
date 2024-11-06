from pathlib import Path

dir_name = Path('docs') # erstellt ein Path-Objekt mit einem relativen Pfad, mit dem Unterordner 'docs'. Beginnt beim current working directory (cwd).
for item in dir_name.iterdir():
    print(item.name)

# cwd für VS code ist der Ordner, in dem die Datei liegt, die ausgeführt wird. 

dir_name = Path('code/data')
for item in dir_name.glon('*.csv'):
    print(item.name)