
**List of common errors:**

- [NameError](#nameerror)
  - [Cause](#cause)
  - [Potential Solutions](#potential-solutions)
  - [Example](#example)
- [EOL, while scanning string literal](#eol-while-scanning-string-literal)
  - [Cause](#cause-1)
  - [Solution](#solution)
  - [Example](#example-1)
- [can only concatenate str (not "int") to str](#can-only-concatenate-str-not-int-to-str)
  - [Cause](#cause-2)
  - [Solution](#solution-1)
  - [Example](#example-2)
- [can't multiply sequence by non-int of type 'str'/'float'](#cant-multiply-sequence-by-non-int-of-type-strfloat)
  - [Cause](#cause-3)
  - [Example](#example-3)
- [Can't convert 'int' object to str implicitly](#cant-convert-int-object-to-str-implicitly)
  - [Cause](#cause-4)
  - [Solution](#solution-2)
  - [Example](#example-4)
- [Infinity Loop](#infinity-loop)
  - [Cause](#cause-5)
  - [Solution](#solution-3)
- [list index out of range](#list-index-out-of-range)
  - [Cause](#cause-6)
  - [Solution](#solution-4)
  - [Example](#example-5)
- [list indices must be integers, not float](#list-indices-must-be-integers-not-float)
  - [Cause](#cause-7)
  - [Solution](#solution-5)
  - [Example](#example-6)
- [unorderable types: str() \< int()](#unorderable-types-str--int)
  - [Cause](#cause-8)
  - [Solution](#solution-6)
  - [Example](#example-7)
- [](#)
  - [Cause](#cause-9)
  - [Solution](#solution-7)
  - [Example](#example-8)
- [](#-1)
  - [Cause](#cause-10)
  - [Solution](#solution-8)
  - [Example](#example-9)
- [](#-2)
  - [Cause](#cause-11)
  - [Solution](#solution-9)
  - [Example](#example-10)


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

## Can't convert 'int' object to str implicitly
### Cause
Python gives an error because you can use the + operator only to add two integers together or concatenate two strings. You can’t add an integer to a string because this is ungrammatical in Python
### Solution
You can fix this by using a string version of the integer instead
### Example
```py
>>> print('I am ' + 29 + ' years old.')
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    print('I am ' + 29 + ' years old.')
TypeError: Can't convert 'int' object to str implicitly

# solution
>>> print('I am ' + str(29) + ' years old.')
I am 29 years old.
```

## Infinity Loop
### Cause
Bug in a program causing to get stuck in a Infinity Loop
### Solution
Press CTRL-C. This will send a *KeyboardInterrrupt* error to your program and cause it to stop immediately.


## list index out of range
### Cause
Python will give you an IndexError error message if you use an index that exceeds the number of values in your list value.
### Solution
Check your lists
### Example
```py
spam = ['cat', 'bat', 'rat', 'elephant']
spam[10000]
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    spam[10000]
IndexError: list index out of range
```

## list indices must be integers, not float
### Cause
You typed a float into the index of a list
### Solution
Recheck that all indexes are integer. If for any reason you still want to work with float values, you have to work with int()-functions.
For more details consulte [INT() Functions](101_functions.md#functions-str-int-float)

### Example
```py
spam = ['cat', 'bat', 'rat', 'elephant']
spam[1]
'bat'
spam[1.0]
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    spam[1.0]
TypeError: list indices must be integers, not float
spam[int(1.0)]
'bat'
```

## unorderable types: str() < int()
### Cause
You cannot sort lists that have both number values and string values in them, since Python doesn’t know how to compare these values. 
### Solution
If you want to sort the list but need to account for the presence of both strings and integers, you could consider this option:
You can provide a custom sort key that converts all elements to a common type, such as strings, for comparison:
```py
spam = [1, 3, 2, 4, 'Alice', 'Bob']
spam.sort(key=str)
print(spam)
# output
[1, 2, 3, 4, 'Alice', 'Bob']
```

This will treat all elements as strings during the sort:
However, note that in this approach, numbers are sorted based on their string representation.
### Example
```py
spam = [1, 3, 2, 4, 'Alice', 'Bob']
spam.sort()
Traceback (most recent call last):
 File "<pyshell#70>", line 1, in <module>
   spam.sort()
TypeError: unorderable types: str() < int()
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