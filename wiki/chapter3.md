# chapter 3
## return
```python
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
```
das kennenlernen der Funktion "return". ähnlich zu print Fkt.

## the none value
The None keyword is used to define a null value, or no value at all. None is not the same as 0, False, or an empty string. None is a data type of its own (NoneType) and only None can be None.

## random.randint
die Funktion random.randint(10, 1) will return a random integer between 1 and 10, because the first argument is the low end of the range and the second argument is the high end. (*import random*)

## local and gobal scope
Python Global variables are those which are not defined inside any function and have a global scope whereas Python local variables are those which are defined inside a function and their scope is limited to that function only.

- Code in the global scope cannot use any local variables.

- However, a local scope can access global variables.

- Code in a function’s local scope cannot use variables in any other local scope.

- You can use the same name for different variables if they are in different scopes. That is, there can be a local variable named spam and a global variable also named spam.

```python
def spam():
    eggs = 31337
spam()
print(eggs)
```
Traceback (most recent call last):
  File "C:/test3784.py", line 4, in <module>
    print(eggs)
NameError: name 'eggs' is not defined

eggs variable exists only in the local scope => that is an issue

If you ever want to modify the value stored in a global variable from in a function, you must use a global statement on that variable.

If you try to use a local variable in a function before you assign a value to it, as in the following program, Python will give you an error. To see this, type the following into the file editor and save it as sameName4.py:

```python
  def spam():
      print(eggs) # ERROR!
    eggs = 'spam local'

eggs = 'global'
   spam()
If you run the previous program, it produces an error message.


Traceback (most recent call last):
  File "C:/test3784.py", line 6, in <module>
    spam()
  File "C:/test3784.py", line 2, in spam
    print(eggs) # ERROR!
UnboundLocalError: local variable 'eggs' referenced before assignment
```
This error happens because Python sees that there is an assignment statement for eggs in the spam() function and therefore considers eggs to be local. But because print(eggs) is executed before eggs is assigned anything, the local variable eggs doesn’t exist. Python will not fall back to using the global eggs variable.

## Questions
1. Why are functions advantageous to have in your programs?

A: Functions help organize code, make it more modular, reusable, and easier to maintain.

2. When does the code in a function execute: when the function is defined or when the function is called?

A: when the function is called

3. What statement creates a function?

A: `def`

4. What is the difference between a function and a function call?

A: A function is just a block of code. The function call is the act of executing it 

5. How many global scopes are there in a Python program? How many local scopes?

A: only one. 

6. What happens to variables in a local scope when the function call returns?

A: Variables in a local scope are destroyed when the function call returns, and their values are lost.

7. What is a return value? Can a return value be part of an expression?

A: A return value is the value that a function gives back when it finished executing and yes. 

8. If a function does not have a return statement, what is the return value of a call to that function?

A: the return value is `None` in this case. 

9. How can you force a variable in a function to refer to the global variable?

A: one can use `global`

10. What is the data type of None?

A: the type of `None`is `NonType`

11. What does the import areallyourpetsnamederic statement do?

A: import the areallyourpetsnamederic library. But i would "guess" that this library does not exist.. so there will be an `Error`.

12. If you had a function named bacon() in a module named spam, how would you call it after importing spam?

A: i would call it `spam.bacon`

13. How can you prevent a program from crashing when it gets an error?

A: `try` and `expect`could be used or export the problematic block of code and run the `step by step thingy`

14. What goes in the try clause? What goes in the except clause?

A: The code that might raise an error goes in the `try` clause, and the code to handle the error goes in the `except` clause.