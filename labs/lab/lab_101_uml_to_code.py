# @exercise_uml
def begruessung(spam):
    if spam == 1:
        return "Hello"
    if spam == 2:
        return "Howdy"
    else:
        return "Greetings"
    
spam = int(input("Geben sie 1, 2 oder eine andere beliebige Zahl ein für eine Begrüssung: "))
begruessung(spam)