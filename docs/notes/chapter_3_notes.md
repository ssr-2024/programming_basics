# Chapter 3 - Functions

- ```def()```: defines a function
    - parameteters between the parantheses are allowed<br> **Attention**:  the value stored in a parameter is forgotten when the function returns
- code in the block is executed when the function is called (not when it is defined)
- purpose: group code that gets executed multiple times

**Return Values and Return Statements**

- with a *return statement* you can specify what the return value should be

**The None Value**
- represents the absence of a value
- *None* is the only value of the *NoneType* data type
- can be helpful when you need to store something that won’t be confused for a real value in a variable

**Keyword Arguments**
- are identified by the keyword put before them in the function call
- ```end``` keyword: Output is printed on a single line
```python
print('Hello', end='') 
print('World')

Output= HelloWorld
````
- ```sep```keyword: replaces the default seperating string
```python
print('cats', 'dogs', 'mice', sep=',') 

Output= cats,dogs,mice
````

## Local and Global Scope

- *local scope*: Parameters and variables that are assigned in a called function
    - *local variable*: variable that exists in a local scope
    - is created whenever a function is called; when the function returns, the local scope is destroyed, and these variables are forgotten. The next time you call this function, the local variables will **not remember** the values stored in them from the last time the function was called.

- *global scope*: Variables that are assigned outside all functions
    - *global variables*: variable that exists in a global scope
    - variables would remember their values from the last time

**Why scopes matter**:
- Code in the global scope cannot use any local variables.
- However, a local scope can access global variables.
- Code in a function’s local scope cannot use variables in any other local scope.
- You can use the same name for different variables if they are in different scopes.

**Important rules**

- local variables can't be used in the global scope
- local scopes can't use variables in other local scopes (local variables in one function are completely seperate from the local variables in another function)
- global variables can be read from a local scope
- local and global variables can have the same name, but you should avoid it

**The Global Statement**

If you need to modify a global variable from within a function, use the global statement

```python
def spam(): 
    global eggs     #eggs is declared global
    eggs = 'spam'

eggs = 'global'
spam()   
print(eggs)

Output = spam
```
There are four rules to tell whether a variable is in a local scope or global scope:
1.  If a variable is being used in the global scope (that is, outside of all functions), then it is always a global variable. 
2.  If there is a global statement for that variable in a function, it is a global variable. 
3.  Otherwise, if the variable is used in an assignment statement in the function, it is a local variable. 
4.  But if the variable is not used in an assignment statement, it is a global variable.

## Exception Handling

- till now: error, or *exception* meant, that the whole program crashed
- Errors can be handled with ```try``` and ```except``` statements
- The code that could potentially have an error is put in a try clause.

```python
def spam(divideBy):     
    try:         
        return 42 / divideBy     
    except ZeroDivisionError:         
        print('Error: Invalid argument.')
print(spam(2)) 
print(spam(12)) 
print(spam(0))
print(spam(1))
````
- When code in a try clause causes an error, the program execution immediately moves to the code in the except clause. After running that code, the execution continues as normal.

## Questions
1. Why are functions advantageous to have in your programs?

Reusability: you can write a block of code once and reuse it multiple times.

2. When does the code in a function execute: when the function is defined or
when the function is called?

The code in a function executes **when the function is called**.

3. What statement creates a function?

```def()```statement

4. What is the difference between a function and a function call?

- A **function** is the block of code that is defined and ready to be used. 
- A **function call** is the execution of the function by its name.

5. How many global scopes are there in a Python program? How many local
scopes?

- There is one global scope per program, which is created when the program starts.
- Local scopes are created whenever a function is called. Each function call gets its own local scope.


6. What happens to variables in a local scope when the function call returns?

The local variables will not remember the values stored in them from the last time the function was called.

7. What is a return value? Can a return value be part of an expression?

A **return value** is the result that a function sends back to the caller using the ```return``` statement. Yes, a return value can be part of an expression.

8. If a function does not have a return statement, what is the return value of a
call to that function?

If a function does not have a ```return``` statement, it implicitly returns ```None```.

9. How can you force a variable in a function to refer to the global variable?

You can use the ```global``` keyword to refer to a global variable inside a function. For example:

```python 
x = 10

def my_function():
    global x
    x = 20  # modifies the global variable x
````


10. What is the data type of None?

NoneType

11. What does the ```import areallyourpetsnamederic``` statement do?

This statement tries to import a module named ```areallyourpetsnamederic```. If such a module exists, it will be imported.

12. If you had a function named bacon() in a module named spam, how would you call it after importing spam?

```python
import spam
spam.bacon()
```

13. How can you prevent a program from crashing when it gets an error?

You can use a ```try```  and ``except`` block to catch and handle errors, preventing the program from crashing.

14. What goes in the try clause? What goes in the except clause?

The try clause contains that could potentially have an error.<br>

The except clause contains the code that runs if an exception occurs in the try block.






