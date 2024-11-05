from pathlib import Path

dir_name = Path('code/data')
dir_name.iterdir() 

for file in dir_name.iterdir():
    print(file.stem) 

for file in dir_name.glob('*.csv'):
    print(file.stem)



