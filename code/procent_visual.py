def visualize (percentage):
    print (f"{percentage}%: {'*' * (percentage // 10)}")
    ''' Diese Funktion visualisiert den Prozentsatz, den sie als Argument erhält.
        Sie gibt eine Zeile mit Sternchen aus, die die Prozentzahl darstellt.
        Aber es gibt nur ganze Sterne, keine halben. '''

percentages = [44, 33, 22]
for percentage in percentages:
    visualize(percentage)