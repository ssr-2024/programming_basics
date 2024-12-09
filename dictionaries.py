def print_result (name,percentage): 
    print (f"{name}: {'* ' * (percentage // 10)}")

successful_tests = { 
    'marc' :100,
    'remo' :61,
    'lars' :42,
    'lana' :87,
    'elio' :70,
    'andi' :90
}


for name, percentage in successful_tests.items():
    print_result (name,percentage)

