def visualize (percentage):
    print (f"{percentage}%: {'* ' * (percentage // 10)}")


visualize (33)
visualize (50)
visualize (22)
visualize (70)
visualize (12)
visualize (90)

percentages = [33, 50, 22, 70, 12, 90]
for percentage in percentages:
    visualize(percentage)


