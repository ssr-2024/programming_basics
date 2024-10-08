
def print_result(name,percentage):
    print(f"{name}: {'*' * (percentage // 10)}")

sucessfull_tests = {
    'Janis':44,
    'Matthieu':55,
    'Jonathan':63,
    'Robin':68,
    'Elias':99,
    'Nicolas1':20,
    'Nicolas2':7
}

for name,percentage in sucessfull_tests.items():
    print_result(name,percentage)



