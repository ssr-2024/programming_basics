#programm, um namen und prozentzahlen aus dictionary auszugeben
successful_tests = {
    'marc': 100,
    'remo': 61,
    'lars': 42,
    'lana': 87,
    'elio': 70,
    'andi': 90
}
def print_result(name:str, percentage:float):
    """funktion, um name und prozentzahl auf einer separaten Zeile auszugeben
    wobei prozentzahl durch 10 geteilt wird und dann durch entsprechende Anzahl * ausgegeben wird
    """
    print(f'{name}: {'*' * (percentage // 10)}')

#gebe alle namen und prozentzahlen aus
print('Successful tests: [name, percentage]')
for name, percentage in successful_tests.items():
    print_result(name,percentage)