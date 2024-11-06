# Chapter 4

## Inhaltsverzeichnis
- [Chapter 4](#chapter-4)
  - [Inhaltsverzeichnis](#inhaltsverzeichnis)
    - [The List Data Type](#the-list-data-type)
    - [Getting Individual Values in a List with Indexes](#getting-individual-values-in-a-list-with-indexes)
    - [Getting Sublists with Slices](#getting-sublists-with-slices)
    - [Getting a List’s Length with len()](#getting-a-lists-length-with-len)
    - [Changing Values in a List with Indexes](#changing-values-in-a-list-with-indexes)
    - [Removing Values from Lists with del Statements](#removing-values-from-lists-with-del-statements)
    - [The in and not in Operators](#the-in-and-not-in-operators)
    - [Finding a Value in a List with the index() Method](#finding-a-value-in-a-list-with-the-index-method)
    - [Adding Values to Lists with the append() and insert() Methods](#adding-values-to-lists-with-the-append-and-insert-methods)
    - [Removing Values from Lists with remove()](#removing-values-from-lists-with-remove)
    - [Sorting the Values in a List with the sort() Method](#sorting-the-values-in-a-list-with-the-sort-method)
  - [Questions](#questions)


### The List Data Type

A list is a value that contains multiple values in an ordered sequence.

```python
>>> [1, 2, 3]
[1, 2, 3]
>>> ['cat', 'bat', 'rat', 'elephant']
['cat', 'bat', 'rat', 'elephant']
>>> ['hello', 3.1415, True, None, 42]
['hello', 3.1415, True, None, 42]
>>> spam = ['cat', 'bat', 'rat', 'elephant']
>>> spam
['cat', 'bat', 'rat', 'elephant']
   ```

### Getting Individual Values in a List with Indexes

```python
>>> spam = [['cat', 'bat'], [10, 20, 30, 40, 50]]
>>> spam[0]
['cat', 'bat']
>>> spam[0][1]
'bat'
>>> spam[1][4]
50
```

The first index dictates which list value to use, and the second indicates the value within the list value. For example, spam[0][1] prints 'bat', the second value in the first list. If you only use one index, the program will print the full list value at that index.

While indexes start at 0 and go up, you can also use negative integers for the index. The integer value -1 refers to the last index in a list, the value -2 refers to the second-to-last index in a list, and so on.

### Getting Sublists with Slices

```python
>>> spam = ['cat', 'bat', 'rat', 'elephant']
>>> spam[0:4]
['cat', 'bat', 'rat', 'elephant']
>>> spam[1:3]
['bat', 'rat']
>>> spam[0:-1]
['cat', 'bat', 'rat'] 
```

Just as an index can get a single value from a list, a slice can get several values from a list, in the form of a new list. A slice is typed between square brackets, like an index, but it has two integers separated by a colon. Notice the difference between indexes and slices.

### Getting a List’s Length with len()

The len() function will return the number of values that are in a list value passed to it, just like it can count the number of characters in a string value. Enter the following into the interactive shell:

```python
>>> spam = ['cat', 'dog', 'moose']
>>> len(spam)
3
```

### Changing Values in a List with Indexes

Normally a variable name goes on the left side of an assignment statement, like spam = 42. However, you can also use an index of a list to change the value at that index. For example, spam[1] = 'aardvark' means “Assign the value at index 1 in the list spam to the string 'aardvark'.” Enter the following into the interactive shell:

```python
>>> spam = ['cat', 'bat', 'rat', 'elephant']
>>> spam[1] = 'aardvark'
>>> spam
['cat', 'aardvark', 'rat', 'elephant']
>>> spam[2] = spam[1]
>>> spam
['cat', 'aardvark', 'aardvark', 'elephant']
>>> spam[-1] = 12345
>>> spam
['cat', 'aardvark', 'aardvark', 12345]
```

### Removing Values from Lists with del Statements

```python
>>> spam = ['cat', 'bat', 'rat', 'elephant']
>>> del spam[2]
>>> spam
['cat', 'bat', 'elephant']
>>> del spam[2]
>>> spam
['cat', 'bat']
```

### The in and not in Operators

```python
>>> 'howdy' in ['hello', 'hi', 'howdy', 'heyas']
True
>>> spam = ['hello', 'hi', 'howdy', 'heyas']
>>> 'cat' in spam
False
```

### Finding a Value in a List with the index() Method

List values have an index() method that can be passed a value, and if that value exists in the list, the index of the value is returned. If the value isn’t in the list, then Python produces a ValueError error. Enter the following into the interactive shell:

```python
>>> spam = ['hello', 'hi', 'howdy', 'heyas']
>>> spam.index('hello')
0
>>> spam.index('heyas')
3
```

### Adding Values to Lists with the append() and insert() Methods

To add new values to a list, use the append() and insert() methods. Enter the following into the interactive shell to call the append() method on a list value stored in the variable spam:

```python
>>> spam = ['cat', 'dog', 'bat']
>>> spam.append('moose')
>>> spam
['cat', 'dog', 'bat', 'moose']
```


### Removing Values from Lists with remove()

The remove() method is passed the value to be removed from the list it is called on. Enter the following into the interactive shell:

```python
>>> spam = ['cat', 'bat', 'rat', 'elephant']
>>> spam.remove('bat')
>>> spam
['cat', 'rat', 'elephant']
``` 

### Sorting the Values in a List with the sort() Method

Lists of number values or lists of strings can be sorted with the sort() method. For example, enter the following into the interactive shell:

```python
>>> spam = [2, 5, 3.14, 1, -7]
>>> spam.sort()
>>> spam
[-7, 1, 2, 3.14, 5]
>>> spam = ['ants', 'cats', 'dogs', 'badgers', 'elephants']
>>> spam.sort()
>>> spam
['ants', 'badgers', 'cats', 'dogs', 'elephants']
```

## Questions

1. What is []?

A: an empty list.

2. How would you assign the value 'hello' as the third value in a list stored in a variable named spam? (Assume spam contains [2, 4, 6, 8, 10].)

For the following three questions, let’s say spam contains the list ['a', 'b', 'c', 'd'].

A: `spam[2]='hello'`

3. What does spam[int(int('3' * 2) // 11)] evaluate to?

A: 3 bc '3'*2=33 as a string => with int() it get a integer. 33//11 = 3. 

4. What does spam[-1] evaluate to?

A: last entry from the list

5. What does spam[:2] evaluate to?

For the following three questions, let’s say bacon contains the list [3.14, 'cat', 11, 'cat', True].

A:it returns all elements from the start up to, but not including, index 2 => 3.14 and 'cat'

6. What does bacon.index('cat') evaluate to?

A: 1

7. What does bacon.append(99) make the list value in bacon look like?

A: `[3.14, 'cat', 11, 'cat', True, 99]`

8. What does bacon.remove('cat') make the list value in bacon look like?

A: `[3.14, 11, 'cat', True, 99]`

9. What are the operators for list concatenation and list replication?

A: The operator for list concatenation is `+`, and the operator for list replication is `*`.

10. What is the difference between the append() and insert() list methods?

A: `append()` adds an item to the end of the list, while `insert()` adds an item at a specified index.

11. What are two ways to remove values from a list?

A: `remove()` or `del spam[2]`

12. Name a few ways that list values are similar to string values.

A: Both lists and strings are ordered collections, allow indexing and slicing, and can be iterated over using loops.

13. What is the difference between lists and tuples?

A: Lists are mutable (they can be changed after creation), while tuples are immutable (they cannot be changed after creation).

14. How do you type the tuple value that has just the integer value 42 in it?

A: `(42,)`

15. How can you get the tuple form of a list value? How can you get the list form of a tuple value?

A: You can convert a list to a tuple using `tuple(list_name)` and a tuple to a list using `list(tuple_name)`.

16. Variables that “contain” list values don’t actually contain lists directly. What do they contain instead?

A: Variables contain references to the list values, not the list itself.

17. What is the difference between copy.copy() and copy.deepcopy()?

A: `copy.copy()` creates a shallow copy of a list (it copies the list but not nested objects). `copy.deepcopy()` creates a deep copy, which duplicates the list and all nested objects within it.