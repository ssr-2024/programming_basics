
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl


def init_grid(grid):
    """
    Initializes a grid and draws a list of colors in the range of 0 to 10 as an image.
   
    Parameters
    ----------
    grid: np.ndarray
        A 2D numpy array representing the grid to be drawn.

    Returns
    -------
    tuple
        A tuple containing the figure and the image handle.
    """

    global fig, handle
    fig = plt.figure()
    handle = plt.imshow(grid, cmap='Reds', norm=mpl.colors.Normalize(vmin=0, vmax=10))

    return fig, handle


def update_grid(grid):
    """
    Updates the grid with new data and redraws the image.
   
    Parameters
    ----------
    grid: np.ndarray
        A 2D numpy array representing the new grid data.

    Returns
    -------
    None
    """
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


def circshift(array, shift, axis):
    """
    Shifts the elements of an array along the specified axis.
   
    Parameters
    ----------
    array: np.ndarray
        The array to be shifted.
    shift: int
        The number of positions by which elements are shifted.
    axis: int
        The axis along which elements are shifted.

    Returns
    -------
    np.ndarray
        The shifted array.
    """
    return np.roll(array, shift=shift, axis=axis)

def circshift_left_to_right():
    """
    Shifts the elements of the global 'heart' array one position to the right.
   
    Parameters
    ----------
    None

    Returns
    -------
    None
    """
    global heart
    heart = circshift(heart, shift=1, axis=1)


def circshift_top_to_bottom():
    """
    Shifts the elements of the global 'heart' array one position downwards.
   
    Parameters
    ----------
    None

    Returns
    -------
    None
    """
    global heart
    heart = circshift(heart, shift=1, axis=0)



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
