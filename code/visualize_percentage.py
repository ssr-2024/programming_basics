#Visualisierung von Prozentzahlen, wobei ein Sternchen für je 10 Prozentpunkte ausgegeben wird

def visualize(percentage):
    print(f"{percentage}%: {'* ' * (percentage//10)}") 
    
    # Teilt die Prozentzahl durch 10, um für je 10% ein Sternchen (*) zu erzeugen.

visualize(33)
visualize(50)
visualize(22)
visualize(70)
visualize(12)
visualize(90)

#Visualisierung von Prozentzahlen anhand von Sammeldatentypen

percentages = [33, 50, 22, 70, 12, 90]

for percentage in percentages:
    visualize(percentage)
    
