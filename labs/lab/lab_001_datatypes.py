# @exercise_1
exercise1_a = 'YesYesYes'
exercise1_b = 'NoNoNoNoNoNoNoNoNo'
exercise1_c = '12 * 3 = {12 * 3}'
exercise1_d = '12 * 3 = 36'

# @exercise_2a
goals = 3
print(f'I have scored {goals} goals.')

# @exercise_2b
size = float(input('my size [m]: '))
weight = float(input('my weight [kg]: '))
bmi = weight / (size**2)
print(f'My BMI is {bmi}.')

# @exercise_2c
text = input('Text to repeat: ')
repeat_n = int(input('How often should "' + text + '" be repeated? '))
print(text * repeat_n)

# @exercise_2d
a = int(input('Enter a number: '))
a_times_3 = a * 3
print(f'{a} times 3 = {a_times_3}')

# @exercise_3a

something = input("Enter something:")
print(f'{len(something)} Letters')

# @exercise_3b
something = input("Enter something:")
print(f'{something}: {len(something)} Letters')
