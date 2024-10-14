## Funktionen

def celsius_to_kelvin(temperatur):
    return temperatur+273.15

def kelvin_to_celsius(temperatur):
    return temperatur-273.15

def celsius_to_fahrenheit(temperatur):
    return temperatur

def fahrenheit_to_celsius(temperatur):
    return (5/9)*(temperatur-32)


def unit_input(selection):
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
    return ''

## Skript
unit = int(input("Welche Umrechnung willst du machen? \n"
                 + "(1) Umrechnung von Celsius nach Kelvin \n"
                 + "(2) Umrechnung von Celsius nach Fahrenheit \n"
                 + "(3) Umrechnung von Kelvin nach Celsius \n"
                 + "(4) Umrechnung von Kelvin nach Fahrenheit \n"
                 + "(5) Umrechnung von Fahrenheit nach Celsius \n"
                 + "(6) Umrechnung von Fahrenheit nach Kelvin \n"))


print(f'{12}° {unit_input(12)} ≅ {12}° {unit_output(12)}')
