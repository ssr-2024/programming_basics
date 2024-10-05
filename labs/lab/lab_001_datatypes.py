# @exercise_1
exercise1_a = 'YesYesYes'
exercise1_b = 'NoNoNoNoNoNoNoNoNo'
exercise1_c = '12 * 3 = {12 * 3}'
exercise1_d = '12 * 3 = 36'

# @exercise_2a
goals = 3
print('I have scored ' + f'{goals}' + ' goals.')

# @exercise_2b
size = input('my size [m]: ')
weight = input('my weight [kg]: ')
bmi = float(weight) / (float(size)**2)
print('My BMI is ' + str(bmi) + '.')

# @exercise_2c
text = input('Text to repeat: ')
repeat_n = input('How often should "' + str(text) + '" be repeated? ')
print(f'{text * int(repeat_n)}')

# @exercise_2d
a = input('Enter a number: ')
a_times_3 = float(a) * 3
print(str(a) + ' times 3 = ' + str(a_times_3))

# @exercise_3a

something = input("Enter something:")
print(len(something) + ' Letters')

# @exercise_3b
something = input("Enter something:")
print(something + ": " + len(something) + ' Letters')
