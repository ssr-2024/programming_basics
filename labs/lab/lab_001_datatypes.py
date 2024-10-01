# @exercise_1
exercise1_a = ''
exercise1_b = ''
exercise1_c = ''
exercise1_d = ''

# @exercise_2a
goals = 3
print('I have scored ' + goals + ' goals.')

# @exercise_2b
size = input('my size [m]: ')
weight = input('my weight [kg]: ')
bmi = weight / (size**2)
print('My BMI is ' + bmi + '.')

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
