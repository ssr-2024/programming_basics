def collatz(a):
    if a % 2 == 0:
        a = a//2 
    else:
        a = a*3+1
    return a

def run():
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