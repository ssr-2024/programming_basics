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

# Anstelle von repeat_n kann man auch eine for-Schleife verwenden.
# Dabei nimmt die Schleife den Input für die Wiederholungen als Argument.
# Es könnte so aussehen:
# for n in range(int(input('How often should "' + text + '" be repeated? '))):
#     print(text)


# @exercise_2d
a = input('Enter a number: ')
a_times_3 = a * 3
print(a + ' times 3 = ' + a_times_3)

# @exercise_3a

something = input("Enter something:")
print(len(something) + ' Letters')

# @exercise_3b
something = input("Enter something:")
print(something + ": " + len(something) + ' Letters')
