# @exercise_1
exercise1_a = 'YesYesYes'
exercise1_b = 'NoNoNoNoNoNoNoNoNo'
exercise1_c = '12 * 3 = {12 * 3}'
exercise1_d = '12 * 3 = 36' # f macht das in dem string die geschweiften klammern '{}' ausgeführt ausgeführt wird.

# @exercise_2a
goals = 3
print('I have scored ' + str(goals) + ' goals.') # variable 'goals' wird durch den befehl str() in einen string umwandeln

# @exercise_2b
size = float(input('my size [m]: ')) # weil der input eine zahl sein wird, benutzen wir float(vornedrann)
weight = float(input('my weight [kg]: '))
bmi = weight / (size**2)
print('My BMI is ' + str(bmi) + '.')    #bmi geben wir als string heraus

# @exercise_2c
text = input('Text to repeat: ')
repeat_n = int(input('How often should "' + text + '" be repeated? ')) # repeat_n in einen integer umwandeln
print(text * repeat_n)


# @exercise_2d
a = input('Enter a number: ')  # Eingabe als String
a = int(a)  # Umwandlung in einen Integer
a_times_3 = a * 3 
print(str(a) + ' times 3 = ' + str(a_times_3)) 

# @exercise_3a

something = input("Enter something:")
print(str(len(something))) # die variable something ist ursrpünglich ein integer und muss mit str in einen string umgewandelt werden


# @exercise_3b
something = input("Enter something:") #something is eine zeichenkette (string)
print(something + ": " + str(len(something)) + ' Letters') #hier wird versucht die zeichenkette something mit einem integer-wert (len(something)) zu verknüpfen. aus dem len(something) wird deshalb ein string gemacht.
