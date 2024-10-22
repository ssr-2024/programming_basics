'''
from typing import NoReturn

def triangle(n: int) -> NoReturn:
    """Prints a pattern of stars in the shape of an ascending and descending triangle.

    Parameters
    ----------
    n (int): 
        The number of lines in the ascending part of the star pattern.

    Returns:
    ----------
    NoReturn: This function does not return a value.
    """
    for i in range(1, n + 1):
        print("* " * i)
    for i in range(n - 1, 0, -1):
        print("* " * i)

triangle(5)
'''

def triangle(size):
    for i in range(1, 2 * size):
        # Erhöhe bis n und dann verringere die Anzahl der Sterne
        stars = i if i <= size else 2 * size - i
        print("*  " * 1)

triangle(5)
