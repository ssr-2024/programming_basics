from typing import *


def visualize(percentage: Union[float, int]) -> None:
    """"
    This function represents any number in form of '*'. 
    For every 10 it gets one more '*'

    Parameters
    -------
    percentage: int, float
        percentage you want to display as astrisks
    
    Returns
    -------

    None    
    
    """
    print(f"{percentage}%: {'* ' * (percentage//10)}")

percentages = [10, 29, 33, 92, 72, 73, 37]

for percentage in percentages:
    visualize(percentage)

