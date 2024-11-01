## Funktionen

def celsius_to_kelvin(temperatur):
    return temperatur

def kelvin_to_celsius(temperatur):
    return temperatur

def celsius_to_fahrenheit(temperatur):
    return temperatur

def fahrenheit_to_celsius(temperatur):
    return temperatur


def unit_input(selection):
    return ''

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
        2: Kelvin to Celsius
        3: Celsius to Fahrenheit
        4: Fahrenheit to Celsius
    """
    print("Choose a transformation:")
    print("1. Celsius to Kelvin")
    print("2. Kelvin to Celsius")
    print("3. Celsius to Fahrenheit")
    print("4. Fahrenheit to Celsius")
    
    choice = int(input("Enter the number of your choice: "))
    return choice

transformation_choice = get_transformation_choice()

print(f"You chose transformation number: {transformation_choice}")



print(f'{12}° {unit_input(12)} ≅ {12}° {unit_output(12)}')

