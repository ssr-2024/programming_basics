# Chapter 4 - Lists

# The List Data Type

- *list*: value that contains multiple values in ordered sequence
- *list value*:  list itself (not the values inside the list value)
- *items*: the values inside  the list value 

- always begins and ends qith **square brackets []**
- items have to be seperated with **commas**
- lists can obtain other lists


# Indexes
- *index*: integer inside the square brackets that follow the list
- *negative indexes*: -1 refers to the last index, -2 to the second-to-last,...

**Attention**: 
- string values have to be typed with quote characters
- indexes can be only integer values, not floats

```python
planets = ['mars', 'venus', 'earth']
planets[1]

Output = 'venus'
````
- indexes can also be used to change the value at the index

```python
planets = ['mars', 'venus', 'earth']
planets[1] = 'jupiter'
planets

Output ['mars', 'jupiter', 'earth']
````

# Getting Sublists with Slices
-  *slice*: can get several values from a list, in the form of a new list
    - is typed between square brackets []
    - has two integers seperated by colon
        - first integer: index where the sclice starts
        - second integer: index where the ends; **the value at the second index is not included**
    - the first or the second index can be left
        - leaving the first index = using 0
        - leaving the second index = using the length of the list

```python
planets = ['mars', 'venus', 'earth']
planets[0:2]

Output: ['mars', 'venus']
````
# Different functions

- ```len()```function: will return the number of values 
- *+* operator: can combine two lists to create a **new** list 
- _*_ operator: can be used for list replication
- ```del```statement: will delete values at an index in a list
- to determine wheter a value is or isn't in a list:
    - ```in```
    - ```not in```
    - it will evaluate to a Boolean value
  
```python
planets = ['mars', 'venus', 'earth']
'saturn' in planets

Output: False
```
- *multiple assignment trick*: shortcut that lets you assign multiple variables with the values in a list in one line of code
    - numbers of variables and the length of the list must be **exactly equal**

```python
cat = ['fat', 'orange', 'loud']
size, colot, disposition = cat
```

- *augmented assignment operators*: for the +,-,*,/ and % operators
```python
planets = ['mars', 'venus', 'earth']
planets *= 2
planets

Output: ['mars', 'venus', 'earth', 'mars', 'venus', 'earth']
```
- ``index()`` method: can be passed a value, and if that value exists in th list, the index of the value is returned
    - when there are duplicates: the index of its first appearance is returned

```python
planets = ['mars', 'venus', 'earth']
planets.index('earth')

Output = 2
````
- ```append()```method: to add new values to a list
    - the argument will be added to the end of the list
- ```insert()``` method: to add new values to a list
    - the argumennt can be inserted at any index in the list

```python
planets = ['mars', 'venus', 'earth']
planets.append('jupiter')
planets

Output = ['mars', 'venus', 'earth', 'jupiter']

planets = ['mars', 'venus', 'earth']
planets.insert(2,'jupiter')
planets

Output = ['mars', 'venus', 'jupiter', 'earth']
````
- ```remove()```method: is passed to a value to be removed from the list
    - if the value appears multiple times in the list, only the first instance of value will be removed

```python
planets = ['mars', 'venus', 'earth', 'mars']
planets.remove('mars')
planets

Output = ['venus', 'earth', 'mars']
````
- ```sort()```method: to sort the list of number values or lists of string
    - pass *True* for the *reverse* keyword argument to sort the values in reverse order
    - you can't sort lists that have both number values and string values
    - sorting strings: uppercase letters come before lowercase letters
        - to sort the values in regualar alphabetical order, pass ```str.lower```for the keyword argument 

