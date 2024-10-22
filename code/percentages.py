from typing import List,Dict



def visualize(percentage):
    print(f"{percentage}%: {'*'*(percentage//10)}")



# visualize(13)
# visualize(43)


percentages = [13, 43, 67, 90, 100]
for percentage in percentages:
    visualize(percentage)