**Table of Content**
- [Operators](#operators)
  - [Arithmetic Operators Overive](#arithmetic-operators-overive)
    - [`+` Operator with data type string](#-operator-with-data-type-string)
    - [`*`Operator with data type string](#operator-with-data-type-string)
  - [Comparison Operators](#comparison-operators)
  - [Boolean Operators](#boolean-operators)
    - [Binary Boolean Operators](#binary-boolean-operators)
  - [Mixing Boolean and comparison Operators](#mixing-boolean-and-comparison-operators)
  - [Membership operators](#membership-operators)
  - [Augmented assignment statement](#augmented-assignment-statement)
  - [Logische Operatoren](#logische-operatoren)
  - [Membership operators](#membership-operators-1)
  - [Identitätsoperator](#identitätsoperator)

# Operators

## Arithmetic Operators Overive
| Operator | Operation                   | Example  | Evaluates to... |
|----------|-----------------------------|----------|-----------------|
| `**`     | Exponent                    | `2 ** 3` | 8               |
| `%`      | Modulus/remainder           | `22 % 8` | 6               |
| `//`     | Integer division/floored quotient | `22 // 8` | 2               |
| `/`      | Division                    | `22 / 8` | 2.75            |
| `*`      | Multiplication              | `3 * 5`  | 15              |
| `-`      | Subtraction                 | `5 - 2`  | 3               |
| `+`      | Addition                    | `2 + 2`  | 4               |

### `+` Operator with data type string
The addition operator works this way either with two integers or floating-point values.
However, when `+` is used on two string values, it joins the strings as the *string concatenation*  operator. Example:
```py
>>> 'Alice' + 'Bob'
'AliceBob'
```
### `*`Operator with data type string
When the * operator is used on one string value and one integer value, it becomes the string replication operator. Example:
```py
>>> 'Alice' * 5
'AliceAliceAliceAliceAlice'
```


## Comparison Operators
| Operator | Meaning | Example       |
|:---------|:-------------|:------------------|
| `<`      |      Less than        |                   |
| `<=`     |        Less than or equal      |                   |
| `>`      |     Greater than         |                   |
| `>=`     |        Greater than or equal      |                   |
| `==`     |        Equal to      |                   |
| `!=`     |    Not equal to          |                   |

These operators evaluate to True or False depending on the values you give them. Let’s try some operators now, starting with == and !=.
```py
>>> 42 == 42
        True
        >>> 42 == 99
        False
        >>> 2 != 3
        True
        >>> 2 != 2
        False
```
Note that an integer or floating-point value will always be unequal to a string value. The expression 42 == '42' evaluates to False because Python considers the integer 42 to be different from the string '42'.

The <, >, <=, and >= operators, on the other hand, work properly only with integer and floating-point values.
```py
   >>> 42 < 100
           True
           >>> 42 > 100
           False
           >>> 42 < 42
           False
           >>> eggCount = 42
        ❶ >>> eggCount <= 42
           True
           >>> myAge = 29
        ❷ >>> myAge >= 10
           True
```
## Boolean Operators
The three Boolean operators (`and`,`or`, and `not`) are used to compare Boolean values. Like comparison operators, they evaluate these expressions down to a Boolean value. Let’s explore these operators in detail, starting with the and operator.

### Binary Boolean Operators
The `and` operator evaluates an expression to True if both Boolean values are True; otherwise, it evaluates to False. Enter some expressions using and into the interactive shell to see it in action.
```py
>>> True and True
          True
          >>> True and False
          False
```
| Expression       | Evaluates to |
|------------------|--------------|
| `True and True`   | True         |
| `True and False`  | False        |
| `False and True`  | False        |
| `False and False` | False        |

On the other hand, the `or` operator evaluates an expression to True if either of the two Boolean values is True. If both are False, it evaluates to False.

```py
>>> False or True
          True
          >>> False or False
          False
```
| Expression        | Evaluates to |
|-------------------|--------------|
| `True or True`    | True         |
| `True or False`   | True         |
| `False or True`   | True         |
| `False or False`  | False        |

Unlike and and or, the `not` operator operates on only one Boolean value (or expression). The not operator simply evaluates to the opposite Boolean value.

```py
   >>> not True
          False
          ❶ >>> not not not not True
          True
```
| Expression   | Evaluates to |
|--------------|--------------|
| `not True`   | False        |
| `not False`  | True         |

## Mixing Boolean and comparison Operators
Recall that the and, or, and not operators are called Boolean operators because they always operate on the Boolean values True and False. While expressions like 4 < 5 aren’t Boolean values, they are expressions that evaluate down to Boolean values. Try entering some Boolean expressions that use comparison operators into the interactive shell.
```py
>>> (4 < 5) and (5 < 6)
        True
        >>> (4 < 5) and (9 < 6)
        False
        >>> (1 == 2) or (2 == 2)
        True
```
Python evaluates this code as followed:
```
(4 < 5) and (5 < 6)
   ↓
True and (5 < 6)
   ↓
True and True
   ↓
True
```
## Membership operators
You can determine whether a value is or isn’t in a list with the in and not in operators. Like other operators, in and not in are used in expressions and connect two values: a value to look for in a list and the list where it may be found. These expressions will evaluate to a Boolean value. Enter the following into the interactive shell:
| Operator | 
|:---------|
| `in`     | 
| `not in` |   
**Example**:
```py
'howdy' in ['hello', 'hi', 'howdy', 'heyas']
True

spam = ['hello', 'hi', 'howdy', 'heyas']
'cat' in spam
False
'howdy' not in spam
False
'cat' not in spam
True
```
## Augmented assignment statement 
| Augmented Assignment Statement | Equivalent Assignment Statement |
|--------------------------------|---------------------------------|
| `spam += 1`                    | `spam = spam + 1`               |
| `spam -= 1`                    | `spam = spam - 1`               |
| `spam *= 1`                    | `spam = spam * 1`               |
| `spam /= 1`                    | `spam = spam / 1`               |
| `spam %= 1`                    | `spam = spam % 1`               |




## Logische Operatoren
| Operator | Beschreibung | Beispiel          |
|:---------|:-------------|:------------------|
| `and`    |              |                   |
| `or`     |              |                   |
| `not`    |              |                   |

## Membership operators
| Operator | Beschreibung | Beispiel          |
|:---------|:-------------|:------------------|
| `in`     |              |                   |
| `not in` |              |                   |

## Identitätsoperator
| Operator | Beschreibung | Beispiel          |
|:---------|:-------------|:------------------|
| `is`     |              |                   |
| `is not` |              |                   |
