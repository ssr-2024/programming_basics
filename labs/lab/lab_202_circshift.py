import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

def init_grid(grid):
    """Draws a list of colors in the range of 0 to 10 as an image."""
    global fig, handle
    fig = plt.figure()
    handle = plt.imshow(grid, cmap='Reds', norm=mpl.colors.Normalize(vmin=0, vmax=10))
    return fig, handle

def update_grid(grid):
    """Updates the displayed grid with a new list of colors in the range of 0 to 10."""
    global fig, handle
    handle.set_data(grid)
    fig.canvas.draw()
    fig.canvas.flush_events()

# Heart shape represented in a grid format with values from 0 to 10
HEART = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 9, 9, 9, 0, 0, 0, 0, 9, 9, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         # ... (remaining rows of HEART) ...
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

global heart
heart = HEART  # Initialize the heart grid as a global variable

def reset():
    """Resets the heart grid to its original shape."""
    global heart
    heart = HEART

def circshift_left_to_right():
    """Shifts each row of the grid one position to the left."""
    global heart
    heart = [row[-1:] + row[:-1] for row in heart]
    # row[-1:] takes the last element of the current row.
    # row[:-1] takes all elements of the row except the last.
    # By combining row[-1:] + row[:-1], the last element moves to the start of the row.

def circshift_top_to_bottom():
    """Shifts the entire grid one row upwards, with the last row moving to the top."""
    global heart
    heart = heart[-1:] + heart[:-1]
    # heart[-1:] takes the last row of the heart grid.
    # heart[:-1] takes all rows except the last.
    # By combining heart[-1:] + heart[:-1], the last row is moved to the top.

if __name__ == '__main__':
    # Initialize and display the heart grid
    global fig, handle
    fig, handle = init_grid(heart)
    plt.pause(0.25)
    
    # Shift the heart grid left to right and update the display
    for n in range(len(heart[0])):
        circshift_left_to_right()
        update_grid(heart)
        plt.pause(0.25)
    
    # Shift the heart grid top to bottom and update the display
    for n in range(len(heart)):
        circshift_top_to_bottom()
        update_grid(heart)
        plt.pause(0.25)
    
    plt.show()
