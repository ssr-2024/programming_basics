#Darstellung der Prozentpunkte mit Sternen

def prozente(zahl):
    zahl = int(zahl) // 10
    print(F"{zahl}%: {zahl * "*"}")

#zahl = input("Geben Sie Ihre Prozentzahl an: ")
zahl = [33,55, 20, 15, 89]
for zahl in zahl:
    prozente(zahl)
