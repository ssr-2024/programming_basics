

from typing import *




def print_result(name: str, percentage: Union [int, float]) -> None:
    """
    Prints a name and a bar visualization of the percentage using asterisks.

    Each asterisk represents 10%. For example, a percentage of 44 will result in four asterisks.

    Parameters
    ----------
    name : str
        The name of the individual or test case to be displayed.
    percentage : int
        The percentage score to be visualized as asterisks.
    
    Returns
    --------

            none
    
    """
    print(f"{name}: {'*' * (percentage // 10)}")


sucessfull_tests = {
    'Janis': 44,
    'Matthieu': 55,
    'Jonathan': 63,
    'Robin': 68,
    'Elias': 99,
    'Nicolas1': 20,
    'Nicolas2': 7
}

for name, percentage in sucessfull_tests.items():
    print_result(name, percentage)




