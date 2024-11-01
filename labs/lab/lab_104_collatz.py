# Create an UML diagram for the collatz problem
'''
mermaid
graph TD
    A[Start with n > 0] --> B[Print the value of n]
    B --> C{Is n even?}
    C -- Yes --> D[n = n / 2]
    C -- No --> E[n = 3 * n + 1]
    D --> B
    E --> B
'''

def collatz(a: int) -> int: 
    """
    Returns the next number in the Collatz sequence for a given number.

    Parameters  
    ----------
    a: int
        The current number in the Collatz sequence to be processed.

    Returns 
    -------
    int
        The next number in the Collatz sequence.
    """
    if a % 2 == 0:
        a = a//2
    else:
        a = a*3+1
    return a

def run()-> list:
    """
    Returns a list of the Collatz sequence for a given number, until 1 is reached 3 times.

    Parameters  
    ----------
    None

    Returns
    -------
    list
        A list containing the Collatz sequence for a given number, until 1 is reached 3 times.
    
    """
    liste = []
    a = int(input("Please enter a number"))
    liste.append(a)
    zaehler = 0
    while zaehler < 3:
        a = collatz(a)
        liste.append(a)
        if a == 1:
            zaehler += 1
    
    print(liste)
    return liste

if __name__ == '__main__':
    run()