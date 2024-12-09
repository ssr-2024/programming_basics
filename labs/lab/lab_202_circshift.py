

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
    global heart
    heart = HEART


def circshift_left_to_right():
    global heart
    heart = np.roll(heart, shift=1, axis=1)

def circshift_top_to_bottom():
    global heart
    heart = np.roll(heart, shift=1, axis=0)


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