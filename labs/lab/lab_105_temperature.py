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
unit = int(input("Welche Umrechnung willst du machen? \n"
                 + "(1) Umrechnung von Celsius nach Kelvin \n"
                 + "(2) Umrechnung von Celsius nach Fahrenheit \n"
                 + "(3) Umrechnung von Kelvin nach Celsius \n"
                 + "(4) Umrechnung von Kelvin nach Fahrenheit \n"
                 + "(5) Umrechnung von Fahrenheit nach Celsius \n"
                 + "(6) Umrechnung von Fahrenheit nach Kelvin \n"))


print(f'{12}° {unit_input(12)} ≅ {12}° {unit_output(12)}')
