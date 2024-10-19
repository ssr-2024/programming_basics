# Strings
## String Literals
**Single Quote**:
'This is a Cat'

**Double Quotes**
"This is Alice's cat"
(wouldn't work with single quote)

### Escape Characters
If you need to use both single quotes and double quotes in the string, you'll need to use escape characters

An escape character consists of a backslash (\ ) followed by the character you want to add to the string.
```py
'Say hi to Bob\'s mother.'
```
| Escape character | Prints as                 |
|------------------|---------------------------|
| \\'              | Single quote              |
| \\"              | Double quote              |
| \\t              | Tab                       |
| \\n              | Newline (line break)      |
| \\\\             | Backslash                 |

### Raw String
You can place an r before the beginning quotation mark of a string to make it a raw string. A raw string completely ignores all escape characters and prints any backslash that appears in the string.
```py
print(r'That is Carol\'s cat.')
#output
That is Carol\'s cat.
```
### Multiline Strings
While you can use the \n escape character to put a newline into a string, it is often easier to use multiline strings. A multiline string in Python begins and ends with either three single quotes or three double quotes. Any quotes, tabs, or newlines in between the “triple quotes” are considered part of the string. Python’s indentation rules for blocks do not apply to lines inside a multiline string.
```py
 print('''Dear Alice,

Eve's cat has been arrested for catnapping, cat burglary, and extortion.

Sincerely,
Bob''')
```
Notice that the single quote character in Eve's does not need to be escaped. Escaping single and double quotes is optional in raw strings.

### In and not in operators
The [in and not in operators](003_operators.md#membership-operators) can be used with strings just like with list values. An expression with two strings joined using in or not in will evaluate to a Boolean True or False
```py
>>> 'Hello' in 'Hello World'
True
>>> 'Hello' in 'Hello'
True
>>> 'HELLO' in 'Hello World'
False
```
### The upper(), lower(), String Methods
The upper() and lower() string methods return a new string where all the letters in the original string have been converted to uppercase or lower-case, respectively. Nonletter characters in the string remain unchanged. Enter the following into the interactive shell:
```py
spam = 'Hello world!'
spam = spam.upper() # you need this to change the original string!
#input
spam
#output
'HELLO WORLD!'

spam = spam.lower()
spam
'hello world!'
```
The upper() and lower() methods are helpful if you need to make a **case-insensitive** comparison. The strings 'great' and 'GREat' are not equal to each other. But in the following small program, it does not matter whether the user types Great, GREAT, or grEAT, because the string is first converted to lowercase.
```py
print('How are you?')
feeling = input()
if feeling.lower() == 'great':
    print('I feel great too.')
else:
    print('I hope the rest of your day is good.')
```
### The isX String Methods

The `isupper()` and `islower()` methods will return a Boolean True value if the string has at least one letter and all the letters are uppercase or lowercase, respectively. Otherwise, the method returns False. 
```py
spam = 'Hello world!'

spam.islower()
False

spam.isupper()
False

'HELLO'.isupper()
True

'abc12345'.islower()
True

'12345'.islower()
False

'12345'.isupper()
False
```
Along with islower() and isupper(), there are several string methods that have names beginning with the word is. These methods return a Boolean value that describes the nature of the string. Here are some common isX string methods:

- `isalpha()` returns True if the string consists only of letters and is not blank.

- `isalnum()` returns True if the string consists only of letters and numbers and is not blank.

- `isdecimal()` returns True if the string consists only of numeric characters and is not blank.

- `isspace()` returns True if the string consists only of spaces, tabs, and new-lines and is not blank.

- `istitle()` returns True if the string consists only of words that begin with an uppercase letter followed by only lowercase letters.

### The startswith() and endswith() String Methods
The startswith() and endswith() methods return True if the string value they are called on begins or ends (respectively) with the string passed to the method; otherwise, they return False. Enter the following into the interactive shell:
```py
'Hello world!'.startswith('Hello')
True
'Hello world!'.endswith('world!')
True
'abc123'.startswith('abcdef')
False
'abc123'.endswith('12')
False
'Hello world!'.startswith('Hello world!')
True
'Hello world!'.endswith('Hello world!')
True
```
These methods are useful alternatives to the [== equals operator](003_operators.md#comparison-operators) if you need to check only whether the first or last part of the string, rather than the whole thing, is equal to another string.
### rjust(), ljust(), and center()
The rjust() and ljust() string methods return a padded version of the string they are called on, with spaces inserted to justify the text. 
- The first argument to both methods is an integer length for the justified string.
- An optional second argument to rjust() and ljust() will specify a fill character other than a space character.

These methods are especially useful when you need to print tabular data that has the correct spacing:
```py
def printPicnic(itemsDict, leftWidth, rightWidth):
    print('PICNIC ITEMS'.center(leftWidth + rightWidth, '-'))
    for k, v in itemsDict.items():
        print(k.ljust(leftWidth, '.') + str(v).rjust(rightWidth))
picnicItems = {'sandwiches': 4, 'apples': 12, 'cups': 4, 'cookies': 8000}
printPicnic(picnicItems, 12, 5)
printPicnic(picnicItems, 20, 6)
```
**Output:**:
```
---PICNIC ITEMS--
sandwiches..    4
apples......   12
cups........    4
cookies..... 8000
-------PICNIC ITEMS-------
sandwiches..........     4
apples..............    12
cups................     4
cookies.............  8000
```
### Pyperclip Module
The pyperclip module has copy() and paste() functions that can send text to and receive text from your computer’s clipboard. Sending the output of your program to the clipboard will make it easy to paste it to an email, word processor, or some other software.
Pyperclip does not come with Python:
```py
import pyperclip
pyperclip.copy('Hello world!')
pyperclip.paste()
'Hello world!'
```
Of course, if something **outside of your program changes** the clipboard contents, the paste() function will return it.
```py
pyperclip.paste()
'For example, if I copied this sentence to the clipboard and then called
paste(), it would look like this:'
```





## Formatierte Ausgabe `f'2 * 2 = {2 * 2}'`

## Beispiele
