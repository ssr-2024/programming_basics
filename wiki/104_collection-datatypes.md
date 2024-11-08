# Collection Data Types

In Python, four primary data types help to organize data into collections:
- **Lists**
- **Tuples**
- **Sets**
- **Dictionaries**

We’ll focus on Lists and Dictionaries here.

## Lists

A `list` is a collection of values stored in a specific order. Each value within the list is called an *item*. Lists are denoted by square brackets `[]`, with items separated by commas. Lists can contain various data types, including other lists.

### Indexing
List items can be accessed and modified using *indexes*, which start at 0 for the first item. Python also supports negative indexing, where `-1` accesses the last item, `-2` accesses the second-to-last, and so forth.

```python
planets = ['mars', 'venus', 'earth']
print(planets[1])  # Output: 'venus'
```

Indexes can also be used to change values at a specific position in the list.

```python
planets[1] = 'jupiter'
print(planets)  # Output: ['mars', 'jupiter', 'earth']
```

### Getting Sublists with Slices
*Slicing* retrieves a portion of a list, specified by start and end indexes.

```python
planets = ['mars', 'venus', 'earth']
print(planets[0:2])  # Output: ['mars', 'venus']
```

### `range()` and `list()`
The `range()` function is often used to generate a sequence of numbers, and the `list()` function can convert that sequence into a list.

```python
numbers = list(range(5))  # Output: [0, 1, 2, 3, 4]
```

### Functions and Methods for Lists
Several functions and methods facilitate list manipulation:
- `len(list)`: returns the length of the list.
- `+` and `*` operators: concatenate and replicate lists, respectively.
- `in` and `not in`: check if a value exists within a list.
- `append()`: adds an item to the end of the list.
- `insert(index, item)`: inserts an item at a specified index.
- `remove(item)`: removes the first occurrence of an item.
- `sort()`: sorts items in ascending order, with options for reversing or case-insensitive sorting.

### Nested Lists
Lists can contain other lists, enabling the creation of complex data structures.

```python
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix[1][2])  # Output: 6
```
For some more informations and more examples about lists, click on this link: [Chapter 4 - Lists](notes/chapter_4_notes.md)


## Dictionaries

A `dictionary` is a collection that stores values by *keys* rather than by position. Each key-value pair is separated by a colon, and pairs are separated by commas within braces `{}`. Dictionaries are useful for associating data, like a word’s definition or a student's details.

```python
my_cat = {'size': 'fat', 'color': 'orange', 'disposition': 'shy'}
print("My cat has " + my_cat['color'] + " fur.")  # Output: 'My cat has orange fur.'
```

### Dictionary Methods
Dictionaries come with several helpful methods for accessing and modifying data:
- `keys()`: returns a list-like view of all keys.
- `values()`: returns a list-like view of all values.
- `items()`: returns a list of key-value pairs.
- `get(key, default)`: retrieves a value for a key, with an option for a default return if the key doesn’t exist.
- `setdefault(key, value)`: sets a default value if the key doesn’t already exist in the dictionary.


For some more informations and more examples about dictionaries, click on this link: [Chapter 5 - Dictionaries](notes/chapter_5_notes.md)


