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
    """ transposes a grid

    Parameters:
    -----------
    grid: list of lists
        a grid of numbers
    
    Returns:
    --------
    list of lists
    """

    #transposing the grid (usual matrix transposition)
    transposed_grid =  []
    for zeile in range(len(grid[0])):
        line = []
        for spalte in range(len(grid)):
        #        print(f"get element [{zeile}][{spalte}]) with value {grid[zeile][spalte]}.")
                line.append(grid[spalte][zeile])
        transposed_grid.append(line)
    return transposed_grid


"""
#rotating the grid by 90 degrees clockwise
    transposed_grid =  []
    for spalte in range(len(grid[0])):
        line = []
        for zeile in range(len(grid)):
        #        print(f"get element [{zeile}][{spalte}]) with value {grid[zeile][spalte]}.")
                line.append(grid[len(grid)-zeile-1][spalte])
        transposed_grid.append(line)
                #print(f"set element [{len(grid[0])-(spalte+1)}][{zeile}]) with value {transposed_grid[len(grid[0])-(spalte+1)][zeile]}.")
                #print(transposed_grid[len(grid[0])-(spalte+1)][zeile])
        #print(transposed_grid[len(grid[0])-(spalte+1)])
    return transposed_grid
"""
    

if __name__ == '__main__':
    print(summary([1, 2, 3, 4, 17]))

    
    print(f'{draw_transposed_grid([[1, 2, 3, 4, 5, 6, 7, 8, 9],
                      [9, 8, 7, 6, 5, 4, 3, 2, 1]]
)}')
    
    draw_grid(smiley)
    draw_grid(heart)
    draw_grid(draw_transposed_grid(smiley))
    draw_grid(draw_transposed_grid(heart))
