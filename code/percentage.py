def visualize(percentage):
    print(f"{percentage}%: {'* ' * (percentage // 10)}") # integer divison durch 10, um eine zahl zwischen 1 und 10 zu erhalten

percentages = [33, 50, 22, 70, 12, 90]
for percentage in percentages:
    visualize(percentage)