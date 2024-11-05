# Chapter 2 - Flow Control

*Flow control statements* can decide which Python instructions to execute under which statements.

## Boolean Values

*Boolean data type*: has only two values: **True** and **False**
- They are used in expressions.
- They can be stored in variables.
- They can't be used for variable names.

## Comparison Operators

They compare two values and evaluate down to a single Boolean value.

Operator| Meaning| 
-------- | -------- | 
==  | Equal to | 
!=  | Note equal to   | 
<  | Less than
*>* | Greater than
<= | Less than or equal to
*>=* | Greater than or equal to

These operators evaluate to **True** or **False**.

An *integer* or *floating-point* value will alwys be unequal to a string value.

The <, >, <=, and >= operators work properly **only with integer and floating-point values.**

Attention:
- The == operator (equal to) asks whether two values are the same as each
other.
- The = operator (assignment) puts the value on the right into the variable on the left. 

## Boolean Operators

There are three operators to compare Boolean values:
- and
- or
- not 

The *and* and *or* operators always take two Boolean values (or expressions), so they’re considered binary operators.

- The *and* operator evaluates an expression to True if both Boolean values are True; otherwise, it evaluates to False.
- The *or* operator evaluates an expression to True if either of the two Boolean values is True. If both are False, it evaluates to False.

The *not* operator operates operates on only one Boolean value (or expression). 
- It simply evalues to the opposite Boolean Value.

```python
not True
Output = False
````

Boolean and comparisoan operators can be mixed.
```python
(4<5) and (5<6)
Outpit = True
````

Order of operations:
1. *not*
2. *and*
3. *or*

## Elements of Flow Control

- *Condition*: expression, that evaluates to True or False
- *Block of code* (clause): Lines of Python code can be grouped together in blocks. There are three rules:
    1. Blocks begin when the indentation increases.
    2. Blocks can contain other blocks.
    3. Blocks end when the indentation decreases to zero or to a containing block’s indentation.

## Flow Control Statements
All flow control statements end with a colon (:) and are followed by a new block of code (the clause).

- *if statement*: it will  execute if the statement's condition is True
- *else statement*: it will execute only when the if statement's condition is False
- *elif statement*: is an “else if” statement that always follows an *if* or another *elif* statement. It provides another condition that is checked only if all of the previous conditions were False. The rest of the elif clauses are automatically skipped once a True condition has been found. If both conditions are False, then both of the clauses are skipped.
```python
if name == 'Alice':     
    print('Hi, Alice.') 
elif age < 12:     
    print('You are not Alice, kiddo.') 
elif age > 2000:     
    print('Unlike you, Alice is not an undead, immortal vampire.') 
elif age > 100:     
    print('You are not Alice, grannie.')
```
- *while statement* (loop): The code in a while clause will be executed as long as the while statement’s condition is True.

- **Difference between a *while statement* and an *if statement*:** 
    - At the end of an if clause, the program execution continues after the if statement. But at the end of a while clause, the program execution jumps back to the start of the while statement. 
    - In the while loop, the condition is always checked at the start of each iteration (that is, each time the loop is executed). If the condition is True, then the clause is executed, and afterward, the condition is checked again. The first time the condition is found to be False, the while clause is skipped.

- *break statement*: it simply contains the *break* keyword
- *continue statement*: the program execution immediately jumps back to the start of the loop and reevaluates the loop’s condition.

```python
while True:       
    print('Who are you?')       
    name = input()    
    if name != 'Joe':         
        continue       
    print('Hello, Joe. What is the password? (It is a fish.)')   
    password = input()      
     if password == 'swordfish':
        break  
print('Access granted.')
````

- *range function*: If you want to execute a block of code only a certain number of times
    - You can use break and continue statements inside *for loops* as well
    - Some functions can be called with multiple arguments separated by a comma
    - The first argument will be where the for loop’s variable starts, and the second argument will be up to, but not including, the number to stop at.
    - The range() function can also be called with three arguments. The first two arguments will be the **start** and **stop** values, and the third will be the **step argumen**t. The step is the amount that the variable is increased by after each iteration.


```python
print('My name is') 
for i in range(5):     
    print('Jimmy Five Times (' + str(i) + ')')

