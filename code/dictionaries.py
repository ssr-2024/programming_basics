def print_results(name, percentage):
    print(f"{name}: {'*' * (percentage//10)}")

# Dictionary that stores number successfull tests for different people (important: keys must be unique)
successfull_tests = {
    "Max" : 100,
    "Remo": 61,
    "Lars": 42,
    "Lana": 87,
    "Elio": 90
}

for name, percentage in successfull_tests.items():
    print_results(name, percentage)