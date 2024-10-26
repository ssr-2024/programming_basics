'''import matplotlib.pyplot as plt
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
    """
    transposed_grid =  [([0] *len(smiley[0]))] * len(smiley[0])
    print(type(transposed_grid))
    for zeile in range(0,len(grid),1):
        for spalte in range(0,len(grid[0]),1):
                print(f"get element [{zeile}][{spalte}]) with value {grid[zeile][spalte]}.")
                transposed_grid[len(grid[0])-(spalte+1)][zeile] = grid[zeile][spalte]
                print(f"set element [{len(grid[0])-(spalte+1)}][{zeile}]) with value {transposed_grid[len(grid[0])-(spalte+1)][zeile]}.")
                print(transposed_grid[len(grid[0])-(spalte+1)][zeile])
        print(transposed_grid[len(grid[0])-(spalte+1)])
    #print(transposed_grid)
    """
    
    transposed_grid =  []
    for zeile in range(0,len(grid),1):
        line = []
        for spalte in range(0,len(grid[0]),1):
        #        print(f"get element [{zeile}][{spalte}]) with value {grid[zeile][spalte]}.")
                line.append(grid[len(grid)-zeile-1][spalte])
        transposed_grid.append(line)
                #print(f"set element [{len(grid[0])-(spalte+1)}][{zeile}]) with value {transposed_grid[len(grid[0])-(spalte+1)][zeile]}.")
                #print(transposed_grid[len(grid[0])-(spalte+1)][zeile])
        #print(transposed_grid[len(grid[0])-(spalte+1)])
    

    return transposed_grid


if __name__ == '__main__':
    print(summary([1, 2, 3, 4, 17]))

    
    draw_grid(draw_transposed_grid(smiley))
    draw_grid(draw_transposed_grid(heart))
'''

import matplotlib.pyplot as plt
import matplotlib as mpl

def draw_grid(grid):
    """Draws a 2D list of numbers (0 to 10) as an image with varying shades of red."""
    plt.imshow(grid, cmap='Reds', norm=mpl.colors.Normalize(vmin=0, vmax=10))
    plt.show()

def summary(array):
    """Returns a summary dictionary with min, max, sum, length, mean, and the raw array."""
    return {
        "min": min(array),
        "max": max(array),
        "sum": sum(array),
        "length": len(array),
        "mean": sum(array) / len(array),
        "raw": array
    }

def draw_transposed_grid(grid):
    """Returns a 2D list transposed (rotated 90° to the right)."""
    # Using zip to transpose rows and columns
    transposed_grid = [list(row) for row in zip(*grid)]
    return transposed_grid

# Test data for grids
smiley = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 9, 9, 9, 9, 9, 9, 9, 9, 0],
    [0, 9, 0, 0, 0, 0, 0, 0, 9, 0],
    [0, 9, 0, 9, 0, 9, 0, 0, 9, 0],
    [0, 9, 0, 0, 0, 9, 9, 0, 9, 0],
    [0, 9, 0, 0, 0, 9, 9, 0, 9, 0],
    [0, 9, 0, 9, 0, 9, 0, 0, 9, 0],
    [0, 9, 0, 0, 0, 0, 0, 0, 9, 0],
    [0, 9, 9, 9, 9, 9, 9, 9, 9, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

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

# Run the functions to test
if __name__ == '__main__':
    # Example use of summary function
    print(summary([2, 5, 3, 7]))

    # Drawing original and transposed grids
    print("Original Smiley:")
    draw_grid(smiley)
    print("Transposed Smiley:")
    draw_grid(draw_transposed_grid(smiley))

    print("Original Heart:")
    draw_grid(heart)
    print("Transposed Heart:")
    draw_grid(draw_transposed_grid(heart))
