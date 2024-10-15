
def triangle(size):
    for i in range(-size, size, 1):
        if i < 0:
            print('* ' * abs(size+i))
        else:
            print('* ' * (size-i))



for i in [1, 2, 5, 8]:
    triangle(i)

