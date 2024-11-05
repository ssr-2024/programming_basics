# Chapter 1 - Python Basics

*expression*: most basic kind of programming instruction. it consists:
-  *values*
- *operators*


math operators:
Operator| Operation| 
-------- | -------- | 
**  | Exponent  | 
%   | Modulus/remainder   | 
//  | Integer division/floored quotient
/  | Division
_*_ | Multiplication
*-* | Subtraction
*+* | Addition

order of operations:
1. **
2. _*_
3. /
4. //
5. %
6. *+*
7. *-*

## The Integer, Floating-Point, and String Data Types

*data type*: category for values
- *integer*: this type incicates values that are whole numbers
- *floats*: numbers with decimal point
- *strings*: text **(always has to be surrounded by a quote sign ('))**

## String Concatenation and Replication

- the "+" operator can also be used on string values

```python
'Alice' + 'Bob'
 
 Output = AliceBob
````
- the _*_ operator  can be used with only two numeric values (for multiplication) or one string value and one integer value (for string replication)
```python
'Alice' * 3
 
 Output = AliceAliceAlice
 ````

## Storing Values in Variables

*assignment statement*: consists of a variable name, an equal sign and the value to be stored

*overwriting*: When a variable is assigned a new value, the old value is forgotten. 

*variable names*: there are four rules:
1. it can be only one word.
2. It can use only letters, numbers, and the underscore(_)
3. It **can't** begin with a number.
4. Variable names are **case-sensitive**

## Writing a program

- *comments*: starts with a #, are ignored my Python
- *print() function*
- *input() function*: waits for the user to type some text on the keyboard and press ENTER. **It always returns a string, even if the user enters a number.**
- len() function: evaluates to the integer value of the number of characters in the string
```python
len('hello')
 
 Output = 5
 ````
- *str(), int() and float() function*: they will evaluate to the string, integer, and floating-point forms of the value you pass, respectively. 
    - The str() function is handy when you have an integer or float that you want to concatenate to a string. 
    - The int() function is also helpful if you have a number as a string value that you want to use in some mathematics
```python
print('I am ' + str(29) + ' years old.') 

Output: I am 29 years old.
````
## Questions

1. Which of the following are operators, and which are values?

- _*_ = operator
- 'hello' = value
- -88.8 = value
- *-* = operator
- / = operator
- *+* = operator
- 5 = value

2. Which of the following is a variable, and which is a string?

- spam = variable 
- 'spam' = string (enclosed in quotes)

3. Name three data types.

- integer
- floating-point number
- string

4. What is an expression made up of? What do all expressions do?

An expression is made up of *values* and *operators*. All expressions evaluate down to a single value.

5. This chapter introduced assignment statements, like ```spam = 10```. What is the difference between an expression and a statement?

- An expression is a combination of values and operators that produces a result.
- A statement is an instruction that performs some action, such as assigning a value to a variable. For example, ```spam = 10``` is a statement, while ```5 + 3``` is an expression.


6. What does the variable bacon contain after the following code runs?

- ```bacon = 20```
- ```bacon + 1```

After running this code, the variable bacon still contains 20. The expression bacon + 1 calculates 21, but the result is not assigned back to bacon. To change the value of bacon, it would need to be assigned like this: ```bacon = bacon + 1```.

7. What should the following two expressions evaluate to?

```python
'spam' + 'spamspam' 
'spam' * 3
````

They evaluate to ```spamspamspam```


8. Why is eggs a valid variable name while 100 is invalid?

Variable names must begin with a letter or an underscore, not a number. 

9. What three functions can be used to get the integer, floating-point number, or string version of a value?

- ```int()``` : Converts a value to an integer.
- ```float()``` : Converts a value to a floating-point number.
- ```str()``` : Converts a value to a string.


10. Why does this expression cause an error? How can you fix it?

```python
'I have eaten ' + 99 + ' burritos.'

```
This expression causes an error because you can't concatenate a string with an integer directly. To fix it, you need to convert the integer 99 to a string using ```str()```:
```python
'I have eaten ' + str(99) + ' burritos.'
````




























