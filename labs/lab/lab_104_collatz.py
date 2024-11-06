def collatz(n):
    """Berechnet den nächsten Wert in der Collatz-Sequenz für eine gegebene Zahl.

    Parameters
    ----------
    n : int
        Die aktuelle Zahl, für die der nächste Collatz-Wert berechnet wird.

    Returns
    -------
    int
        Der nächste Wert in der Collatz-Sequenz.
    """
    # Wenn n gerade ist, teile es durch 2; andernfalls wende die Collatz-Funktion 3*n + 1 an
    if n % 2 == 0:
        return n // 2
    else:
        return 3 * n + 1


def run():
    """Generiert die Collatz-Sequenz für eine eingegebene Zahl bis zum Erreichen von 1.

    Returns
    -------
    list
        Eine Liste der Zahlen in der Collatz-Sequenz bis zur 1.
    """
    liste = []  # Initialisiert eine leere Liste, um die Collatz-Sequenz zu speichern
    n = int(input("Please enter a number: "))
    liste.append(n)

    # Führt die Collatz-Funktion wiederholt aus, bis die Zahl 1 erreicht wird
    while n != 1:
        n = collatz(n)
        liste.append(n)
    
    print(liste)  # Gibt die vollständige Collatz-Sequenz aus
    return liste


def run():
    """Generiert die Collatz-Sequenz und stoppt, nachdem die Zahl 1 dreimal erreicht wurde.

    Returns
    -------
    list
        Eine Liste der Zahlen in der Collatz-Sequenz bis zum dreimaligen Erreichen der 1.
    """
    liste = []  # Initialisiert eine leere Liste, um die Collatz-Sequenz zu speichern
    n = int(input("Please enter a number: "))
    liste.append(n)
    count_ones = 0  # Zählt die Anzahl der Male, die 1 erreicht wurde
    
    # Führt die Collatz-Funktion aus, bis die Zahl 1 dreimal erreicht wurde
    while count_ones < 3:
        n = collatz(n)
        liste.append(n)
        if n == 1:
            count_ones += 1  # Erhöht den Zähler, wenn 1 erreicht wurde
    
    print(liste)  # Gibt die Collatz-Sequenz bis zum dreimaligen Erreichen der 1 aus
    return liste
