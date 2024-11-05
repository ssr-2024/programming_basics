from pathlib import Path

print(Path.home())  # prints the home directory
print(Path.cwd())   # prints the current working directory

dir_name = Path('code') # relative path to the directory 'code'

for item in dir_name.iterdir():
    print(item.name)  

dir_name = Path ('code/data') # relative path to the directory 'data'

for item in dir_name.glob('*.csv'):
    print(item.name)

    