Output:
 My name is 
 Jimmy Five Times (0) 
 Jimmy Five Times (1) 
 Jimmy Five Times (2) 
 Jimmy Five Times (3) 
 Jimmy Five Times (4)
 ```
```python
for i in range(0,10,2):     
    print(i)

Output:
0
2
4
6
8
```    
## Importing Modules

All Python programs can call a basic set of functions called built-in functions,
including the ```print()```, ```input()```, and ```len()``` functions you’ve seen before. Python also comes with a set of modules called the standard library. Each module is a Python program that contains a related group of functions that can be embedded in your programs. For example, the **math** module has mathematics-related
functions, the **random** module has random number–related functions, and so on. 

Before you can use the functions in a module, you must import the module with an import statement. 

```python
import random
````
```python
from random import *
````
## Ending a program early

By calling ```sys.exit()``` function

## Questions

1. What are the two values of the Boolean data type? How do you write them?

- ```True```
- ```False```

They are written with an uppercase first letter.

2. What are the three Boolean operators?

- ```and```
- ```or```
- ```not```

3. Write out the truth tables of each Boolean operator (that is, every possible combination of Boolean values for the operator and what they evaluate to).
- and Operator:

A| B| A and B
-------- | -------- | ------- | 
True  | True | True
True  | False   | False
False  | True | False
False |False | False


- or Operator:

A| B| A or B
-------- | -------- | ------- | 
True  | True | True
True  | False   | True
False  | True | True
False |False | False

- not Operator:

A| not A| 
-------- | -------- | 
True  | False
False  | True   


4. What do the following expressions evaluate to?

(5 > 4) and (3 == 5) False <br>
not (5 > 4) False <br>
(5 > 4) or (3 == 5) True <br>
not ((5 > 4) or (3 == 5)) False <br>
(True and True) and (True == False) False <br>
(not False) or (not True) True 

5. What are the six comparison operators?

- ```==```
- ```!=```
- ```<```
- ```>```
- ```<=```
- ```>=```


6. What is the difference between the equal to operator and the assignment operator?

- The == operator (equal to) asks whether two values are the same as each
other.
- The = operator (assignment) puts the value on the right into the variable on the left.


7. Explain what a condition is and where you would use one.

A condition is an expression that evaluates to ```True``` or ```False```. Conditions are used in flow control statements like ```if```, ```while```, and ```for``` to determine which block of code should be executed.



8. Identify the three blocks in this code:

```python
spam = 0 
if spam == 10:     
    print('eggs')    
    if spam > 5:         
        print('bacon')     
    else:         
        print('ham')     
    print('spam')
print('spam')
```

- First block: if spam == 10: (the code inside this condition, starting with print('eggs'))
- Second block: if spam > 5: (nested within the first block)
- Third block: The final print('spam') outside of the if statement.

9. Write code that prints Hello if 1 is stored in spam, prints Howdy if 2 is stored in spam, and prints Greetings! if anything else is stored in spam.

```python
spam = int(input("Enter a number: "))
if spam == 1:
    print("Hello")
elif spam == 2:
    print("Howdy")
else:
    print("Greetings!")
```


10. What can you press if your program is stuck in an infinite loop?

Ctrl + C

11. What is the difference between ```break``` and ```continue```?

- ```break```: Immediately exits the current loop.
- ```continue```: Skips the rest of the current loop iteration and moves on to the next iteration.

12. What is the difference between range(10), range(0, 10), and range(0, 10,1) in a for loop?

- range(10) : Generates numbers from 0 to 9.
- range(0, 10) : Explicitly starts at 0 and goes to 9.
- range(0, 10, 1) : Starts at 0, goes to 9, and increments by 1 (same as the previous two).

13. Write a short program that prints the numbers 1 to 10 using a for loop. Then write an equivalent program that prints the numbers 1 to 10 using a while loop.

- For-Loop:

```python
for i in range (1,11):
    print(i)
````

- While-Loop:

```python
i=1
while i <=10:
    print(i)
    i += 1
```


14. If you had a function named bacon() inside a module named spam, how would you call it after importing spam?

```python
import spam
spam.bacon()
```





















