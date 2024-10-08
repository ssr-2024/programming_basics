def print_result(name,percentage):
    print(f"{name}: {'*'*(percentage//10)}")

successful_tests = {
    'Janis': 44,
    'Matthieu': 55,
    'Jonathan': 63,
    'Robin': 78,
    'Nicolas1': 72,
    'Eliane': 77,
    'Johanna': 82,
    'Nicolas2': 87,
    'Elias': 93, 
}

for name, percentage in successful_tests.items():
    print_result(name, percentage)