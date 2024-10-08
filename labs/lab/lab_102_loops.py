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

# Example call:
triangle(5)
