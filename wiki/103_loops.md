# Loops

Loops allow for the repeated execution of code, enabling tasks to be automated and processed in sequences or until certain conditions are met. This concept is foundational in programming as it reduces redundancy and enables scalable logic in scripts and applications.

## `while` Loop

A `while` loop repeats as long as a specified condition is true. This kind of loop is useful when the number of iterations isn’t known in advance but depends on a condition.

![while diagram](<while diagram.png>)

### Example of a `while` Loop in Python

```python
count = 0
while count < 5:
    print("Count is:", count)
    count += 1
```

In this example, the `while` loop continues to print and increment `count` until `count` reaches 5.

### `break`

The `break` statement immediately exits a loop, even if the loop condition hasn’t been met.

```python
count = 0
while count < 10:
    print("Count is:", count)
    if count == 5:
        break  # Exit the loop when count is 5
    count += 1
```

### `continue`

The `continue` statement skips the current iteration and proceeds to the next iteration of the loop.

```python
count = 0
while count < 10:
    count += 1
    if count % 2 == 0:
        continue  # Skip even numbers
    print("Odd count:", count)
```

## `for` Loop

A `for` loop is especially useful when iterating over a collection or a range of values where the number of iterations is known or predictable. This loop is typically better suited than a `while` loop when you need to loop through items in a sequence or apply a specific, finite number of iterations.

### Example of a `for` Loop in Python

```python
# Using a `for` loop to iterate over a range of numbers
for i in range(5):
    print(i)
```

This example will print numbers from 0 to 4, as the `range(5)` function generates numbers from 0 up to (but not including) 5.

The `for` loop is often preferred over `while` when the number of iterations is known upfront or when looping through elements in a collection like a list, tuple, or dictionary.

For more informations about loops or more examples click on this link: [Chapter 2 - Flow Control](notes/chapter_2_notes.md#elements-of-flow-control)



