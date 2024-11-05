from pathlib import Path

dir_name = Path('code') # absolute path to directory 'code'
dir_data = Path('code/data')

# iterate through all items in the directory
for item in dir_name.iterdir():
    print(item.name)

# iterate and print all .csv file names
for item in dir_data.glob('*.csv'):
    print(item.name)