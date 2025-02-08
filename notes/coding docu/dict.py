# Kreieren eines Wörterbuchs und weitere Spielereien

from typing import *


def print_result (name: str, percentage: Union[int,float])->None:
    """prints the name and corresponding percentage value in a nicely formatted format.
    
    Parameters
    ----------

    name: str, char
        name of the individual or test case to be displayed
        
    percentage: int, float
        percentage score to be visualized as asterisks
    
    Returns
    -------
        none    
    """

    print(f"{name}: {'*'*(percentage//10)}")

successfull_tests={
    'marc':100,
    'remo':61,
    'lars':42,
    'lana':87,
    'elio':70,
    'andi':90
}

for name, percentage in successfull_tests.items():
    print_result(name,percentage) # print_result erst definieren


