'''mermaid
graph TD
    A[Start: n > 0] --> B[Zahl n ausgeben]
    B --> C{Ist n gerade?}
    C -- Ja --> D[n = n / 2]
    C -- Nein --> E[n = 3n + 1]
    D --> F[Zahl ausgeben]
    E --> F[Zahl ausgeben]
    F --> C
    C --> G{n == 1?}
    G -- Ja --> H[Ende]
    G -- Nein --> C
'''


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