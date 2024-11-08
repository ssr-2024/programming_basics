# Types of Data

A *data type* is a category for values.Below is an overview of common data types, special cases, type determination, and type conversion (casting) methods. 

## Common Data Types

| Data Type       | Description                                     | Example                   |
|-----------------|-------------------------------------------------|---------------------------|
| Integer (`int`) | Whole numbers, both positive and negative       | `42`, `-7`, `0`           |
| Float (`float`) | Numbers with a decimal point                    | `3.14`, `-0.5`, `2.0`     |
| String (`str`)  | Text, enclosed in single or double quotes       | `'Hello'`, `"Python"`     |
| Boolean (`bool`)| Logical values representing `True` or `False`   | `True`, `False`           |
| List (`list`)   | Ordered, mutable collection of values           | `[1, 2, 3]`, `['a', 'b']` |
| Tuple (`tuple`) | Ordered, immutable collection of values         | `(1, 2, 3)`, `('a', 'b')` |
| Dictionary (`dict`) | Key-value pairs used for data mapping       | `{'key': 'value'}`        |

### Special Case: `None`

`None` is a special data type in Python representing the absence of a value. This is commonly used as a placeholder for variables that will be assigned values later or to indicate "no result" in functions.

| Value  | Description                |
|--------|-----------------------------|
| `None` | Represents the absence of a value, similar to `null` in other languages |

Example:
```python
result = None  # result currently holds no value
```


## Determine the Data Type of a Variable

To determine the data type of a variable in Python, use the `type()` function, which returns the type of the specified variable.

| Syntax               | Description                        |
|----------------------|------------------------------------|
| `type(variable)`     | Returns the data type of `variable` |

Example:
```python
x = 10
print(type(x))  # Output: <class 'int'>
```

## Type Conversion (Casting)

Python provides functions to convert between different data types, known as *casting*. This is useful when data needs to be transformed to match a specific type for a particular operation.

| Function   | Description                                            | Example                               |
|------------|--------------------------------------------------------|---------------------------------------|
| `int(x)`   | Converts `x` to an integer (if possible)               | `int('42')` ➔ `42`                   |
| `float(x)` | Converts `x` to a floating-point number                | `float('3.14')` ➔ `3.14`             |
| `str(x)`   | Converts `x` to a string                               | `str(42)` ➔ `'42'`                   |
| `bool(x)`  | Converts `x` to a boolean (`True` or `False`)          | `bool(1)` ➔ `True`                   |
| `list(x)`  | Converts `x` to a list                                 | `list('abc')` ➔ `['a', 'b', 'c']`    |
| `tuple(x)` | Converts `x` to a tuple                                | `tuple([1, 2, 3])` ➔ `(1, 2, 3)`     |
| `dict()`   | Creates a dictionary (often from key-value pairs)      | `dict(a=1, b=2)` ➔ `{'a': 1, 'b': 2}`|


## Summary of Key Data Types and Functions

| Purpose                         | Function/Method               | Example                                  |
|---------------------------------|-------------------------------|------------------------------------------|
| Check type                      | `type(variable)`              | `type(10) ➔ <class 'int'>`              |
| Convert to integer              | `int(x)`                      | `int('5') ➔ 5`                          |
| Convert to float                | `float(x)`                    | `float('3.5') ➔ 3.5`                    |
| Convert to string               | `str(x)`                      | `str(10) ➔ '10'`                        |
| Convert to boolean              | `bool(x)`                     | `bool(0) ➔ False`                       |
| Length of string/list           | `len(x)`                      | `len('hello') ➔ 5`                      |
| Absence of value                | `None`                        | `result = None`                         |
| Boolean values                  | `True`, `False`               | `is_valid = True`                       |
| Concatenate strings             | `+` operator                  | `'Hello' + ' World' ➔ 'Hello World'`    |
| Repeat string                   | `*` operator                  | `'Hi' * 3 ➔ 'HiHiHi'`                   |


