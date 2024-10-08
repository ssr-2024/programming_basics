from typing import *


def print_results(name: str, percentage: Union[int, float]) -> None: # we tell the function what types the parameters have to be
    """ prints name and corresponding percentage as number of '*'.

    Parameters
    -----
    name: str, char 
        name of a individual or test case you want to be displayed
    percentage: int, float
        percentage score to be visualized as astrisks

    Returns
    -----
    
        none

    """
    print(f"{name}: {'* ' * (int(percentage)//10)}")

# Dictionary that stores number successfull tests for different people (important: keys must be unique)
successfull_tests = {
    "Max" : 100,
    "Remo": 61,
    "Lars": 42,
    "Lana": 87.8,
    "Elio": 90
}

for name, percentage in successfull_tests.items():
    print_results(name, percentage)

