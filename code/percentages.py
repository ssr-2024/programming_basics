""""
This function represents any number in form of '*'. 
For every 10 it gets one more '*'
"""
def visualize(percentage):
    print(f"{percentage}%: {'* ' * (percentage//10)}")

percentages = [10, 29, 33, 92, 72, 73, 37]

for percentage in percentages:
    visualize(percentage)

