# @exercise_uml
def begruessung(spam):
    if spam == 1:
        print("Hello")
    elif spam == 2:
        print("Howdy")
    else:
        print("Greetings!")

spam = int(input("Geben sie 1, 2 oder eine andere beliebige Zahl ein für eine Begrüssung: "))

begruessung(spam)