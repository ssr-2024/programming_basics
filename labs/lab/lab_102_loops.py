def triangle(size):
    for i in range(1, size * 2):
        if i <= size:
            print('*   ' * i)
        else:
            print('*   ' * (size * 2 - i))

# Beispiele
triangle(1)
print()
triangle(2)
print()
triangle(5)
