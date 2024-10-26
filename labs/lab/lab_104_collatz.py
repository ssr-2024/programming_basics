

def collatz(n):
    if n % 2 == 0:
        return n // 2
    else:
        return 3 * n + 1

def run():
    liste = []
    n = int(input("Please enter a number: "))
    liste.append(n)
    
    while n != 1:
        n = collatz(n)
        liste.append(n)
    
    print(liste)
    return liste

def run():
    liste = []
    n = int(input("Please enter a number: "))
    liste.append(n)
    count_ones = 0
    
    while count_ones < 3:
        n = collatz(n)
        liste.append(n)
        if n == 1:
            count_ones += 1
    
    print(liste)
    return liste

