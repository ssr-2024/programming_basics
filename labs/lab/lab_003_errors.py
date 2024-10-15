# @exercise_1a 'TypeError: can only concatenate str (not "float") to str'

# Um diese Fehlermeldung zu bekommen, muss ich versuchen einen Float mit einem String zu verketten
value = 7.77
print("The value is: " + value)

# @exercise_1b "TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'int'"

# Um diese Fehlermeldung zu bekommen muss eine Zeichenkette (str) mit einem Exponenten (**) oder der Funktion pow() zu potenziert werden
value = "5"
result = value ** 2

# @exercise_1c 'ZeroDivisionError: division by zero'

# Um diese Fehlermeldung zu bekommen muss versucht werden, durch 0 zu teilen
numerator = 10
denominator = 0
result = numerator / denominator

# @exercise_2
# die Fehlermeldung "[ ] SyntaxError: can't assign to operator" erscheint, da keine Zuweisung an "'some ' + 'text'" erfolgen kann, da dies kein Variablenname ist