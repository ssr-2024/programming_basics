# @exercise_1
exercise1_a = 'YesYesYes'
exercise1_b = 'NoNoNoNoNoNoNoNoNo'
exercise1_c = '12 * 3 = {12 * 3}'
exercise1_d = '12 * 3 = 36'

# @exercise_2a
goals = 3
print(' I have scored ' + str(goals) + ' goals.')

# @exercise_2b
size = float(input('my size [m]: ')) #convert input to float
weight = float(input('my weight [kg]: ')) #convert input to float
bmi = weight / (size**2)
print('My BMI is ' + str(bmi) + '.') #The variable bmi is a number and it must be converted into a string before it is output in a string.

# @exercise_2c
text = input('Text to repeat: ')
repeat_n = input('How often should "' + text + '" be repeated? ')
print(text * repeat_n)

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
