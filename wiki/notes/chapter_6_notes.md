# Manipulating Strings

### String Literals
- strings can begin and end with:
    - single quotes (')
    - double quotes (")
        - benefit: the string can have a sinqle quote character in it
    - escape characters which consists of a backslash followed by the character you want to add to the string

    Escape character| Prints as|       
    -------- | -------- | 
    \\' | Single quote  | 
    \\"   | Double quote   | 
    \t  | Tab
    \n  | Newline (line break)
    \\\ | Backslash

 - *raw string*: place an r before the beginning quotation mark of a string; it ignores all escape characters
 - *multiline strings*: begins and ends with three single quotes or three double quotes
    - it is often used for comments

### Indexing and Slicing Strings

- Strings use indexes and slices the same way lists do
    - the starting index is included and the ending index is not
    - slicing a string does not modify the original string

```python
test = "Let's count!"
test[5]

Output: ' '

newtest = test[6:]
newtest

Output: 'count!'
```
### The In and Not In Operators

The ```in``` and ```not in``` operators can be used with strings just like with list value. It will evaluate to a Boolean True or False.

### Useful String Methods

- ```upper()```and ```lower()```: returns a new string where all the letters in the original string have been converted to uppercase or lower-case
    - it doesn't change the string itself
    - if you want to change the original string, you have to call ```upper()``` or ```lower()``` on the string and then assign the new string to the variable where the original was stored
    - useful to make a case-insensitive comparison

```python
test = "Let's count!"
test.upper()

Output: "LET'S COUNT!"
````
- ```isupper()```and ```islower()```: will return a Boolean True value if the string has at least one letter and **all** the letters are uppercase or lowercase.

```python

test = "ELIANE"
test.isupper()

Output: True
```

- there are several string methods that have names beginning with the word *is*. These methods return a Boolean value that describes the nature of the string.
    - ```isalpha()``` returns True if the string consists only of letters and is not blank
    - ```isalnum()``` returns True if the string consists only of letters and numbers and
is not blank
    - ```isdecimal()``` returns True if the string consists only of numeric characters and
is not blank
    - ```isspace()``` returns True if the string consists only of spaces, tabs, and new-
lines and is not blank
    - ```istitle()``` returns True if the string consists only of words that begin with an
uppercase letter followed by only lowercase letters

```python
'This Is A Title'.istitle()

Output: True
```
- ```startswith()```and ```endswith()```: returns True if the string value they are called on begins or ends (respectively) with the string passed to the method

```python
'This Is A Title'.startswith('Is')

Output: False
```

- ```join()```: useful when you have a list of strings that need to be joined together into a single string value
    - the string ```join()``` calls on is inserted between each string of the list argument
    - is called on a string value and is passed a list value

```python

'Not'.join(['true','false', 'true'])

Output: 'trueNotfalseNottrue'
```

- ```split()```: does the opposite
    - is called on a string value and returns a list of strings

```python

'trueNotfalseNottrue'.split('Not')

Output: ['true', 'false', 'true']
```
- ```rjust()```and ```ljust()```: return a padded version of the string they are called on, with spaces inserted to justify the text
- ```center()```: centers the text
    - first argument: integer length for the justified string
    - optional second argument: will specify a fill character other than a space character

```python
'Title'.rjust(15,'_')

Output: '__________Title'
````
- ```strip()```: will return a new string without any whitespace characters at the beginning or end.
- ```lstrip()```and ```rstrip()```: will remove whitespace characters from the left and right ends

```python
test = '          Eliane   '

test.strip()

Output: 'Eliane'

test.lstrip()

Output: 'Eliane   '
````

- *pyperclip* module: has ```copy()``` and ```paste()```functions that can send text to and receive text from your computer’s clipboard
    - **Pyperclip does not come with Python**


## Questions

1. What are escape characters?

Escape characters are special characters in strings that are preceded by a backslash (\\) to represent characters that are otherwise difficult or impossible to type directly. 

2. What do the \n and \t escape characters represent?

The escape characters \n and \t represent:

- \n: Newline (moves the text cursor to the next line).
- \t: Tab 

3. How can you put a \ backslash character in a string?

To put a backslash (\\)  character in a string, you need to escape it by using a double backslash.

4. The string value ```"Howl's Moving Castle"``` is a valid string. Why isn’t it a problem that the single quote character in the word Howl's isn’t escaped?

Because the string is enclosed in double quotes allowing you to include a single quote without needing to escape it.

5. If you don’t want to put \n in your string, how can you write a string with
newlines in it?

To write a string with newlines without using the escape sequence \n, you can use triple quotes (either ''' or """).


6. What do the following expressions evaluate to?

- 'Hello world!'[1]:
'e'
- 'Hello world!'[0:5]:
'Hello'
- 'Hello world!'[:5]:
'Hello'
- 'Hello world!'[3:]:
'lo world!'

7. What do the following expressions evaluate to?

- 'Hello'.upper():
'HELLO'
- 'Hello'.upper().isupper():
True
- 'Hello'.upper().lower():
'hello'

8. What do the following expressions evaluate to?

- 'Remember, remember, the fifth of November.'.split(): ['Remember,', 'remember,', 'the', 'fifth', 'of', 'November.']
- '-'.join('There can be only one.'.split())
'There-can-be-only-one.'

9. What string methods can you use to right-justify, left-justify, and center a
string?
- Right-justify: ```str.rjust()```
- Left-justify: ```str.ljust()```
- Center: ```str.center()```

10. How can you trim whitespace characters from the beginning or end of a
string?

- Trim from the beginning: ```str.lstrip()```
- Trim from the end: ```str.rstrip()```
- Trim from both ends: ```str.strip()```




