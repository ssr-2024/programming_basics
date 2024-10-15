# Automate the Boring Stuff

# Chapter 1 - Python Basics
add notes

# Chapter 2 - Flow Control
add notes

### elif-Statements
add notes
add vampire.py example code

```py
# Playing and testing elif-Statements

name=input('Please enter your name ')
age=input('Please enter your age ')

if name == 'Alice':
    print('Hi Alice')
elif int(age) < 12:
    print('You are not Alice, kiddo')
elif int(age) > 2000:
    print('Unlike you, Alice is not an undead, immortal vampire.')
elif int(age) > 100:
    print('You are not Alice, grannie') # example from Automate the Boring Stuff
# However, what happens if the person is older than 12 but younger than 100? Therefore:
elif int(age) < 100:
    print('You might be as old as Alice, but you are not her.') # Adds an answer in case the person is Alice's age
# Otherwise an else-Statement would've done the trick, according to the book.
```

### While-Loop-Statements
Executes a block of code over and over again as long as the *while-statement* condition is *True*. 
A *while-statement* always contains

- the *while* keyword
- a condition (that evaluates to a Boolean Value) **add link to Boolean Value**
- a colon
- in the next line: the *while* clause (an indented block of code)

```py
# Create an annoying While-Loop

name=''
while name !='your name':
    print('Please type your name.')
    name=input()
print('Thank you.')
```
### Break-Statements
A shortcut to break out of a while-loop early. In code, the *break* statement just contains the word *'break'*.

```py
# Create a finite while-loop using a break-statement

while True:
    print('Please type your name')
    name=input()
    if name == 'your name':
        break
print('Thank you')
```

### Continue-Statements
Used inside loops. When reaching a *continue-statement*, the program execution jumps back to the start of the loop and the condition is re-evaluated. 

#### Tip
---
    When trapped in an Infinite Loop: press CTRL-C
---

```py
# Use the continue-statement within a while-loop

while True:
    print('Who are you?')
    name=input()
    if name !='Johanna':
        continue
    print('Hello, Johanna. What is the password? (It is a fish.)')
    password=input()
    if password == 'swordfish':
        break
print('Access granted.')
```

#### "Truthy" and "Falsey" Values
----
When used in conditions the following input() will be considered as false:

    0, 0.0 and '' 
These values may make the code easier to read.

### For-Loops and the range() function
Runs a loop for a certain number of times.
In code, this looks like this:
```py
for i in range(5):
    the for-clause
```

#### Note

    continue- and break-statements can only be used inside while- and for-loops. Otherwise Python will show an Error.




# Chapter 3 - Functions
# Chapter 4 - Lists
# Chapter 5 - Dictionairies and Structuring Data
# Chapter 6 - Manipulating Strings