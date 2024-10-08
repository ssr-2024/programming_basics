from typing import *

def print_result(name: str,percentage: Union[int,float])-> None:
    """prints the name and the corresponding precentage value nicely formatted.

    Parameters
    -----------

    name: str, char
        name of the individual or test case to be displayed.

    percentage: int, float
        percentage score to be visualized as asterisks

    Returns
    --------

        none    
    """
    print(f"{name}: {'*'*(percentage//10)}")

successful_tests = {
    'Janis': 44,
    'Matthieu': 55,
    'Jonathan': 63,
    'Robin': 78,
    'Nicolas1': 72, # Werte können hier auch andere Datentypen annehmen, beispielsweise ein float also hier 72.8 Dazu muss dann oben "percentage" in einen integer umgewandelt werden, damit die integer division funktioniert. Dictionaries sind sehr flexibles, anders als Listen.
    'Eliane': 77,
    'Johanna': 82,
    'Nicolas2': 87,
    'Elias': 93, 
}

for name, percentage in successful_tests.items():
    print_result(name, percentage)
