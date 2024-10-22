
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl


def init_grid(grid):
    """ draws a list of colors in the range of 0 to 10 as an image """
    global fig, handle
    fig = plt.figure()
    handle = plt.imshow(grid, cmap='Reds', norm=mpl.colors.Normalize(vmin=0, vmax=10))

    return fig, handle


def update_grid(grid):
    """ draws a list of colors in the range of 0 to 10 as an image """
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
    # This function resets the global variable 'heart' to its initial state 'HEART'
    global heart
    heart = HEART


def circshift_left_to_right():
    # This function performs a circular shift of each row in the 'heart' grid to the right.
    global heart
    for i in range(len(heart)):
        # For each row, move the last element to the first position and shift all other elements to the right.
        heart[i] = [heart[i][-1]] + heart[i][:-1]

def circshift_top_to_bottom():
    global heart
    last_row = heart[-1]  # Store the last row
    for i in range(len(heart) - 1, 0, -1):
        heart[i] = heart[i - 1]  # Shift each row down by one position
    heart[0] = last_row  # Set the first row to the last row


if __name__ == '__main__':
    global fig, handle
    fig, handle = init_grid(heart)
    plt.pause(0.25)
    for n in range(len(heart[0])):
        circshift_left_to_right()
        update_grid(heart)
        plt.pause(0.25)
    for n in range(len(heart)):
        circshift_top_to_bottom()
        update_grid(heart)
        plt.pause(0.25)
    plt.show()
