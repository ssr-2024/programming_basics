def kelvin_to_celsius(temperatur):
    """Konvertiert eine Temperatur von Kelvin nach Celsius.

    Parameters
    ----------
    temperatur : float
        Temperatur in Kelvin.

    Returns
    -------
    float
        Temperatur in Celsius.
    """
    return temperatur - 273.15

def celsius_to_kelvin(temperatur):
    """Konvertiert eine Temperatur von Celsius nach Kelvin.

    Parameters
    ----------
    temperatur : float
        Temperatur in Celsius.

    Returns
    -------
    float
        Temperatur in Kelvin.
    """
    return temperatur + 273.15


def celsius_to_fahrenheit(temperatur):
    """Konvertiert eine Temperatur von Celsius nach Fahrenheit.

    Parameters
    ----------
    temperatur : float
        Temperatur in Celsius.

    Returns
    -------
    float
        Temperatur in Fahrenheit.
    """
    return (temperatur * 9 / 5) + 32


def fahrenheit_to_celsius(temperatur):
    """Konvertiert eine Temperatur von Fahrenheit nach Celsius.

    Parameters
    ----------
    temperatur : float
        Temperatur in Fahrenheit.

    Returns
    -------
    float
        Temperatur in Celsius.
    """
    return (temperatur - 32) * 5 / 9


def kelvin_to_fahrenheit(temperatur):
    """Konvertiert eine Temperatur von Kelvin nach Fahrenheit.

    Parameters
    ----------
    temperatur : float
        Temperatur in Kelvin.

    Returns
    -------
    float
        Temperatur in Fahrenheit.
    """
    return (temperatur - 273.15) * 9 / 5 + 32


def fahrenheit_to_kelvin(temperatur):
    """Konvertiert eine Temperatur von Fahrenheit nach Kelvin.

    Parameters
    ----------
    temperatur : float
        Temperatur in Fahrenheit.

    Returns
    -------
    float
        Temperatur in Kelvin.
    """
    return (temperatur - 32) * 5 / 9 + 273.15


def unit_input(selection):
    """Gibt die Einheit der Eingabetemperatur basierend auf der Auswahl zurück.

    Parameters
    ----------
    selection : int
        Auswahl des Benutzers für die gewünschte Konvertierung.

    Returns
    -------
    str
        Die Einheit der Eingabetemperatur.
    """
    # Gibt die korrekte Eingabeeinheit basierend auf der Auswahl des Benutzers zurück
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
    """Gibt die Einheit der Ausgabetemperatur basierend auf der Auswahl zurück.

    Parameters
    ----------
    selection : int
        Auswahl des Benutzers für die gewünschte Konvertierung.

    Returns
    -------
    str
        Die Einheit der Ausgabetemperatur.
    """
    # Gibt die korrekte Ausgabeeinheit basierend auf der Auswahl des Benutzers zurück
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



# Fragt den Benutzer nach der gewünschten Konvertierungsart
selection = int(input('Please enter the number corresponding to the conversion you want to do:\n'
                      '(1) Celsius to Kelvin\n'
                      '(2) Celsius to Fahrenheit\n'
                      '(3) Kelvin to Celsius\n'
                      '(4) Kelvin to Fahrenheit\n'
                      '(5) Fahrenheit to Celsius\n'
                      '(6) Fahrenheit to Kelvin\n'
                      'Your choice: '))

# Fragt den Benutzer nach der Eingabetemperatur basierend auf der Auswahl
temperatur = float(input(f'Please enter a temperature in {unit_input(selection)}: '))



# Führt die entsprechende Konvertierung basierend auf der Auswahl durch
if selection == 1:
    converted_temp = celsius_to_kelvin(temperatur)
elif selection == 2:
    converted_temp = celsius_to_fahrenheit(temperatur)
elif selection == 3:
    converted_temp = kelvin_to_celsius(temperatur)
elif selection == 4:
    converted_temp = kelvin_to_fahrenheit(temperatur)
elif selection == 5:
    converted_temp = fahrenheit_to_celsius(temperatur)
elif selection == 6:
    converted_temp = fahrenheit_to_kelvin(temperatur)

# Gibt die konvertierte Temperatur und die entsprechenden Einheiten aus
print(f'{temperatur}° {unit_input(selection)} ≅ {converted_temp}° {unit_output(selection)}')
