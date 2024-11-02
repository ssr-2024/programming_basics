## Funktionen

def celsius_to_kelvin(temperature: float)->float:
    """
    Convert a temperature from Celsius to Kelvin
    
    Parameters
    ----------
    temperature: float

    
    Returns
    -------
    float: the temperature in Kelvin

    """

    return temperature + 273.15

def kelvin_to_celsius(temperature: float)->float:
    """
    Convert a temperature from Kelvin to Celsius

    Parameters
    ----------
    temperature: float

    Returns
    -------
    float: the temperature in Celsius
    """
    return temperature - 273.15

def celsius_to_fahrenheit(temperature: float)->float:
    """
    Convert a temperature from Celsius to Fahrenheit

    Parameters
    ----------
    temperature: float

    Returns
    -------
    float: the temperature in Fahrenheit
    """
    return temperature * 9/5 + 32

def fahrenheit_to_celsius(temperature: float)->float:
    """
    Convert a temperature from Fahrenheit to Celsius

    Parameters
    ----------
    temperature: float

    Returns
    -------
    float: the temperature in Celsius
    """
    return (temperature - 32) * 5/9


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

# Step 2: ask the user for a temperature to transform

temperature = float(input(f"Enter the temperature in {unit_input(transformation_choice)} you want to transform: "))
print(f"You entered {temperature} {unit_input(transformation_choice)}")

print(f'{12}° {unit_input(12)} ≅ {12}° {unit_output(12)}')

