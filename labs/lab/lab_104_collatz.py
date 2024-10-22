def collatz(a:int):
    """
    function to caculate the next collatz-number

    Parameters
    ----------
    a: int
        the input number

    Returns
    -------
    int
        the following collatz-number

    """
    if a % 2 == 0:#if a is even
        a = a//2 #returns integer
    else:#if a is uneven
        a = a*3+1
    return a

def run():
    """
    calculates the collatz-numbers, until 1 is reached 3 times

    Parameters
    ----------
    None

    Returns
    -------
    list    
        list of collatz-numbers 
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

if __name__ == '__main__': #is run, if not imported 
    run()