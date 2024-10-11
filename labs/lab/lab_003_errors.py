# @exercise_1a 'TypeError: can only concatenate str (not "float") to str'

#Der Fehlercode entsteht, wenn man versucht einen String mit einem Float zu addieren, beispielsweise so:

text= 'Ich habe die Schuhgrösse '
schuh_groesse= 42.5
print (text + schuh_groesse)

# @exercise_1b "TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'int'"

text= 'Haus'
multiplikator= 4
print (text ** multiplikator)

# @exercise_1c 'ZeroDivisionError: division by zero'

test = 17
error = 17/0

