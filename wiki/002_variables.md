# Variables
    A variable is like a box in the computer’s memory where you can store a single value. If you want to use the result of an evaluated expression later in your program, you can save it inside a variable.

For example, if you want to variable "spam" to have the value 42 you can do the following:

```py
# initializing variable
spam = 40
#input
spam 
#output
40
```

You can *override* the variable, when it is assigned a new value
```py
# new value
spam = 'HELLO'
#input
spam 
#output
'HELLO?
```
The old value is forgoten

## Legal Variable names
    A good variable name describes the data it contains. Imagine that you moved to a new house and labeled all of your moving boxes as Stuff. You’d never find anything! The variable names spam, eggs, and bacon are used as generic names for the examples in this book and in much of Python’s documentation (inspired by the Monty Python “Spam” sketch), but in your programs, a descriptive name will help make your code more readable.

You can name a varaible anything, as long as it obeys the following three rules:
1. It can be only one word
2. It can use only letters, numbers, and the underscore (_) character
3. It can't begin with a number
### Examples
| Identifier          | Validity                             | Reason for Invalidity (if any)           |
|---------------------|--------------------------------------|------------------------------------------|
| `balance`           | ✅ Valid                             | N/A                                      |
| `current-balance`   | ❌ Invalid                           | Hyphens are not allowed                  |
| `currentBalance`    | ✅ Valid                             | N/A                                      |
| `current balance`   | ❌ Invalid                           | Spaces are not allowed                   |
| `current_balance`   | ✅ Valid                             | N/A                                      |
| `4account`          | ❌ Invalid                           | Can't begin with a number                |
| `_spam`             | ✅ Valid                             | N/A                                      |
| `42`                | ❌ Invalid                           | Can't begin with a number                |
| `SPAM`              | ✅ Valid                             | N/A                                      |
| `total_$um`         | ❌ Invalid                           | Special characters like `$` are not allowed |
| `account4`          | ✅ Valid                             | N/A                                      |
| `'hello'`           | ❌ Invalid                           | Special characters like `'` are not allowed |

Variable names are **case-sensitive**, meaning that spam, SPAM, Spam, and sPaM are four different variables. It is a Python convention to start your variables with a lowercase letter.


