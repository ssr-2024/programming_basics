
def triangle(size):
    """Prints a symmetric triangle pattern using asterisks, with a top and bottom part.

    Parameters
    -----------

    size: int
        The number of lines in the top part of the triangle, and also determines the overall height of the triangle.

    Returns
    --------

        None
    """    
    # Erste Schleife: Erstellt den oberen Teil des Dreiecks
    # Die Schleife startet bei 1, da die erste Zeile nur ein Stern enthält
    # Für jeden Wert von i wird i-mal die Zeichenkette '*   ' gedruckt, um die Anzahl der Sterne pro Zeile zu erhöhen
    for i in range(1, size + 1):
        print('*   ' * i)
    
    # Zweite Schleife: Erstellt den unteren Teil des Dreiecks
    # Die Schleife startet bei (size - 1) und läuft bis 1 (exklusiv der 0)
    # Für jeden Wert von i wird i-mal die Zeichenkette '*   ' gedruckt, um die Anzahl der Sterne pro Zeile zu verringern
    for i in range(size - 1, 0, -1):
        print('*   ' * i)

triangle(5)
print()