# Use the continue-statement within a while-loop

while True:
    print('Who are you?')
    name=input()
    if name !='Johanna':
        continue
    print('Hello, Johanna. What is the password? (It is a fish.)')
    password=input()
    if password == 'swordfish':
        break
print('Access granted.')
