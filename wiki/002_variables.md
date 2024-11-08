# Variables

Variables are used to store and manipulate data values. Below is an overview of creating variables, naming rules and assigning values.

## Storing Values in Variables

To store a value, use an *assignment statement*, which includes:
- A variable name,
- An equal sign `=`,
- And the value to be stored.

Example:
```python
age = 30
```

Here, `age` is the variable that holds the integer value `30`.

### Overwriting Variables

Assigning a new value to an existing variable *overwrites* the old value:
```python
name = "Alice"
name = "Bob"  # "Alice" is forgotten, and name is now "Bob"
```

## Variable Naming Rules

Python variable names must follow these rules:

1. Must be a single word (no spaces).
2. Can contain letters, numbers, and underscores (`_`).
3. **Cannot** start with a number.
4. Are **case-sensitive** (`age` and `Age` are different).

| Variable Name | Validity | Explanation |
|---------------|----------|-------------|
| `name`        | Valid    | Follows all naming rules. |
| `_age`        | Valid    | Underscores are allowed. |
| `2nd_try`     | Invalid  | Starts with a number. |
| `my name`     | Invalid  | Contains a space. |
| `Name` and `name` | Both valid | Case-sensitive, so `Name` ≠ `name`. |

## Types of Variables

Python variables are *dynamically typed*, meaning the type can change as new values are assigned. The main types include:
- **Local Variables**: Defined within a function, accessible only inside that function.
- **Global Variables**: Defined outside any function, accessible throughout the program.






