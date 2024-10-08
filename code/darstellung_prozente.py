#Darstellung der Prozentpunkte mit Sternen

def prozente(zahl):
    zahl = int(zahl) // 10
    print(zahl * "*")

zahl = input("Geben Sie Ihre Prozentzahl an: ")
prozente(zahl)
