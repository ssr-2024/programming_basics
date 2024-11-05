def triangle(size):
    """
    Draws a right-facing triangle that expands to the specified size and then contracts.

    Parameters
    ----------
    size : int
        The maximum width of the triangle.
    """
    # First, build the increasing part of the triangle
    for i in range(1, size + 1):
        # Print each line with an increasing number of stars
        print("*" * i)
    
    # Then, build the decreasing part of the triangle
    for i in range(size - 1, 0, -1):
        # Print each line with a decreasing number of stars
        print("*" * i)

# Get user input for the triangle size
n = int(input("Enter a number: "))
triangle(n)
