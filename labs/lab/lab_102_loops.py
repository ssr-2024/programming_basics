
def triangle(size):
    for i in range(1, size + 1):
        print('* ' * i)  
    for i in range(size - 1, 0, -1):
        print('* ' * i) 

triangle(1)
print()

triangle(2)
print()

triangle(5)
print()

'''
Alternative Lösung innerhalb einer for-Schleife:
def triangle(size):
    # Gesamtanzahl der Zeilen, die ausgegeben werden sollen
    total_lines = size * 2 - 1  # Größe des aufsteigenden und absteigenden Dreiecks

    for i in range(1, total_lines + 1):
        if i <= size:
            # Aufsteigendes Dreieck
            print('* ' * i)
        else:
            # Absteigendes Dreieck
            print('* ' * (total_lines - i + 1))
'''