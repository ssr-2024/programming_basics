# @exercise_1
exercise1_a = 'YesYesYes'
exercise1_b = 'NoNoNoNoNoNoNoNoNo'
exercise1_c = '12 * 3 = {12 * 3}'
exercise1_d = '12 * 3 = 36'

# @exercise_2a
goals = 3
print('I have scored ' + str(goals) + ' goals.')

# @exercise_2b
size = float(input('my size [m]: '))
weight = float(input('my weight [kg]: '))
bmi = weight / (size**2)
print('My BMI is ' + str(bmi) + '.')

# @exercise_2c
text = input('Text to repeat: ')
repeat_n = int(input('How often should "' + text + '" be repeated? '))
print(text * repeat_n)
'''Es darf nur ein int sein, da die multiplikation von einem string mit einem string nicht möglich ist.
Und mit float wäre es auch nicht möglich, da es keine Kommazahlen geben kann.'''


# @exercise_2d
a = int(input('Enter a number: '))
a_times_3 = a * 3
print(str(a) + ' times 3 = ' + str(a_times_3))

# @exercise_3a

something = input("Enter something:")
print(len(something))

# @exercise_3b
something = input("Enter something: ")
print(something + ": " + str(len(something)) + " Letters")