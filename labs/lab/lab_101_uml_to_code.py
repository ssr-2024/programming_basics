# @exercise_uml

# Eingabe des Wertes von spam durch den Benutzer. Mit int() wird der Wert in eine Ganzzahl umgewandelt. Und mit input() wird der Wert vom Benutzer abgefragt.
spam = int(input("Bitte gib einen Wert zwischen 1 und 3 ein.: "))

# Der eingegebene Wert wird überprüft und die entsprechende Ausgabe wird ausgegeben.
if spam == 1:
    print("Hello")
elif spam == 2:
    print("Howdy")
else:
    print("Greetings!")