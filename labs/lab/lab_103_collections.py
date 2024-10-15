import matplotlib.pyplot as plt
import matplotlib as mpl


def draw_grid(grid):
    """ draws a list of colors in the range of 0 to 10 as an image """
    plt.imshow(grid, cmap='Reds', norm=mpl.colors.Normalize(vmin=0, vmax=10))
    plt.show()


def summary(array):
    # => {
#       min: 2,
#       max: 7,
#       sum: 17,
#       length: 4,
#       mean: 4.25,
#       raw: [2, 5, 3, 7]
#    }

    """
    my_summary = {
    my_summary["min"] = min(array)
    my_summary["max"] = max(array)
    my_summary["sum"] = sum(array)
    my_summary["length"] = len(array)
    my_summary["mean"] = sum(array)/len(array)
    my_summary["raw"] = array
    """

    # nicht mehr mit 3.11.6 möglich
    my_summary =  {
        "min": min(array),
        "max": max(array),
        "sum": sum(array),
        "length": len(array),
        "mean": sum(array)/len(array),
        "raw": array
    }

    return my_summary


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


def draw_transposed_grid(grid):
    # Transponiert die Liste, indem die Spalten zu Zeilen gemacht werden.
    transposed_grid = []
    for spalte in range(len(grid[0])):  # Durchlaufe die Spalten der Original-Liste
        new_row = []
        for zeile in range(len(grid)):  # Durchlaufe die Zeilen der Original-Liste
            new_row.append(grid[zeile][spalte])  # Füge das Element zur neuen Zeile hinzu
        transposed_grid.append(new_row)  # Neue Zeile zur transponierten Liste hinzufügen
    return transposed_grid



if __name__ == '__main__':
    print(summary([1, 2, 3, 4, 17]))

    
    draw_grid(draw_transposed_grid(smiley))
    draw_grid(draw_transposed_grid(heart))
