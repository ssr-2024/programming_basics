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

selection = int(input("""(1) Umrechnung von Celsius nach Kelvin
        (2) Umrechnung von Celsius nach Fahrenheit
        (3) Umrechnung von Kelvin nach Celsius
        (4) Umrechnung von Kelvin nach Fahrenheit
        (5) Umrechnung von Fahrenheit nach Celsius
        (6) Umrechnung von Fahrenheit nach Kelvin"""))

def unit_input(selection):
    """
    gibt einzugebendes Temperaturformat zurück
    """
    if selection == 1 or selection == 2:
        return 'Celsius'
    elif selection == 3 or selection == 4:
        return 'Kelvin'
    elif selection == 5 or selection == 6:
        return 'Fahrenheit'

temp = float(input(f'Gib eine Temperatur in {unit_input(selection)} ein:'))

def unit_output(selection):
    """
    gibt auszugebendes Temperaturformat zurück
    """
    if selection == 3 or selection == 5:
        return 'Celsius'
    elif selection == 1 or selection == 6:
        return 'Kelvin'
    elif selection == 2 or selection == 4:
        return 'Fahrenheit'


if selection == 1:
    new_temp = celsius_to_kelvin(temp)
elif selection == 2:
    new_temp = celsius_to_fahrenheit(temp)
elif selection == 3:
    new_temp = kelvin_to_celsius(temp)
elif selection == 4:
    new_temp = celsius_to_fahrenheit(kelvin_to_celsius(temp))
elif selection == 5:
    new_temp = fahrenheit_to_celsius(temp)
elif selection == 6:
    new_temp = celsius_to_kelvin(fahrenheit_to_celsius(temp))

#print(f'{temp} für `{temp}`° {unit_input(int)} gewählt: "{temp}"° {unit_input(int)} ≅ {new_temperature(temp)}° {unit_output(temp)}')

## Skript
print(f'{temp}° {unit_input(selection)} ≅ {new_temp}° {unit_output(selection)}')
