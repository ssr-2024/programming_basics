
def triangle(size):
   
    for i in range(1, size * 2):
        num_stars = i if i <= size else 2 * size - i
        print("*   " * num_stars)

triangle(1)
print("\n")
triangle(2)
print("\n")
triangle(5)




