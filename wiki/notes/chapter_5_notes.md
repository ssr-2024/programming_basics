# Dictionaries

- collections of many values
- *keys*: indexes for dictionaries
- typed with **braces {}**

Dictionaries are useful for associating keys with values.

```python
myCat = {'size': 'fat', 'color': 'orange', 'disposition': 'shy'}

'My cat has' + myCat['color'] + ' fur.'

Output: 'My cat has orange fur.'
````
- keys: size, color, disposition
- values for the keys: fat, orange, shy

### Dictionaries versus Lists

- items in dictionaries are unordered
    - this means that dictionaries can't be scliced like lists

- three dictionary methods that will return list-like values of the dictionary's keys, values or both keys and values:
    - ```keys()```
    - ```values()```
    - ```items()```

```python
myCat = {'size': 'fat', 'color': 'orange', 'disposition': 'shy'}
for v in myCat.values():
    print (v)

Output:

fat
orange
shy
```

## Other Functions

- ```in```and ```not in```: to check whether a key or value exists in a dictionary
```python
myCat = {'size': 'fat', 'color': 'orange', 'disposition': 'shy'}
'weight' in myCat.keys()

Output: False
```
- ```get()```method: to check whether a key exists in a dictionary before accessing that key’s value
    - two arguments: the key of the value to retrieve and a fallback value to return if that key does not exist

```python
picnicItems = {'bread': 1, 'eggs': 4, 'ham': 2}

'I am bringing ' + str(picnicItems.get('eggs', 0)) + ' eggs.'

Output: 'I am bringing 4 eggs.'
```
- ```setdefault()```method: to set a value in a dictionary for a certain key only if that key does not already have a value.
    - two arguments: the first argument passed to the method is the key to check for, and the second argument is the value to set at that key if the key does not exist

```python
picnicItems = {'bread': 1, 'eggs': 4, 'ham': 2}
picnicItems.setdefault('apples', 4)

Output: 4

picnicItems

Output: {'bread': 1, 'eggs': 4, 'ham': 2, 'apples': 4}
````

- *pprint* module: with that you have access to the ```pprint()``` and ```pformat()``` functions that will “pretty print” a dictionary’s value

```python
import pprint
message = 'Let us see what happens!' 
count = {}

for character in message:     
    count.setdefault(character, 0)     
    count[character] = count[character] + 1

pprint.pprint(count)

Output: 
{' ': 4,
 '!': 1,
 'L': 1,
 'a': 2,
 'e': 4,
 'h': 2,
 'n': 1,
 'p': 2,
 's': 3,
 't': 2,
 'u': 1,
 'w': 1}
 ```

## Questions

1. What does the code for an empty dictionary look like?

{}

2. What does a dictionary value with a key 'foo' and a value 42 look like?

{'foo' : 42}

3. What is the main difference between a dictionary and a list?

- list: ordered collection of items that are accessed by index (e.g., list[0])
- dictionary: unordered collection of key-value pairs, where items are accessed by **key**

4. What happens if you try to access spam['foo'] if spam is {'bar': 100}?

You would get a KeyError because the key 'foo' does not exist in the dictionary spam.

5. If a dictionary is stored in spam, what is the difference between the
expressions 'cat' in spam and 'cat' in spam.keys()?

Both expressions will return True or False depending on whether 'cat' is a key in spam.

```'cat' in spam```is essentially a shorter version of writing ```'cat' in spam.keys()```

6. If a dictionary is stored in spam, what is the difference between the epressions 'cat' in spam and 'cat' in spam.values()?

- ```'cat' in spam```: Checks if 'cat' is a key in spam.
- ```'cat' in spam.values()```: Checks if 'cat' is a value in the dictionary spam.

7. What is a shortcut for the following code?

```python
if 'color' not in spam:
    spam['color'] = 'black'
```

```spam.setdefault('color', 'black')```

8. What module and function can be used to “pretty print” dictionary values?

- the *pprint* module
- the functions ```pprint.pprint()``` or ```pprint.format()```





