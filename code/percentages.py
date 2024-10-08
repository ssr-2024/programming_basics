""""
This function represents any number in form of '*'. 
For every 10 it gets one more '*'
"""
def visualize(percentage):
    print(f"{percentage}%: {'* ' * (percentage//10)}")

test_variable = "im a test variable"

visualize(10)
visualize(74)
visualize(99)
visualize(82)
visualize(12)
visualize(55)
