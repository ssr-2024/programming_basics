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


def draw_transposed_grid(grid: list) -> list:
    """ Transposes a 2D grid (list of lists) by swapping rows and columns 
    
    Parameters
    ----------
    grid: list of lists
        A 2D list representing the original grid to be transposed. 

    Returns
    ----------
    transposed_grid: list of lists
        A 2D list representing the transposed grid. 
    """
    # Initialize an empty list to hold the transposed grid
    transposed_grid = []
    
    # Iterate over each column in the original grid
    for zeile in range(len(grid[0])):  # len(grid[0]) gives the number of columns in the original grid
        # Initialize an empty list to hold the current line of the transposed grid
        line = []
        
        # Iterate over each row in the original grid
        for spalte in range(0, len(grid)):  # len(grid) gives the number of rows in the original grid
            # Append the element from the original grid to the current line
            # The element is taken from the current row (spalte) and the current column (zeile)
            line.append(grid[spalte][zeile])
        
        # Append the current line to the transposed grid
        transposed_grid.append(line)
    
    # Return the transposed grid
    return transposed_grid


if __name__ == '__main__':
    print(summary([1, 2, 3, 4, 17]))

    
    draw_grid(draw_transposed_grid(smiley))
    draw_grid(draw_transposed_grid(heart))
