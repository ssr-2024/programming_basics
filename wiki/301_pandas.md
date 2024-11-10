# Pandas

Pandas is useful for handling and analyzing structured data. The name “Pandas” is derived from “Panel Data".

## DataFrame

In Pandas, a **DataFrame** is the primary data structure used to store data in a tabular format with labeled rows and columns, similar to an Excel spreadsheet. It allows for efficient data manipulation and analysis, including filtering, grouping, and joining.

### Creating a DataFrame

A DataFrame can be created in several ways, including from lists, dictionaries, or external files like CSVs and Excel sheets. 

Here’s an example of creating a DataFrame from a dictionary:

```python
import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [24, 27, 22],
    'City': ['New York', 'Los Angeles', 'Chicago']
}

df = pd.DataFrame(data)
print(df)
```
And here is an example of reading data from a CSV file:

import pandas as pd

```python
import pandas as pd

# Reading CSV data 
df = pd.read_csv("example.csv",
    sep=',', # Specifies that data is comma-separated
    header=2,# Skips the first two lines, assuming they are not data
    nrows=5, # Limits to reading only the first 5 rows
    usecols=[0, 2, 4], # Selects only columns 0, 2, and 4
    na_values=['N/A', '0'], # Treats 'N/A' and '0' as missing values (NaN)
).dropna(axis=0, how='any') # Drops rows with any NaN values

print(df)
```

### Index and Columns

- **Index**: Indexes are labels used to refer to your data. These labels are usually your column headers.
- **Columns**: Each column in a DataFrame has a label, making it easy to access specific data fields.


### Selecting Columns

```py
# 1. Create a list of columns to be selected
columns_to_be_selected = ["Player", "Team", "Goals"]

# 2. Use it as an index to the DataFrame
df[columns_to_be_selected]

# 3. Using loc method
df.loc[columns_to_be_selected]
```
### Selecting Rows

Unlike the columns, our current DataFrame does not have a label which we can use to refer the row data. But like arrays, DataFrame provides numerical indexing `(0, 1, 2…)` by default.

```py
# 1. using numerical indexes as with numpy - iloc
df.iloc[0:3, :]

# 2. using labels as index - loc
row_index_to_select = [0, 1, 4, 5]
df.loc[row_index_to_select]
```

You can also modify existing data or add new columns:

```python
# Adding a new column
df['Salary'] = [70000, 80000, 60000]
```

## Group By

The **groupby** function is used to group data based on specific columns, enabling you to perform aggregate operations, like sum, mean, or count, on each group.

```python
# Group by 'City' and calculate the average salary
df.groupby('City')['Salary'].mean()
```

## Pivot

A **pivot table** reshapes data by summarizing it based on specific columns, displaying data in a more organized, multi-dimensional table format. This is especially helpful for summarizing large datasets with complex structures.

```python
# Creating a pivot table
df.pivot_table(index='City', columns='Age', values='Salary', aggfunc='sum')
```

## Transpose

Transpose a DataFrame to swap rows and columns, providing a different view of the data. 

```python
# Transpose the DataFrame
df = pd.DataFrame(data).transpose()
```

## Importing Data

Pandas makes it easy to import data from different sources, including CSV, Excel, and SQL. Here’s an example of how to load data from various sources into a DataFrame:

### From a CSV File

```python
df = pd.read_csv('path_to_file.csv')
```

### Handling Missing Values

When importing data, there may be missing or unknown values. Pandas represents these as `NaN` (Not a Number) by default. You can handle them using functions like `fillna()` to replace them or `dropna()` to remove rows/columns with missing data.

```python
# Fill missing values
df.fillna(0, inplace=True)

# Drop rows with missing values
df.dropna(inplace=True)
```

## Exporting Data

After working with a DataFrame, you may want to save or export it to various formats, such as CSV or Excel.

```python
# Export to CSV
df.to_csv('exported_file.csv')

# Export to Excel
df.to_excel('exported_file.xlsx')
```


