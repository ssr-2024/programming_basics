import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl


def init_grid(grid):
    """Initialisiert die Anzeige eines Gitters als Bild und stellt Farben im Bereich von 0 bis 10 dar.

    Parameters
    ----------
    grid : list
        2D-Liste, die die Werte des Gitters enthält.

    Returns
    -------
    tuple
        Das figure-Objekt und das handle-Objekt, um das Bild zu aktualisieren.
    """
    # Initialisiert die Grafik und stellt das Gitter als Bild dar
    global fig, handle
    fig = plt.figure()
    handle = plt.imshow(grid, cmap='Reds', norm=mpl.colors.Normalize(vmin=0, vmax=10))

    return fig, handle


def update_grid(grid):
    """Aktualisiert das angezeigte Gitterbild mit neuen Werten.

    Parameters
    ----------
    grid : list
        2D-Liste, die die neuen Werte des Gitters enthält.

    Returns
    -------
    None
    """
    # Aktualisiert die Grafikdaten und zeichnet das Bild neu
    global fig, handle
    handle.set_data(grid)
    fig.canvas.draw()
    fig.canvas.flush_events()

 

HEART = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 9, 9, 9, 0, 0, 0, 0, 9, 9, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 9, 9, 7, 9, 9, 0, 0, 9, 9, 7, 9, 9, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 9, 9, 7, 0, 7, 9, 9, 9, 9, 7, 7, 7, 9, 9, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 9, 9, 7, 0, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 9, 9, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 9, 7, 0, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 9, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 9, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 9, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 9, 9, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 8, 9, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 9, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 8, 9, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 9, 9, 7, 7, 7, 7, 7, 7, 7, 7, 7, 8, 9, 9, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 9, 7, 7, 7, 7, 7, 7, 7, 7, 7, 8, 9, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 9, 7, 7, 7, 7, 7, 7, 7, 8, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 7, 7, 7, 7, 7, 8, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 7, 7, 7, 8, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 7, 8, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

global heart
heart = HEART


def reset():
    """Setzt das Herz-Gitter auf seinen ursprünglichen Zustand zurück.

    Returns
    -------
    None
    """
    global heart
    heart = HEART


def circshift(array, shift, axis):
    """Verschiebt die Elemente eines Arrays zirkulär.

    Parameters
    ----------
    array : np.ndarray
        Das zu verschiebende Array.
    shift : int
        Anzahl der Positionen, um die die Elemente verschoben werden.
    axis : int
        Achse, entlang der verschoben wird (0 für Zeilen, 1 für Spalten).

    Returns
    -------
    np.ndarray
        Das zirkulär verschobene Array.
    """
    return np.roll(array, shift=shift, axis=axis)


def circshift_left_to_right():
    """Verschiebt das Herz-Gitter zirkulär um eine Spalte nach rechts.

    Returns
    -------
    None
    """
    global heart
    heart = circshift(heart, shift=1, axis=1)


def circshift_top_to_bottom():
    """Verschiebt das Herz-Gitter zirkulär um eine Zeile nach unten.

    Returns
    -------
    None
    """
    global heart
    heart = circshift(heart, shift=1, axis=0)


if __name__ == '__main__':
    # Initialisiert das Gitter und zeigt es an
    global fig, handle
    fig, handle = init_grid(heart)
    plt.pause(0.25)

    # Verschiebt das Gitter zirkulär von links nach rechts
    for n in range(len(heart[0])):
        circshift_left_to_right()
        update_grid(heart)
        plt.pause(0.25)

    # Verschiebt das Gitter zirkulär von oben nach unten
    for n in range(len(heart)):
        circshift_top_to_bottom()
        update_grid(heart)
        plt.pause(0.25)

    plt.show()