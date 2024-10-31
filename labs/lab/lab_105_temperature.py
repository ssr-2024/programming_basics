## Funktionen

# 4. / 5. Funktionen, welche die Umrechnungen durchführen (eigentlich 4. Schritt, ich habe es im Ersten gemacht, ups.)
def celsius_to_kelvin(temperatur):
    return temperatur + 273.15

def kelvin_to_celsius(temperatur):
    return temperatur - 273.15

def celsius_to_fahrenheit(temperatur):
    return (temperatur * 9/5) + 32

def fahrenheit_to_celsius(temperatur):
    return (temperatur-32) * 5/9

# Löst das Problem der fehlenden Funktionen zur Umrechnung von Kelvin und Fahrenheit (und umgekehrt)
def kelvin_to_fahrenheit(temperatur):
    return (temperatur - 273.15) * 9/5 + 32

def fahrenheit_to_kelvin(temperatur):
    return (temperatur - 32) * 5/9 + 273.15

# 2. Funktion, welche basierend auf der Eingabe des Benutzers die Einzugebende Einheit zurückgibt.
def unit_input(selection): # Schleifen!
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
     else:
        return 'Invalid selection'

def unit_output(selection):
    return ''

## Skript

# 1. Fragt Nutzer*innen nach der Umrechnung, die sie durchführen möchten
selection = int(input('Please enter the number corresponding to the conversion you want to do:\n'
                            '(1) Celsius to Kelvin\n'
                            '(2) Celsius to Fahrenheit\n'
                            '(3) Kelvin to Celsius\n'
                            '(4) Kelvin to Fahrenheit\n'
                            '(5) Fahrenheit to Celsius\n'
                            '(6) Fahrenheit to Kelvin\n'
                            'Your choice: '))

# 3. Fragt Nutzer*innen nach der Temperatur, die sie umrechnen möchten
temperatur = float(input(f'Please enter a temperature in {unit_input(selection)}: '))

# 6. Transformation der Temperatur
if selection == 1:
    converted_temp=celsius_to_kelvin(temperatur)
elif selection == 2:
    converted_temp=celsius_to_fahrenheit(temperatur)
elif selection == 3:
    converted_temp=kelvin_to_celsius(temperatur)
elif selection == 4:
    converted_temp=kelvin_to_fahrenheit(temperatur) 
elif selection == 5:
    converted_temp=fahrenheit_to_celsius(temperatur)
elif selection == 6:
    converted_temp=fahrenheit_to_kelvin(temperatur)




print(f'{12}° {unit_input(12)} ≅ {12}° {unit_output(12)}')