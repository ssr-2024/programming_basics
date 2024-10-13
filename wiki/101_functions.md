**Table of content**
- [Functions](#functions)
  - [DEF Statements with Parameters](#def-statements-with-parameters)
  - [Return Values and Return Statements](#return-values-and-return-statements)
  - [`None` Value](#none-value)
- [Local and Global Scope](#local-and-global-scope)
  - [Global Variables](#global-variables)
  - [Local Variables](#local-variables)
    - [Multiple Local Scopes](#multiple-local-scopes)
  - [`global`Keyword](#globalkeyword)
  - [Why Scopes Matter](#why-scopes-matter)
  - [Local and Global Varaibles with the same name](#local-and-global-varaibles-with-the-same-name)
  - [Rules for Global and Local Variables](#rules-for-global-and-local-variables)
    - [Example](#example)
- [Exception Handling](#exception-handling)
- [Standard Functions](#standard-functions)
  - [Function `Print()`](#function-print)
  - [Function `Input()`](#function-input)
  - [Functions `STR(), INT(), FLOAT()`](#functions-str-int-float)
    - [Example on how to use it](#example-on-how-to-use-it)
- [Moduls](#moduls)
    - [Import](#import)
  - [Modul `Art (in) Python`](#modul-art-in-python)
    - [Installation](#installation)
        - [Use](#use)

# Functions
    Functions are reusable blocks of code that perform a specific task. They allow you to break your program into smaller, manageable parts. A function can take input, process it, and return an output.
## DEF Statements with Parameters
When you call the print() or len() function, you pass in values, called arguments in this context, by typing them between the parentheses. You can also define your own functions that accept arguments.
```py
 def hello(name):
     print('Hello ' + name)

 hello('Alice')
  hello('Bob')
```
```py
# output
Hello Alice
Hello Bob

  ```
The definition of the hello() function in this program has a parameter called name. A parameter is a variable that an argument is stored in when a function is called. The first time the hello() function is called, it’s with the argument 'Alice'. The program execution enters the function, and the variable name is automatically set to 'Alice', which is what gets printed by the print() statement.

One special thing to note about parameters is that the value stored in a parameter is forgotten when the function returns. For example, if you added print(name) after hello('Bob') in the previous program, the program would give you a NameError because there is no variable named name. This variable was destroyed after the function call hello('Bob') had returned, so print(name) would refer to a name variable that does not exist.

## Return Values and Return Statements
When you call the len() function and pass it an argument such as 'Hello', the function call evaluates to the integer value 5, which is the length of the string you passed it. In general, the value that a function call evaluates to is called the return value of the function.

When creating a function using the def statement, you can specify what the return value should be with a return statement. A return statement consists of the following:
- The return keyword
- The value or expression that the function should return

When an expression is used with a return statement, the return value is what this expression evaluates to. For example, the following program defines a function that returns a different string depending on what number it is passed as an argument. 

**Magic 8-Ball** 
```py
import random
def getAnswer(answerNumber):
    if answerNumber == 1:
           return 'It is certain'
       elif answerNumber == 2:
           return 'It is decidedly so'
       elif answerNumber == 3:
           return 'Yes'
       elif answerNumber == 4:
           return 'Reply hazy try again'
       elif answerNumber == 5:
           return 'Ask again later'
       elif answerNumber == 6:
           return 'Concentrate and ask again'
       elif answerNumber == 7:
           return 'My reply is no'
       elif answerNumber == 8:
           return 'Outlook not so good'
       elif answerNumber == 9:
           return 'Very doubtful'

r = random.randint(1, 9)
fortune = getAnswer(r)
print(fortune)
```
## `None` Value
`None` is a special constant in Python representing the absence of a value. It is often used to signify "nothing" or "no result" and is the only value of the `NoneType` data type.
- *Default return value*: If a function doesn’t explicitly return a value, it returns None by default.
- *Placeholder*: It can be used as a placeholder for variables that are yet to be assigned meaningful values.
- *Comparison*: Use the `is` operator to check if a variable is `None` (e.g., `if var is None:`).

`None` helps manage cases where a function or operation should return "nothing," making it useful in function return types and variable initialization.
```py
def example_function():
    print("This function doesn't return anything.")

result = example_function()  # Calls the function but doesn't return a value
print(result)  # Output: None

# Using None as a placeholder
value = None  # Initial value is None

if value is None:
    print("The variable 'value' has no value yet!")  # This will be printed
```
# Local and Global Scope
Scope refers to the area in a program where a variable is accessible. Python has two main types of scope:
- Global scope: Variables defined outside any function. These variables are accessible throughout the entire program.
- Local scope: Variables defined inside a function. These variables are only accessible within that function.
## Global Variables
Variables declared outside of any function are in the global scope. They can be accessed from anywhere in the program, including inside functions:
```py
eggs = 42  # Global variable
def spam():
    print(eggs)  # Accesses global variable
spam()  # Output: 42
```
## Local Variables
Variables declared inside a function exist in the local scope of that function. They can only be used within that function and are destroyed once the function finishes:
```py
def spam():
    eggs = 99  # Local variable
    print(eggs)
spam()  # Output: 99
print(eggs)  # Error: 'eggs' is not defined (outside of function)
```
### Multiple Local Scopes
Each function call has its own local scope. Variables with the same name in different functions are treated separately:
```py
eggs = 'global'
def spam():
    eggs = 'local'
    print(eggs)  # Output: local
spam()
print(eggs)  # Output: global (global variable unchanged)
```
## `global`Keyword
If you want to modify a global variable inside a function, you must use the global keyword:
```Py
eggs = 42
def spam():
    global eggs
    eggs = 'modified'
spam()
print(eggs)  # Output: modified
```
## Why Scopes Matter
- Local variables limit the effect of changes to just one function, reducing bugs.
- Global variables should be used sparingly in larger programs, as they can lead to hard-to-find bugs when multiple parts of the program modify them.
## Local and Global Varaibles with the same name
To simplify your life, avoid using local variables that have the same name as a global variable or another local variable. But technically, it’s perfectly legal to do so in Python. To see what happens, type the following code into the file editor and save it as sameName.py:

    def spam():
❶     eggs = 'spam local'
       print(eggs) # prints 'spam local'
   def bacon():

❷     eggs = 'bacon local'
       print(eggs) # prints 'bacon local'
       spam()
       print(eggs) # prints 'bacon local'

❸ eggs = 'global'
   bacon()
   print(eggs) # prints 'global'
When you run this program, it outputs the following:

 bacon local
spam local
bacon local
global
There are actually three different variables in this program, but confusingly they are all named eggs. The variables are as follows:

❶ A variable named eggs that exists in a local scope when spam() is called.

❷ A variable named eggs that exists in a local scope when bacon() is called.

❸ A variable named eggs that exists in the global scope.

Since these three separate variables all have the same name, it can be confusing to keep track of which one is being used at any given time. This is why you should avoid using the same variable name in different scopes.


## Rules for Global and Local Variables
1. **Global Scope:** A variable used outside of any function is global.
2. **Global Statement:** If a variable is declared global inside a function using the global statement, it's treated as a global variable.
3. **Assignment Inside a Function:**
If a variable is assigned a value inside a function without using global, it's a local variable.
4. **No Assignment in Function:**
If a variable is used but not assigned in a function, it's global (assuming it exists in the global scope).

### Example
```py
def spam():
    global eggs  # Refers to the global 'eggs'
    eggs = 'spam'  # Modifies the global variable

def bacon():
    eggs = 'bacon'  # Local variable inside bacon()

def ham():
    print(eggs)  # Refers to the global 'eggs'

eggs = 42  # Global variable
spam()
print(eggs)  # Output: 'spam'
```
# Exception Handling
Right now, getting an error, or exception, in your Python program means the entire program will crash. You don’t want this to happen in real-world programs. Instead, you want the program to detect errors, handle them, and then continue to run.

For example, consider the following program, which has a “divide-by-zero” error:
```Py
def spam(divideBy):
    return 42 / divideBy

print(spam(2))
print(spam(12))
print(spam(0))
print(spam(1))
```
```py
#output
21.0
3.5
Traceback (most recent call last):
  File "C:/zeroDivide.py", line 6, in <module>
    print(spam(0))
  File "C:/zeroDivide.py", line 2, in spam
    return 42 / divideBy
ZeroDivisionError: division by zero
```
Errors can be handled with `try` and except statements. The code that could potentially have an error is put in a `try` clause. The program execution moves to the start of a following `except` clause if an error happens.
```py
def spam(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        print('Error: Invalid argument.')

print(spam(2))
print(spam(12))
print(spam(0))
print(spam(1))
```
```py
#output
21.0
3.5
Error: Invalid argument.
None
42.0
```
**Alternative**
```py
def spam(divideBy):
    return 42 / divideBy

try:
    print(spam(2))
    print(spam(12))
    print(spam(0))
    print(spam(1))
except ZeroDivisionError:
    print('Error: Invalid argument.')
```
```py
#output
21.0
3.5
Error: Invalid argument.
```
The reason print(spam(1)) is never executed is because once the execution jumps to the code in the except clause, it does not return to the try clause. Instead, it just continues moving down as normal.








# Standard Functions
## Function `Print()`
The print() function displays the string value inside the parentheses on the screen.
```py
 print('Hello world!')
 print('What is your name?') # ask for their name
   ```


The line print('Hello world!') means “Print out the text in the string 'Hello world!'.” When Python executes this line, you say that Python is calling the print() function and the string value is being passed to the function. A value that is passed to a function call is an argument. Notice that the quotes are not printed to the screen. They just mark where the string begins and ends; they are not part of the string value.

## Function `Input()`
The input() function waits for the user to type some text on the keyboard and press ENTER.
```py
 myName = input()
 ```
This function call evaluates to a string equal to the user’s text, and the previous line of code assigns the myName variable to this string value.

You can think of the input() function call as an expression that evaluates to whatever string the user typed in. If the user entered 'Al', then the expression would evaluate to myName = 'Al'.

## Functions `STR(), INT(), FLOAT()`
The str(), int(), and float() functions will evaluate to the string, integer, and floating-point forms of the value you pass, respectively. Try converting some values in the interactive shell with these functions, and watch what happens.
```py
>>> str(0)
'0'
>>> str(-3.14)
'-3.14'
>>> int('42')
42
>>> int('-99')
-99
>>> int(1.25)
1
>>> int(1.99)
1
>>> float('3.14')
3.14
>>> float(10)
10.0
```
### Example on how to use it
```py
print('What is your age?') # ask for their age
   myAge = input()
   print('You will be ' + str(int(myAge) + 1) + ' in a year.')
```

# Moduls
All Python programs can call a basic set of functions called built-in functions, including the print(), input(), and len() functions you’ve seen before. Python also comes with a set of modules called the standard library. Each module is a Python program that contains a related group of functions that can be embedded in your programs.

### Import
Before you can use the functions in a module, you must import the module with an import statement. In code, an import statement consists of the following:
- The import keyword
- The name of the module
- Optionally, more module names, as long as they are separated by commas

An alternative form of the import statement is composed of the from keyword, followed by the module name, the import keyword, and a star; for example, from random import *.

With this form of import statement, calls to functions in random will not need the random. prefix. However, using the full name makes for more readable code, so it is better to use the normal form of the import statement.

Let's take the following modul as an example:
## Modul `Art (in) Python`
"Art Python" is a package that allows you to create art in the terminal. The following documentation explains the installation process and provides some examples.

### Installation
1. Search for "art Python" in a browser.
2. On the website https://pypi.org/project/art/, copy the "pip install art" link.
3. For Mac, use: pip3 install art.
4. To switch the terminal into a Python environment, type: python3.
5. Then, type from art import * to import all commands from the package.


##### Use
After installing the package, you can use the functions it provides. An example would be:

```python
>>> tprint ("test")
 _               _   
| |_   ___  ___ | |_ 
| __| / _ \/ __|| __|
| |_ |  __/\__ \| |_ 
 \__| \___||___/ \__|
                     

>>> aprint("butterlfy")
Ƹ̵̡Ӝ̵̨̄Ʒ
```