# Chapter 1

## Tables of content
- [Chapter 1](#chapter-1)
  - [Tables of content](#tables-of-content)
    - [Introduction to Python](#introduction-to-python)
    - [Expressions and Data Types](#expressions-and-data-types)
    - [String Concatenation and Replication](#string-concatenation-and-replication)
    - [Variables](#variables)
    - [Writing Your First Program](#writing-your-first-program)
    - [Functions](#functions)
    - [Summary](#summary)
    - [Questions](#questions)
      - [Q1: Which of the following are operators, and which are values?](#q1-which-of-the-following-are-operators-and-which-are-values)
      - [Q2: Which of the following is a variable, and which is a string?](#q2-which-of-the-following-is-a-variable-and-which-is-a-string)
      - [Q3: Name three data types.](#q3-name-three-data-types)
      - [Q4: What is an expression made up of? What do all expressions do?](#q4-what-is-an-expression-made-up-of-what-do-all-expressions-do)
      - [Q5: This chapter introduced assignment statements, like `spam = 10`. What is the difference between an expression and a statement?](#q5-this-chapter-introduced-assignment-statements-like-spam--10-what-is-the-difference-between-an-expression-and-a-statement)
      - [Q6: What does the variable `bacon` contain after the following code runs?](#q6-what-does-the-variable-bacon-contain-after-the-following-code-runs)
      - [Q7: What should the following two expressions evaluate to?](#q7-what-should-the-following-two-expressions-evaluate-to)
      - [Q8: Why is `eggs` a valid variable name while `100` is invalid?](#q8-why-is-eggs-a-valid-variable-name-while-100-is-invalid)
      - [Q9: What three functions can be used to get the integer, floating-point number, or string version of a value?](#q9-what-three-functions-can-be-used-to-get-the-integer-floating-point-number-or-string-version-of-a-value)
      - [Q10: Why does this expression cause an error? How can you fix it?](#q10-why-does-this-expression-cause-an-error-how-can-you-fix-it)

### Introduction to Python

Chapter 1 introduces the fundamental concepts of programming with Python, starting with the interactive shell. The interactive shell allows users to execute Python statements one at a time and immediately see the results, which makes it an ideal tool for getting acquainted with Python basics.

### Expressions and Data Types

An **expression** is the simplest type of programming instruction in Python. It consists of **values** (such as numbers or text) and **operators** (like `+` or `-`) and can be **evaluated** to produce a single value.

Python supports several essential **data types**, which are categories for values:

* **Integer (int):** Whole numbers, such as `-2`, `0`, `10`
* **Floating-point number (float):** Numbers with decimal points, like `3.14`, `-0.5`
* **String (str):** Text values enclosed in single or double quotes, such as `'Hello'` or `"World"`

### String Concatenation and Replication

The `+` operator can be used to **concatenate** two strings, combining them into a new string. The `*` operator can **replicate** a string by copying it multiple times in sequence.

### Variables

A **variable** is like a labeled box in the computer’s memory that can store a single value. A variable is **assigned** a value using an **assignment statement**, which consists of the variable name, the equals sign (`=`), and the value to store.

Variable names must follow certain rules:

* They must be one word (no spaces).
* They can contain letters, numbers, and the underscore (`_`).
* They cannot start with a number.

### Writing Your First Program

Chapter 1 also covers writing and executing Python programs in IDLE’s file editor. It introduces a simple "Hello, World" program that uses the `print()` and `input()` functions to display text and receive user input.

### Functions

In addition to `print()` and `input()`, other essential functions introduced include:

* `len()`: Returns the length of a string.
* `str()`: Converts a value to a string.
* `int()`: Converts a value to an integer.
* `float()`: Converts a value to a floating-point number.

### Summary

Chapter 1 lays the groundwork for programming with Python by introducing core concepts like expressions, data types, variables, and functions. This foundational knowledge enables users to start writing simple programs that process text and interact with users. The chapter also includes exercises to help reinforce understanding of the concepts covered.

### Questions

#### Q1: Which of the following are operators, and which are values?

- **Operators**: `*`, `-`, `/`, `+`
- **Values**: `'hello'`, `-88.8`, `5`

Operators perform operations on values or variables, while values represent data.

---

#### Q2: Which of the following is a variable, and which is a string?

- **Variable**: `spam`
- **String**: `'spam'`

In Python, a variable is a name for storing values, while a string is a data type for text values, typically enclosed in quotes.

---

#### Q3: Name three data types.

1. Integer (`int`): Whole numbers like `42`
2. Floating-point number (`float`): Decimal numbers like `3.14`
3. String (`str`): Text data, such as `"hello"`

---

#### Q4: What is an expression made up of? What do all expressions do?

An **expression** consists of **values** and **operators**. It evaluates to a single value. For example, `2 + 3` is an expression that evaluates to `5`.

---

#### Q5: This chapter introduced assignment statements, like `spam = 10`. What is the difference between an expression and a statement?

An **expression** evaluates to a value, while a **statement** performs an action, such as assigning a value to a variable. For instance, `spam = 10` is a statement that assigns the value `10` to `spam`.

---

#### Q6: What does the variable `bacon` contain after the following code runs?

```python
bacon = 20
bacon + 1
```

The variable `bacon` will still contain `20` because `bacon + 1` evaluates to `21` but does not reassign it to `bacon`. To update `bacon`, you would need to write `bacon = bacon + 1`.

---

#### Q7: What should the following two expressions evaluate to?

```python
'spam' + 'spamspam'
```

- Evaluates to `'spamspamspam'` by concatenating the strings.

```python
'spam' * 3
```

- Also evaluates to `'spamspamspam'` by replicating the string three times.

---

#### Q8: Why is `eggs` a valid variable name while `100` is invalid?

`eggs` is valid because variable names can include letters, numbers, and underscores but cannot start with a number. `100` is invalid as a variable name because it starts with a digit.

---

#### Q9: What three functions can be used to get the integer, floating-point number, or string version of a value?

1. `int()` – Converts a value to an integer.
2. `float()` – Converts a value to a floating-point number.
3. `str()` – Converts a value to a string.

---

#### Q10: Why does this expression cause an error? How can you fix it?

```python
'I have eaten ' + 99 + ' burritos.'
```

This expression causes an error because `99` is an integer, and Python cannot concatenate strings with integers directly. To fix it, convert `99` to a string using `str()`:

```python
'I have eaten ' + str(99) + ' burritos.'
```

This will produce: `'I have eaten 99 burritos.'`