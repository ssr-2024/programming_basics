# Funktionen für Temperaturumrechnungen
def celsius_to_kelvin(temperature):
    """Konvertiert Celsius nach Kelvin."""
    return temperature + 273.15

def kelvin_to_celsius(temperature):
    """Konvertiert Kelvin nach Celsius."""
    return temperature - 273.15

def celsius_to_fahrenheit(temperature):
    """Konvertiert Celsius nach Fahrenheit."""
    return (temperature * 9/5) + 32

def fahrenheit_to_celsius(temperature):
    """Konvertiert Fahrenheit nach Celsius."""
    return (temperature - 32) * 5/9

def unit_input(selection):
    """Gibt die Eingabeeinheit basierend auf der Auswahl zurück."""
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
        return 'Unbekannt'

def unit_output(selection):
    """Gibt die Ausgabeeinheit basierend auf der Auswahl zurück."""
    if selection == 1:
        return 'Kelvin'
    elif selection == 2:
        return 'Fahrenheit'
    elif selection == 3:
        return 'Celsius'
    elif selection == 4:
        return 'Fahrenheit'
    elif selection == 5:
        return 'Celsius'
    elif selection == 6:
        return 'Kelvin'
    else:
        return 'Unbekannt'

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

# Verwende die unit_input Funktion, um die richtige Einheit anzugeben
temperature = float(input(f"Gib eine Temperatur in {unit_input(selection)} ein: "))

# Umrechnung durchführen basierend auf der Benutzerauswahl
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
else:
    converted_temp = None  # Ungültige Auswahl

# Ergebnis anzeigen
if converted_temp is not None:
    print(f"{temperature}° {unit_input(selection)} ≅ {converted_temp}° {unit_output(selection)}")
else:
    print("Ungültige Auswahl.")
