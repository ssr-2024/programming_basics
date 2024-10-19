## Funktionen

def celsius_to_kelvin(temperatur):
    return temperature + 273.15

def kelvin_to_celsius(temperatur):
    return temperatur  - 273.15

def celsius_to_fahrenheit(temperatur):
    return (temperature * 9/5) + 32

def fahrenheit_to_celsius(temperatur):
    return 5/9*(temperature - 32)


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
# Benutzer nach Umrechnungstyp fragen
print("Wähle eine Option für die Umrechnung:")
print("(1) Umrechnung von Celsius nach Kelvin")
print("(2) Umrechnung von Celsius nach Fahrenheit")
print("(3) Umrechnung von Kelvin nach Celsius")
print("(4) Umrechnung von Kelvin nach Fahrenheit")
print("(5) Umrechnung von Fahrenheit nach Celsius")
print("(6) Umrechnung von Fahrenheit nach Kelvin")

# Entscheidung als int speichern
selection = int(input("Deine Wahl: "))

print(unit_input(selection))

temperature = float(input(f"Gib eine Temperatur in {unit_input(selection)} ein: "))

if selection == 1:
    converted_temp = celsius_to_kelvin(temperature)
elif selection == 2:
    converted_temp = celsius_to_fahrenheit(temperature)
elif selection == 3:
    converted_temp = kelvin_to_celsius(temperature)
elif selection == 4:
    converted_temp = celsius_to_fahrenheit(kelvin_to_celsius(temperature))
elif selection == 5:
    converted_temp = fahrenheit_to_celsius(temperature)
elif selection == 6:
    converted_temp = celsius_to_kelvin(fahrenheit_to_celsius(temperature))


print(f'{12}° {unit_input(12)} ≅ {12}° {unit_output(12)}')

