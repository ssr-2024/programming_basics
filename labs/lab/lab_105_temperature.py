## Funktionen

def celsius_to_kelvin(temperatur):
    """ returns the temperature transformed from celsius to kelvin
    Parameters
    -----
    temperature: float 
        temperature to be transformed       
    

    Returns
    -----
    temperature: float
        transformed temperature

    """
    return temperatur+273.15

def kelvin_to_celsius(temperatur):
    """ returns the temperature transformed from kelvin to celsius
    Parameters
    -----
    temperature: float 
        temperature to be transformed       
    

    Returns
    -----
    temperature: float
        transformed temperature

    """
    return temperatur-273.15

def celsius_to_fahrenheit(temperatur):
    """ returns the temperature transformed from celsius to fahrenheit
    Parameters
    -----
    temperature: float 
        temperature to be transformed       
    

    Returns
    -----
    temperature: float
        transformed temperature

    """
    return temperatur/(5/9) + 32

def fahrenheit_to_celsius(temperatur):
    """ returns the temperature transformed from fahrenheit to celsius
    Parameters
    -----
    temperature: float 
        temperature to be transformed       
    

    Returns
    -----
    temperature: float
        transformed temperature

    """
    return (5/9)*(temperatur-32)


def unit_input(selection):
    """ returns the input unit of the temperature, depending on the selection

    Parameters
    -----
    selection: int 
        user input for the transformation selected        
    

    Returns
    -----
    unit: str
        unit of the input temperature

    """
    if selection == 1:
        return 'Celsius'
    elif selection == 2:
        return 'Celsius'
    elif selection == 3:
        return 'Kelvin'
    elif selection == 4:
        return 'Kelvin'
    elif selection == 5:
        return 'Fahrenheit'
    elif selection == 6:
        return 'Fahrenheit'

def unit_output(selection):
    """ returns the output unit of the temperature, depending on the selection

    Parameters
    -----
    selection: int 
        user input for the transformation selected        
    

    Returns
    -----
    unit: str
        unit of the output temperature

    """
    if selection == 1:
        return 'Kelvin'
    elif selection == 2:
        return 'Fahrenheit'
    elif selection == 3:
        return 'Celsius'
    elif selection == 4:
        return 'Fahrenheit'
    elif selection == 5:
        return 'Celsius'
    elif selection == 6:
        return 'Kelvin'

## Skript
# tells user to input a number to select a transformation
transformation = int(input("Welche Umrechnung willst du machen? \n"
                 + "(1) Umrechnung von Celsius nach Kelvin \n"
                 + "(2) Umrechnung von Celsius nach Fahrenheit \n"
                 + "(3) Umrechnung von Kelvin nach Celsius \n"
                 + "(4) Umrechnung von Kelvin nach Fahrenheit \n"
                 + "(5) Umrechnung von Fahrenheit nach Celsius \n"
                 + "(6) Umrechnung von Fahrenheit nach Kelvin \n"))
# tells user to input a temperature to transform
temperature = float(input(f"Gib die Temperatur in {unit_input(transformation)} ein: "))

# calculates the new temperature depending on input
if transformation == 1:
    new_temperature = celsius_to_kelvin(temperature)
elif transformation == 2:
    new_temperature = celsius_to_fahrenheit(temperature)
elif transformation == 3:
    new_temperature = kelvin_to_celsius(temperature)
elif transformation == 4:
    new_temperature = celsius_to_fahrenheit(kelvin_to_celsius(temperature))
elif transformation == 5:
    new_temperature = fahrenheit_to_celsius(temperature)
elif transformation == 6:
    new_temperature = celsius_to_kelvin(fahrenheit_to_celsius(temperature))

print(f'{temperature}° {unit_input(transformation)} ≅ {new_temperature}° {unit_output(transformation)}')
