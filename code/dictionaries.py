def print_result (name,percentage):
    print(f"{name}: {'*'*(percentage//10)}")

successful_tests = {
    'Janis' : 44,
    'Peter' : 33,
    'George' : 22,

}

for name, percentage in successful_tests.items():
    print_result(name,percentage)
