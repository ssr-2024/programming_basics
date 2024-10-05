## Funktionen

def celsius_to_kelvin(temperatur):
    temperatur = temperatur + 273.15
    return temperatur

def kelvin_to_celsius(temperatur):
    temperatur = temperatur - 273.15
    return temperatur

def celsius_to_fahrenheit(temperatur):
    temperatur = temperatur * 9/5 + 32
    return temperatur

def fahrenheit_to_celsius(temperatur):
    temperatur = 5/9 * (temperatur - 32)
    return temperatur

int = input("""(1) Umrechnung von Celsius nach Kelvin
        (2) Umrechnung von Celsius nach Fahrenheit
        (3) Umrechnung von Kelvin nach Celsius
        (4) Umrechnung von Kelvin nach Fahrenheit
        (5) Umrechnung von Fahrenheit nach Celsius
        (6) Umrechnung von Fahrenheit nach Kelvin""")

def unit_input(selection):
    if int == 1 or 2:
        a = 'Celsius'
    elif int == 3 or 4:
        a = 'Kelvin'
    elif int == 5 or 6:
        a = 'Fahrenheit'
    return 'a'

#temp = float(input(f'Temperatur in {unit_input(int)}:'))
#print(f'Temperatur in ')

def unit_output(selection):
    return ''

## Skript
print(f'{12}° {unit_input(12)} ≅ {12}° {unit_output(12)}')
