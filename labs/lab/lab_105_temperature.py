## Funktionen

def celsius_to_kelvin(temperatur):
    return temperatur

def kelvin_to_celsius(temperatur):
    return temperatur

def celsius_to_fahrenheit(temperatur):
    return temperatur

def fahrenheit_to_celsius(temperatur):
    return temperatur


def unit_input(transformation_choice)->str:
    """
    Get the unit of the input temperature

    Parameters:
    ----------
    transformation_choice: int
    
    Returns:
    -------
    str: the unit of the input temperature
    """

    if transformation_choice == 1:
        return 'Celsius'
    elif transformation_choice == 2:
        return 'Celsius'
    elif transformation_choice == 3:
        return 'Kelvin'
    elif transformation_choice == 4:
        return 'Kelvin'
    elif transformation_choice == 5:
        return 'Fahrenheit'
    elif transformation_choice == 6:
        return 'Fahrenheit'
    

def unit_output(selection):
    return ''

## Skript

# Step 1: ask the user for a transformation choice

def get_transformation_choice()->int:
    """
    Ask the user for a transformation choice
    
    Parameters:
    ----------
    None

    Returns:
    -------
    int: the transformation choice
        1: Celsius to Kelvin
        2: Celsius to Fahrenheit
        3: Kelvin to Celsius
        4: Kelvin to Fahrenheit
        5: Fahrenheit to Celsius
        6: Fahrenheit to Kelvin

    """
    print("Choose a transformation:")
    print("1. Celsius to Kelvin")
    print("2. Celsius to Fahrenheit")
    print("3. Kelvin to Celsius")
    print("4. Kelvin to Fahrenheit")
    print("5. Fahrenheit to Celsius")
    print("6. Fahrenheit to Kelvin")    
    
    choice = int(input("Enter the number of your choice: "))
    return choice

transformation_choice = get_transformation_choice()

print(f"You chose transformation number: {transformation_choice}")



print(f'{12}° {unit_input(12)} ≅ {12}° {unit_output(12)}')

