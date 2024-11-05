def triangle(size):
    for i in range(1, size + 1):
        # Berechne die Anzahl der Leerzeichen und Sterne
        spaces = size - i
        stars = 2 * i - 1
        # Zeichne die Leerzeichen und Sterne
        print(" " * spaces + "*" * stars)

triangle(n)
n=int(input("gib eine Zahl ein"))
