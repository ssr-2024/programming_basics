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
repeat_n = int(input('How often should "' + text + '" be repeated? ')) #convert repeat_n to int()
print(text * repeat_n)

#Only the data type integer (int) can be used for the variable repeat_n. 
#The * operator can be used with only two numeric values (for multiplication) or one string value and one integer value (for string replication).
#Multiplying a string by a float leads to an error because it is not clear how many times a string should be repeated if the number is not an integer.
#Multiplying a string with another string is not possible, as the concept of ‘replication’ for strings is only defined with integers.

# @exercise_2d
a = int(input('Enter a number: ')) #convert a to an integer
a_times_3 = a * 3
print(str(a) + ' times 3 = ' + str(a_times_3)) #convert a and a_times_3 to a string

# @exercise_3a

something = input("Enter something:")
print(len(something) + ' Letters')

# @exercise_3b
something = input("Enter something:")
print(something + ": " + len(something) + ' Letters')
