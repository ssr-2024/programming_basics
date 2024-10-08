
def print_result (name,percentage):
    """Prints the name and corresponding percentage value in a nicely formatted format.
    
    Parameters:
        name (str): Name of the person.
        percentage (int or float): Percentage of successful tests visualized by stars (1 star for each 10%).

    Returns:
        None
    """
    print(f"{name}: {'*'*(percentage//10)}")


successful_tests = {
    'Janis' : 44,
    'Peter' : 33,
    'George' : 22,

}

for name, percentage in successful_tests.items():
    print_result(name,percentage)
