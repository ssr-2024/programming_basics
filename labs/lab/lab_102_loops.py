
def triangle(size):
    for i in range(1, (2*size)+1):
        if i < size+1:
            print("* " * i)
        else:
            print("* " * (2*size-i))
    print('')


triangle(4)
