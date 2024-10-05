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
    """
    gibt einzugebendes Temperaturformat zurück
    """
    if selection == 1 or 2:
        return 'Celsius'
    elif selection == 3 or 4:
        return 'Kelvin'
    elif selection == 5 or 6:
        return 'Fahrenheit'

temp = float(input(f'Gib eine Temperatur in °{unit_input(int)} ein:'))

def unit_output(selection):
    """
    gibt auszugebendes Temperaturformat zurück
    """
    if selection == 3 or 5:
        return 'Celsius'
    elif selection == 1 or 6:
        return 'Kelvin'
    elif selection == 2 or 4:
        return 'Fahrenheit'

def new_temperature(temp):
    if int == 1:
        new_temp = celsius_to_kelvin(temp)
    elif int == 2:
        new_temp = celsius_to_fahrenheit(temp)
    elif int == 3:
        new_temp = kelvin_to_celsius(temp)
    elif int == 4:
        new_temp = celsius_to_fahrenheit(kelvin_to_celsius(temp))
    elif int == 5:
        new_temp = fahrenheit_to_celsius(temp)
    elif int == 6:
        new_temp = celsius_to_kelvin(fahrenheit_to_celsius(temp))
    return new_temp

print(f'User hat `{int}` für `{temp}`° {unit_input(int)} gewählt: "{temp}"° {unit_input(int)} ≅ {new_temperature(temp)}° {unit_output(temp)}')

## Skript
print(f'{12}° {unit_input(12)} ≅ {12}° {unit_output(12)}')