```python
planets = ['Mars', 'venus', 'earth', 'mars']
planets.sort()
planets

Output = ['Mars', 'earth', 'mars', 'venus']

planets = ['venus', 'earth', 'mars', 'jupiter']
planets.sort(reverse=True)
planets

Output = ['venus', 'mars', 'jupiter', 'earth']
````

# List-like types

- list value: *mutable*
- string value: *immutable*
- *tuple*:

    - typed with parantheses ()
    - immutable
    - are used to convey to anyone reading your code that you don’t intend for that sequence of values to change
- converting types with: ```list()```and ```tuple()```

## References
When you assign a list to a variable, you are actually assigning a list reference to the variable

- *reference* = value, that points to some bit of data
- *list reference* = value that points to a list

```python
spam = [0,1,2,3,4,5]
cheese = spam
````
--> in this case ```spam = cheese```copies the reference, not the list

Variables will contain references to list values rather than list values themselves. 

Module named *copy* provides the ```copy()```and ```deecopy()```functions
- ```copy.copy()```: make a duplicate copy of a mutable value (list/dictionary)
    - the second list can be modified independently of the first
- ```deepcopy()```: will copy these inner lists ass well

```python
import copy
planets = ['venus', 'earth', 'mars', 'jupiter']
universe = copy.copy(planets)
universe[2] = 'saturn'

universe 

Output = ['venus', 'earth', 'saturn', 'jupiter']
````

## Questions

1. What is []?

```[]``` represents a list with no elements in it.

2. How would you assign the value 'hello' as the third value in a list stored in a variable named spam? (Assume spam contains [2, 4, 6, 8, 10].)

spam[2] = 'hello'

For the following three questions, let’s say spam contains the list ['a', 'b','c', 'd'].


3. What does spam[int(int('3' * 2) // 11)] evaluate to?

The expression ```int('3' * 2)``` evaluates to 33, and then ```33 // 11``` evaluates to 3.
So, ```spam[3]``` evaluates to the element at index 3 in ```['a', 'b', 'c', 'd']```, which is 'd'.


4. What does spam[-1] evaluate to?

```spam[-1]``` returns the last element of the list, which is 'd'


5. What does spam[:2] evaluate to?

```spam[:2]``` returns a slice of the list from the start up to (but not including) index 2, which is ```['a', 'b']```.


For the following three questions, let’s say bacon contains the list [3.14,'cat', 11, 'cat', True].

6. What does bacon.index('cat') evaluate to?

```bacon.index('cat')``` returns the index of the first occurrence of 'cat' in the list [3.14, 'cat', 11, 'cat', True], which is at index 1.

7. What does bacon.append(99) make the list value in bacon look like?

[3.14,'cat', 11, 'cat', True, 99]


8. What does bacon.remove('cat') make the list value in bacon look like?

[3.14, 11, 'cat', True]


9. What are the operators for list concatenation and list replication?

- list concatenation: +
- list replication: *


10. What is the difference between the append() and insert() list methods?

- ```append()``` adds an element to the end of the list.
- ```insert()``` adds an element at a specific index in the list.

11. What are two ways to remove values from a list?

- ```remove()```method
- ```del```statement

The ```del``` statement is good to use when you know the index of the value you want to remove from the list. The ```remove()``` method is good when you know the value you want to remove from the list.


12. Name a few ways that list values are similar to string values.

Many of the things you can do with lists can also be done with strings: indexing; slicing; and using them with ```for``` loops, with ```len()```, and with the ```in``` and ```not in``` operators.



13. What is the difference between lists and tuples?

- lists are mutable (you can change, add, or remove items), while tuples are immutable (once defined, they cannot be modified).
- lists use square brackets [], whereas tuples use parentheses ().

14. How do you type the tuple value that has just the integer value 42 in it?

(42,)


15. How can you get the tuple form of a list value? How can you get the list form of a tuple value?

- to convert a list to a tuple: ```tuple(list_value)```
- to convert a tuple to a list: ```list(tuple_value)```

16. Variables that “contain” list values don’t actually contain lists directly. What do they contain instead?

references 

17. What is the difference between copy.copy() and copy.deepcopy()?

If the list you need to copy contains lists, then use the ```copy.deepcopy()``` function instead of ```copy.copy()```. The ```deepcopy()``` function will copy these inner lists as well.












