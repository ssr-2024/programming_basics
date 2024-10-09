# Errors

List of common errors:

- [NameError](#NameError)
- [EOL, while scanning string literal](#SyntaxError)
- [can only concatenate str (not "int") to str](#TypeError)
- [can't multiply sequence by non-int of type 'str'/'float'](#TypeError)


## NameError
`NameError: name 'a' is not defined`
### Cause
Call to a variable or function that is not defined in the current script
### Potential Solutions
- Is the variable/function defined later in the script?
- Missing import of a Python module that defines the variable/function?

### Example
```py
print(variable_not_defined_before)
```


## EOL, while scanning string literal
### Cause
You probably fogot the final single quote character at the end of the string

### Solution
- Check your string quote characters
### Example
```py
 'Hello, world!
```

## can only concatenate str (not "int") to str
### Cause
If you try to use the + operator on a string and an integer value, Python will not know how to handle this.

### Solution
Your code will have to explicitly convert the integer to a string because Python cannot do this automatically

### Example
```py
>>> 'Alice' + 42
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    'Alice' + 42
TypeError: can only concatenate str (not "int") to str

------Solution-----------
'Alice' + str(42)
```

## can't multiply sequence by non-int of type 'str'/'float'
### Cause
The * operator can be used with only two numeric values (for multiplication), or one string value and one integer value (for string replication). Otherwise, Python will just display an error message
It makes sense that Python wouldn’t understand these expressions: you can’t multiply two words, and it’s hard to replicate an arbitrary string a fractional number of times.

### Example
```py
>>> 'Alice' * 'Bob'
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    'Alice' * 'Bob'
TypeError: can't multiply sequence by non-int of type 'str'

>>> 'Alice' * 5.0
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    'Alice' * 5.0
TypeError: can't multiply sequence by non-int of type 'float'
```

## 
### Cause

### Solution

### Example

## 
### Cause

### Solution

### Example

## 
### Cause

### Solution

### Example

## 
### Cause

### Solution

### Example

