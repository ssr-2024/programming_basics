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



print(f'{12}° {unit_input(12)} ≅ {12}° {unit_output(12)}')

