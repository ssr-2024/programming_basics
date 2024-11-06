import matplotlib.pyplot as plt
import matplotlib as mpl


def draw_grid(grid: list[list[int]]) -> None:
    """Zeichnet ein Gitter als Heatmap basierend auf den übergebenen Werten.

    Parameters
    ----------
    grid : list[list[int]]
        2D-Liste von Zahlen, die die Farben des Gitters darstellen.

    Returns
    -------
    None
    """
    # Visualisiert das Gitter mit der "Reds" Farbskala und normalisiert zwischen 0 und 10
    plt.imshow(grid, cmap='Reds', norm=mpl.colors.Normalize(vmin=0, vmax=10))
    plt.show()


def summary(values: list[int]) -> dict[str, int | float | list[int]]:
    """Erstellt eine Zusammenfassung der gegebenen Liste von Werten.

    Parameters
    ----------
    values : list[int]
        Eine Liste von Zahlen, aus der die Statistik berechnet wird.

    Returns
    -------
    dict
        Ein Wörterbuch mit Minimum, Maximum, Summe, Länge, Mittelwert und der ursprünglichen Liste.
    """
    # Berechnet verschiedene statistische Kennzahlen für die Liste
    my_summary = {
        "min": min(values),  # Mindestwert
        "max": max(values),  # Höchstwert
        "sum": sum(values),  # Summe aller Werte
        "length": len(values),  # Anzahl der Werte
        "mean": sum(values) / len(values),  # Durchschnitt
        "raw": values  # Gibt die ursprüngliche Liste zurück
    }

    return my_summary


# Gitter-Daten, die ein Herz und ein Smiley darstellen
heart = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 9, 9, 9, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 9, 9, 7, 7, 9, 9, 9, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 9, 9, 7, 0, 7, 7, 7, 9, 9, 0, 0, 0, 0, 0, 0],
    [0, 9, 9, 7, 0, 7, 7, 7, 7, 7, 7, 9, 0, 0, 0, 0, 0],
    [0, 9, 7, 0, 7, 7, 7, 7, 7, 7, 7, 7, 9, 0, 0, 0, 0],
    [0, 9, 9, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 9, 0, 0, 0],
    [0, 0, 9, 9, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 9, 0, 0],
    [0, 0, 0, 9, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 9, 0],
    [0, 0, 0, 9, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 8, 9, 0],
    [0, 0, 9, 9, 7, 7, 7, 7, 7, 7, 7, 7, 7, 8, 9, 0, 0],
    [0, 9, 9, 7, 7, 7, 7, 7, 7, 7, 7, 7, 8, 9, 0, 0, 0],
    [0, 9, 7, 7, 7, 7, 7, 7, 7, 7, 7, 8, 9, 0, 0, 0, 0],
    [0, 9, 9, 7, 7, 7, 7, 7, 7, 8, 8, 9, 0, 0, 0, 0, 0],
    [0, 0, 9, 9, 7, 7, 7, 7, 8, 9, 9, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 9, 9, 7, 7, 8, 9, 9, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 9, 9, 9, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

smiley = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 9, 9, 9, 9, 9, 9, 9, 9, 0],
          [0, 9, 0, 0, 0, 0, 0, 0, 9, 0],
          [0, 9, 0, 9, 0, 9, 0, 0, 9, 0],
          [0, 9, 0, 0, 0, 9, 9, 0, 9, 0],
          [0, 9, 0, 0, 0, 9, 9, 0, 9, 0],
          [0, 9, 0, 9, 0, 9, 0, 0, 9, 0],
          [0, 9, 0, 0, 0, 0, 0, 0, 9, 0],
          [0, 9, 9, 9, 9, 9, 9, 9, 9, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]


def draw_transposed_grid(grid: list[list[int]]) -> list[list[int]]:
    """Transponiert das übergebene Gitter um 90 Grad nach rechts.

    Parameters
    ----------
    grid : list[list[int]]
        2D-Liste von Zahlen, die das ursprüngliche Gitter darstellen.

    Returns
    -------
    list[list[int]]
        Ein neues Gitter, das um 90 Grad nach rechts gedreht ist.
    """
    # Initialisiert die Liste für das transponierte Gitter
    transposed_grid = []

    # Iteriert durch jede Spalte und erstellt Zeilen für das transponierte Gitter
    for spalte in range(len(grid[0])):
        line = []
        for zeile in range(len(grid)):
            line.append(grid[zeile][spalte])  # Fügt das transponierte Element hinzu
        transposed_grid.append(line)

    return transposed_grid


if __name__ == '__main__':
    # Beispiel für die summary-Funktion
    print(summary([1, 2, 3, 4, 17]))

    # Zeichnet die transponierten Gitter
    draw_grid(draw_transposed_grid(smiley))
    draw_grid(draw_transposed_grid(heart))