# NumPy
Numpy is the most basic and a powerful package for working with data in python.

At the core, numpy provides the excellent ndarray objects, short for n-dimensional arrays.

In a ‘ndarray’ object, aka ‘array’, you can store multiple items of the same data type. It is the facilities around the array object that makes numpy so convenient for performing math and data manipulations.

## Advantages of using numpy arrays overs lists

The key difference between an array and a list is, arrays are designed to handle vectorized operations while a python list is not. That means, if you apply a function it is performed on every item in the array, rather than on the whole array object.

Another characteristic is that, once a numpy array is created, you cannot increase its size.

A numpy array must have all items to be of the same data type, unlike lists. This is another significant difference.

To summarise, the main differences with python lists are:
- Arrays support vectorised operations, while lists don’t.
- Once an array is created, you cannot change its size. You will have to create a new array or overwrite the existing one.
- Every array has one and only one dtype. All items in it should be of that dtype.
- An equivalent numpy array occupies much less space than a python list of lists.

## Installing NumPy

To install NumPy, use pip:

```python
pip install numpy
```

## How to create a numpy array

**First**: import NumPy

```python
import numpy as np
````

**Second**: using the ```np.array()``` function
### Creating an 1d array from a list

```python
list = [0,1,2,3]
arr1d = np.array(list)

Output: array([0, 1, 2, 3])
````
### Creating an 2d array from a list

You may also specify the datatype by setting the dtype argument 
```python
list = [[0,1,2,3], [10,11,12,13], [20,21,22,23]]
arr2d = np.array(list, dtype = 'float')

Output: array([[ 0.,  1.,  2.,  3.],
       [10., 11., 12., 13.],
       [20., 21., 22., 23.]])
````
The decimal point after each number is indicative of the float datatype.

### Creating an array filled with a specific value

4x3 array filled with 5

```python
array = np.full((4, 3), 5)

Output: array([[5, 5, 5],
       [5, 5, 5],
       [5, 5, 5],
       [5, 5, 5]])
```

### Creating an array with a sequence of numbers

```python
array = np.arange(0,10,2) #Numbers from 0 to 9 with a step of 2

Output: array([0, 2, 4, 6, 8])
```

## Reshaping arrays

NumPy allows arrays to be reshaped, changing their dimensions without changing the underlying data. The ```reshape()``` function changes the array of numbers into a n x d array.

```python
array = np.arange(12).reshape(3, 4)

Output: array([[ 0,  1,  2,  3],
       [ 4,  5,  6,  7],
       [ 8,  9, 10, 11]])
```

## Inspect the size and shape of a numpy array

If you want to know:

- If it is a 1D or a 2D array or more: use ```ndim```
- How many items are present in each dimension: use ```shape```
- What is its datatype: use ```dtype```
- What is the total number of items in it: use ```size```


## Extract specific items from an array
You can extract specific portions on an array using indexing starting with 0, something similar to how you would do with python lists.

But unlike lists, numpy arrays can optionally accept as many parameters in the square brackets as there is number of dimensions.

### 1d array

```python
array = np.array([10, 20, 30, 40])
print(array[-2])

Output: 30
```

### 2d array
For two-dimensional arrays, you use double indexing:
```python
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(matrix[0, 0])  

Output: 1 (first element in the first row)

print(matrix[1, 2])  

Output: 6 (third element in the second row)
```

### Boolean indexing

A boolean index array is of the same shape as the array-to-be-filtered and it contains only True and False values. The values corresponding to True positions are retained in the output.

```python
array = np.array([10, 20, 30, 40])
secondarray = array > 20
secondarray

Output: array([False, False,  True,  True])
```

## Stacking arrays

The ```numpy.stack()``` function joins a sequence of arrays along a new axis. All arrays must have the same shape.

```python

a = np.array([1, 2])
b = np.array([3, 4])

c = np.stack((a, b))
print(c)

Output: [[1 2]
 [3 4]]
```

Besides the ```stack()``` function, NumPy also has ```vstack()``` function that joins two or more arrays vertically and ```hstack()``` function that joins two or more arrays horizontally.




## Calculating with arrays

### Adding a number to every item in the list:

```python
list = [0,1,2,3]
arr1d = np.array(list)
arr1d + 2

Output: array([2, 3, 4, 5])
````
### Mean, minimum, maximum: 
```python

array = np.array([0,1,2,3,4,5])
print (array.mean())

Output: 2.5

print (array.min())

Output: 0

print (array.max())

Output: 5
````
However, if you want to compute the minimum values row wise or column wise, use the ```np.amin``` version instead.

```python
list = [[1, 2, 3, 4],[3, -1, 5, 6], [5, 6, 7, -5]]
array = np.array(list, dtype = 'float')
print(np.amin(array, axis=0)) #column wise minimum

Output: [ 1. -1.  3. -5.]

print(np.amin(array, axis=1)) #row wise minimum

Output: [ 1. -1. -5.]
````




## Represent missing values

Missing values can be represented using ```np.nan``` object

```python
list = [[1, 2, 3, 4],[3, 4, 5, 6], [5, 6, 7, 8]]
array = np.array(list, dtype = 'float')
array [:2, :2] = np.nan
array

Output: array([[nan, nan,  3.,  4.],
       [nan, nan,  5.,  6.],
       [ 5.,  6.,  7.,  8.]])

