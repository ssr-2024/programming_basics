
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
