# Functions

Functions in Python allow for modular programming, enabling you to group reusable code blocks that perform specific tasks. This promotes code efficiency and readability, making it easier to debug and maintain complex programs.

## Principle of Modularity
Modularity is the practice of dividing a program into smaller, manageable parts (functions). Each function is responsible for a single task and can be reused multiple times, reducing redundancy.

## Calling Functions

To use a function, you must call it by its name followed by parentheses, which may include arguments if required by the function.

```python
def greet():
    print("Hello, world!")

greet()  # Calls the function and prints "Hello, world!"
```

## Calling Functions from Libraries

Python allows you to use functions from external libraries. For example, to use the `art` library for ASCII art, first install it via:

```python
pip3 install art
```

Examples of using `art` for ASCII text with the name "Eliane":

```python
from art import text2art
Art = text2art("Eliane")
print(Art)
```
This function returns ASCII text as a `str` in normal mode.

## Defining Functions
To define a function in Python, use the `def` keyword, followed by the function name, parentheses, and a colon. Inside the parentheses, you can add parameters for passing data to the function.

```python
def add(a, b):
    return a + b
```

### `return` Statement
The `return` statement allows a function to send a result back to the caller. It can be used in expressions and other operations.

### Example
```python
def square(num):
    return num ** 2

result = square(5)  # result will be 25
print(result)
```

## Variables in Functions

### Local and Global Variables
Variables declared inside functions are **local** and only accessible within the function. Variables declared outside any function are **global** and can be accessed anywhere in the program.

### Example of Local Scope
```python
def example():
    x = 10  # local variable
    print(x)

example()  # Prints 10
print(x)  # Error: x is not defined outside the function
```

### Global Variables
Global variables can be accessed in any part of the program. If you want to modify a global variable within a function, use the `global` keyword.

```python
x = 5  # global variable

def modify_global():
    global x
    x = 10

modify_global()
print(x)  # Prints 10
```

## Exception Handling

Errors, or *exceptions*, in Python can be handled using `try` and `except` statements. This allows the program to continue running even if an error occurs within a function.

```python
def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")

print(divide(10, 2))  # Prints 5.0
print(divide(10, 0))  # Prints "Error: Cannot divide by zero."
```
When an error occurs in the `try` block, execution jumps to the `except` block.



