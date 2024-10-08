def print_result(name, percentage):
    """prints the name and correspondending percentage value in a nicely formatted format
    
    Parameters
    -----------
    name: str, char
        name of the individual or test case to be displayed
    percentage: int, float
        percentage score to be visualized as asteriks

    Returns
    --------
        none
        
    """
    print (f"{name}: {'* ' * (int(percentage)//10)}") 

successful_tests = {
    'Janis':44,
    'Matthieu': 55,
    'Jonathan': 63,
    'Robin': 68,
    'Nicolas':72,
    'Eliane':77,
    'Johanna': 82,
    'Nicolas I': 87.8, #Keys müssen immer eindeutig sein
    'Elias':93

}

for name, percentage in successful_tests.items():
    print_result(name, percentage)

