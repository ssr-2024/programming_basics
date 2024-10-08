#programm, um namen und prozentzahlen aus dictionary auszugeben
from typing import Union


successful_tests = {
    'marc': 100,
    'remo': 61,
    'lars': 42,
    'lana': 87,
    'elio': 70,
    'andi': 90
}
def print_result(name:str, percentage: Union[int,float])-> None:
    """prints name and percentage in line
    therefore percentage is displayed with one * per 10%

    Parameters 
    ----------
    name: str
        name of individual
    percentage: int, float
        percentage of corresponding individual

    Returns
    -------
        none
    """
    print(f'{name}: {'*' * (int(percentage) // 10)}')

#gebe alle namen und prozentzahlen aus
print('Successful tests: [name, percentage]')
for name, percentage in successful_tests.items():
    print_result(name,percentage)