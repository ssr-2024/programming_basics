from pathlib import Path

Path().home()

Path().cwd()

file_path = Path
print(file_path.name)

dir_name = Path('code/data')
for item in dir_name.glob('*.csv'):
    print(item.name)


