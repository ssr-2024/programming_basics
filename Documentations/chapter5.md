# Dictionaries and Structuring Data

## Table of content
- [Dictionaries and Structuring Data](#dictionaries-and-structuring-data)
  - [Table of content](#table-of-content)
    - [The Dictionary Data Type](#the-dictionary-data-type)
    - [Dictionaries vs. Lists](#dictionaries-vs-lists)
    - [The `keys()`, `values()`, and `items()` Methods](#the-keys-values-and-items-methods)
    - [Checking Whether a Key or Value Exists in a Dictionary](#checking-whether-a-key-or-value-exists-in-a-dictionary)
    - [The `setdefault()` Method](#the-setdefault-method)
    - [Pretty Printing](#pretty-printing)
    - [Questions](#questions)


### The Dictionary Data Type

Like a list, a dictionary is a collection of many values. But unlike indexes for lists, indexes for dictionaries can use many different data types, not just integers. Indexes for dictionaries are called keys, and a key with its associated value is called a key-value pair.

```python
>>> myCat = {'size': 'fat', 'color': 'gray', 'disposition': 'loud'}

>>> myCat['size']
'fat'
>>> 'My cat has ' + myCat['color'] + ' fur.'
'My cat has gray fur.'
```

### Dictionaries vs. Lists

Unlike lists, items in dictionaries are unordered. The first item in a list named spam would be `spam[0]`. But there is no “first” item in a dictionary. While the order of items matters for determining whether two lists are the same, it does not matter in what order the key-value pairs are typed in a dictionary.

```python
>>> spam = ['cats', 'dogs', 'moose']
>>> bacon = ['dogs', 'moose', 'cats']
>>> spam == bacon
False
>>> eggs = {'name': 'Zophie', 'species': 'cat', 'age': '8'}
>>> ham = {'species': 'cat', 'age': '8', 'name': 'Zophie'}
>>> eggs == ham
True
```

### The `keys()`, `values()`, and `items()` Methods

There are three dictionary methods that will return list-like values of the dictionary’s keys, values, or both keys and values: `keys()`, `values()`, and `items()`. The values returned by these methods are not true lists: They cannot be modified and do not have an `append()` method. But these data types (`dict_keys`, `dict_values`, and `dict_items`, respectively) can be used in for loops.

```python
>>> spam = {'color': 'red', 'age': 42}
>>> for v in spam.values():
        print(v)

red
42

>>> for k in spam.keys():
        print(k)

color
age
>>> for i in spam.items():
        print(i)

('color', 'red')
('age', 42)
```

If you want a true list from one of these methods, pass its list-like return value to the `list()` function. Enter the following into the interactive shell:

```python
>>> spam = {'color': 'red', 'age': 42}
>>> spam.keys()
dict_keys(['color', 'age'])
>>> list(spam.keys())
['color', 'age']
```

### Checking Whether a Key or Value Exists in a Dictionary

```python
>>> spam = {'name': 'Zophie', 'age': 7}
>>> 'name' in spam.keys()
True
>>> 'Zophie' in spam.values()
True
>>> 'color' in spam.keys()
False
>>> 'color' not in spam.keys()
True
```

### The `setdefault()` Method

The `setdefault()` method is a nice shortcut to ensure that a key exists. Here is a short program that counts the number of occurrences of each letter in a string.

```python
message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}

for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1

print(count)
```

The program loops over each character in the message variable’s string, counting how often each character appears. The `setdefault()` method call ensures that the key is in the count dictionary (with a default value of 0) so the program doesn’t throw a KeyError error when `count[character] = count[character] + 1` is executed. When you run this program, the output will look like this:


{' ': 13, ',': 1, '.': 1, 'A': 1, 'I': 1, 'a': 4, 'c': 3, 'b': 1, 'e': 5, 'd': 3, 'g': 2, 'i':
6, 'h': 3, 'k': 2, 'l': 3, 'o': 2, 'n': 4, 'p': 1, 's': 3, 'r': 5, 't': 6, 'w': 2, 'y': 1}

### Pretty Printing 

If you import the pprint module into your programs, you’ll have access to the `pprint()` and `pformat()` functions that will “pretty print” a dictionary’s values. This is helpful when you want a cleaner display of the items in a dictionary than what print() provides. **The `pprint.pprint()` function is especially helpful when the dictionary itself contains nested lists or dictionaries.**

### Questions

Q:1. What does the code for an empty dictionary look like?

`empty_dict = {}`


Q:2. What does a dictionary value with a key 'foo' and a value 42 look like?

`dict = {'foo':42}`

Q:3. What is the main difference between a dictionary and a list?

- A list is an ordered collection of items accessed by their index (position), e.g., `my_list[0]`.
- A dictionary is a collection of key-value pairs, where items are accessed by their key, e.g., `my_dict['key']`.

Q:4. What happens if you try to access spam['foo'] if spam is {'bar': 100}?

`KeyError`

Q:5. If a dictionary is stored in spam, what is the difference between the expressions 'cat' in spam and 'cat' in spam.keys()?

no difference

Q:6. If a dictionary is stored in spam, what is the difference between the expressions 'cat' in spam and 'cat' in spam.values()?

difference between `Key` and `Value`. `'cat' in spam`checks for the key. `'cat' in spam.values()`checks for the value. 

Q:7. What is a shortcut for the following code?


if 'color' not in spam:
    spam['color'] = 'black'

`spam.setdefault('color', 'black')`


Q:8. What module and function can be used to “pretty print” dictionary values?

`pprint` module
