## Funktionen

def celsius_to_kelvin(temperatur):
    return temperatur + 273.15

def kelvin_to_celsius(temperatur):
    return temperatur - 273.15

def celsius_to_fahrenheit(temperatur):
    return (temperatur * 9/5) + 32

def fahrenheit_to_celsius(temperatur):
    return (temperatur-32) * 5/9


def unit_input(selection):
    return ''

def unit_output(selection):
    return ''

## Skript
print(f'{12}° {unit_input(12)} ≅ {12}° {unit_output(12)}')