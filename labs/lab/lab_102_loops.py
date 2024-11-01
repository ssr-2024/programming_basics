def triangle(size: int) --> None:
    """Draws a symmetrical triangle of stars with the given size.

    This function prints an upper and a lower triangle made of asterisks ('*') 
    that together form a diamond-like shape. The upper triangle has a growing 
    number of asterisks in each row, while the lower triangle has a decreasing 
    number.

    Parameters
    ----------
    size: int
        The number of rows in the upper triangle and the height of the 
        diamond-like shape (2 * size - 1). The lower triangle will have 
        one row less than the specified size.
    
    Returns
    ----------
    None
       
    """
    
    # Loop 1: Draws the upper triangle
    for i in range(size):
        print('* ' * (i + 1))
    
    # Loop 2: Draws the lower triangle
    for i in range(size - 1):
        print('* ' * (size - i - 1))

# Call the function
triangle(1)
triangle(2)
triangle(5)