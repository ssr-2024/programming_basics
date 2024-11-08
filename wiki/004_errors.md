# Error Messages

Common Error Messages:

- [NameError](#NameError)
- [TypeError: can only concatenate str (not "float") to str](#TypeError-can-only-concatenate-str-not-float-to-str)
- [TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'int'](#TypeError-unsupported-operand-types-for--or-pow-str-and-int)
- [ZeroDivisionError: division by zero](#ZeroDivisionError-division-by-zero)

## NameError
`NameError: name 'a' is not defined`

### Cause
Occurs when a variable or function is called but has not been defined in the current script.

### Possible Causes
- The variable or function is defined later in the script but is called before its definition.
- Missing import of a Python module that defines the variable or function.

### Example
```python
print(variable_not_defined_before)
```

---

## TypeError: can only concatenate str (not "float") to str
`TypeError: can only concatenate str (not "float") to str`

### Cause
This error occurs when trying to concatenate a string with a non-string data type (such as a float) without converting it to a string.

### Possible Causes
- Attempting to use the `+` operator to concatenate a string and a float without converting the float to a string.

### Example
```python
print("My height is " + 1.75)  # Error: 1.75 is a float, not a string
```

### Solution
Convert the float to a string using `str()` before concatenating:
```python
print("My height is " + str(1.75))
```

---

## TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'int'
`TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'int'`

### Cause
Occurs when attempting to use the `**` operator or `pow()` function with incompatible data types, such as a string and an integer.

### Possible Causes
- Attempting to perform exponentiation on a string value rather than converting it to an integer or float.

### Example
```python
print("100" ** 2)  # Error: "100" is a string, not a number
```

### Solution
Convert the string to an integer or float before performing the exponentiation:
```python
print(int("100") ** 2)
```

---

## ZeroDivisionError: division by zero
`ZeroDivisionError: division by zero`

### Cause
This error occurs when attempting to divide a number by zero, which is mathematically undefined.

### Possible Causes
- A variable or expression used as the divisor evaluates to zero, resulting in a division-by-zero operation.

### Example
```python
print(100 / 0)  # Error: Division by zero
```

### Solution
Ensure that the divisor is not zero before performing the division. Use conditional checks if necessary:
```python
divisor = 0
if divisor != 0:
    print(100 / divisor)
else:
    print("Cannot divide by zero.")
```