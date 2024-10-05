
def triangle(size):
    for i in range(-size, size, 1):
        if i < 0:
            print('* ' * abs(size+i))
        else:
            print('* ' * (size-i))


triangle(1)

for i in range(2,9,3):
    triangle(i)

