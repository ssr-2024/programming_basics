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
# Fragt Nutzer*innen nach der Umrechnung, die sie durchführen möchten
user_input = int(input('Please enter the number corresponding to the conversion you want to do:\n'
                            '(1) Celsius to Kelvin\n'
                            '(2) Celsius to Fahrenheit\n'
                            '(3) Kelvin to Celsius\n'
                            '(4) Kelvin to Fahrenheit\n'
                            '(5) Fahrenheit to Celsius\n'
                            '(6) Fahrenheit to Kelvin\n'
                            'Your choice: '))
print(f'{12}° {unit_input(12)} ≅ {12}° {unit_output(12)}')