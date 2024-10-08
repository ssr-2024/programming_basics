def print_result(name, percentage):
    print (f"{name}: {'* ' * (int(percentage)//10)}") 

successful_tests = {
    'Janis':44,
    'Matthieu': 55,
    'Jonathan': 63,
    'Robin': 68,
    'Nicolas':72,
    'Eliane':77,
    'Johanna': 82,
    'Nicolas I': 87.8, #Keys müssen immer eindeutig sein
    'Elias':93

}

for name, percentage in successful_tests.items():
    print_result(name, percentage)

