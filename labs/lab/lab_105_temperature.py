
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
    

def unit_output(transformation_choice)->str:
    """
    Get the unit of the output temperature

    Parameters
    ----------
    transformation_choice: int

    Returns
    -------
    str: the unit of the output temperature
    """
    if transformation_choice == 1:
        return 'Kelvin'
    elif transformation_choice == 2:
        return 'Fahrenheit'
    elif transformation_choice == 3:
        return 'Celsius'
    elif transformation_choice == 4:
        return 'Fahrenheit'
    elif transformation_choice == 5:
        return 'Celsius'
    elif transformation_choice == 6:
        return 'Kelvin'

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


# Step 3: Calculate the transformed temperature depending on the transformation choice

if transformation_choice == 1:
    transformed_temperature = celsius_to_kelvin(temperature)
elif transformation_choice == 2:
    transformed_temperature = celsius_to_fahrenheit(temperature)
elif transformation_choice == 3:
    transformed_temperature = kelvin_to_celsius(temperature)
elif transformation_choice == 4:
    transformed_temperature = celsius_to_fahrenheit(kelvin_to_celsius(temperature))
elif transformation_choice == 5:
    transformed_temperature = fahrenheit_to_celsius(temperature)
elif transformation_choice == 6:
    transformed_temperature = celsius_to_kelvin(fahrenheit_to_celsius(temperature))

# Step 4: Print the transformed temperature

print(f'{temperature} {unit_input(transformation_choice)} = {transformed_temperature} {unit_output(transformation_choice)}')