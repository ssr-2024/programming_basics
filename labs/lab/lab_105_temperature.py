## Funktionen

def celsius_to_kelvin(temperatur):
    return temperatur + 273.15

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

## Auswahl des Benutzers für die Umrechnung
print("Wählen Sie die gewünschte Umrechnung:")
print("    (1) Umrechnung von Celsius nach Kelvin")
print("    (2) Umrechnung von Celsius nach Fahrenheit")
print("    (3) Umrechnung von Kelvin nach Celsius")
print("    (4) Umrechnung von Kelvin nach Fahrenheit")
print("    (5) Umrechnung von Fahrenheit nach Celsius")
print("    (6) Umrechnung von Fahrenheit nach Kelvin")

# Speichere die Auswahl des Benutzers als int
selection = int(input("Ihre Auswahl: "))

# Definiere die Funktion unit_input
def unit_input(selection):
    """Gibt die Einheitsbezeichnung basierend auf der Benutzerauswahl zurück"""
    if selection == 1 or selection == 2:
        return 'Celsius'
    elif selection == 3 or selection == 4:
        return 'Kelvin'
    elif selection == 5 or selection == 6:
        return 'Fahrenheit'
    return ''


# Speichere die Auswahl des Benutzers als int
selection = int(input("Ihre Auswahl: "))





