# Table of Contents
- [Table of Contents](#table-of-contents)
- [Introduction](#introduction)
- [Help](#help)
- [**Key Functions in the Code**](#key-functions-in-the-code)
- [Task 1 "Using Delimiters"](#task-1-using-delimiters)
- [Task 2 "Using Keywords"](#task-2-using-keywords)

# Introduction
Hello, dear friend!

In this tutorial, you will learn how to organize and clean a messy Excel file using Python's powerful **pandas** library. In real-world scenarios, data files are seldom perfectly formatted. You may frequently encounter Excel sheets where all the data is contained in a single, disorganized sheet..

To work effectively with data visualization libraries such as **Plotly** or **Openpyxl**, it is essential to have a well-structured Excel sheet. This involves having a clear header row, an index column, and consistently formatted data throughout the file. A clean and organized dataset not only simplifies the process of visualizing data but also improves the accuracy and efficiency of your analysis.

By the end of this tutorial, you will have the skills to transform messy, complex spreadsheets into clean, organized datasets that are ready for analysis using two different methods. Let’s get started and make data cleaning easy!

# Help
If you find yourself stuck at any point, feel free to consult the two files 'SolutionTask1.py' and 'SolutionTask2.py' containing the solutions.


# **Key Functions in the Code**
To assist you with the following tasks, I will provide a few key functions that you will need to utilize. The tasks can be found in the section below this one.

Examples and explanations are from the [Pandas documentation](https://pandas.pydata.org/docs/index.html).

---

## **1. Reading Excel Files**

Use `pd.read_excel()` to load data from an Excel file into a Pandas DataFrame.

### Example:
```python
import pandas as pd

# Define the file path
file_path = "your_file.xlsx"

# Load the Excel file into a DataFrame
data = pd.read_excel(file_path)

# Inspect the first few rows of the data
print(data.head())
```

### Key Points:
- **Purpose**: Load data and inspect its structure.
- **Parameters**:
  - `file_path`: Path to the Excel file.
  - `header=None`: If specified, treats all rows as data without assigning column names.
  
[Read More: pd.read_excel](https://pandas.pydata.org/docs/reference/api/pandas.read_excel.html)

---

## **2. Filtering Data with `str.contains`**

The `.str.contains()` function filters rows based on patterns in a text column.

### Example:
```python
# Example DataFrame
df = pd.DataFrame({"Name": ["John Doe", "Jane Smith", "John Smith"], "Age": [25, 30, 35]})

# Filter rows where 'Name' contains the text 'John'
filtered = df[df["Name"].str.contains("John")]
print(filtered)
```

### Output:
```
         Name  Age
0  John Doe   25
2  John Smith  35
```

### Key Points:
- **Purpose**: Identify rows containing specific patterns.
- **Parameter**:
  - `na=False`: Ensures rows with `NaN` values are excluded from filtering.

---

## **3. Identifying Delimiters Dynamically**

Use `.str.contains()` to locate rows with specific patterns.

### Example:
```python
# Create example data
df = pd.DataFrame({
    "A": ["Header", "___________________", "Data1", "Data2", "___________________", "Data3"],
    "B": [1, None, 2, 3, None, 4]
})

# Find rows containing the delimiter
delimiter_rows = df[df["A"].str.contains("___________________", na=False)].index
print(delimiter_rows)
```

### Output:
```
Int64Index([1, 4], dtype='int64')
```

### Key Points:
- **Purpose**: Identify section boundaries dynamically by matching text patterns.

---

## **4. Slicing Data with `iloc`**

The `.iloc` function is used for slicing data by row and column indices.

### Example:
```python
# Example DataFrame
df = pd.DataFrame({"A": ["Header1", "Data1", "Data2", "Header2", "Data3", "Data4"]})

# Slice rows 1–3
section1 = df.iloc[1:3]
print(section1)
```

### Output:
```
        A
1  Data1
2  Data2
```

### Key Points:
- **Purpose**: Extract subsets of rows and columns based on index positions.
- **Syntax**:
  - `start:end`: Includes rows from `start` up to but not including `end`.

---

## **5. Resetting Indices**

Use `reset_index()` to reset the row indices of a DataFrame for cleaner output.

### Example:
```python
# Example DataFrame
df = pd.DataFrame({"A": [10, 20, 30]}, index=[2, 4, 6])

# Reset index
df_reset = df.reset_index(drop=True)
print(df_reset)
```

### Output:
```
    A
0  10
1  20
2  30
```

### Key Points:
- **Purpose**: Remove the old index and create a new, sequential one.
- **Parameter**:
  - `drop=True`: Ensures the old index is not added as a new column.

---

## **6. Writing to Excel**

Save data to an Excel file using `ExcelWriter` to create multiple sheets.

### Example:
```python
# Example DataFrames
df1 = pd.DataFrame({"A": [1, 2, 3]})
df2 = pd.DataFrame({"B": ["a", "b", "c"]})

# Save multiple DataFrames to an Excel file
with pd.ExcelWriter("output.xlsx") as writer:
    df1.to_excel(writer, sheet_name="Sheet1", index=False)
    df2.to_excel(writer, sheet_name="Sheet2", index=False)
```

### Key Points:
- **Purpose**: Write data into an Excel file with multiple sheets.
- **Syntax**:
  - `to_excel`: Saves the DataFrame to a specified sheet.

---

## **7. Identifying Empty Rows with `isnull()`**

The `isnull()` function identifies missing values in a DataFrame.

### Example:
```python
# Example DataFrame
df = pd.DataFrame({
    "A": [1, 2, None, 4],
    "B": [None, 2, 3, None]
})

# Check for missing values
print(df.isnull())
```

### Output:
```
       A      B
0  False   True
1  False  False
2   True  False
3  False   True
```

---

## **8. Identifying Completely Empty Rows**

Use `isnull().all(axis=1)` to check if all values in a row are `NaN`.

### Example:
```python
# Identify rows where all elements are NaN
empty_rows = df.isnull().all(axis=1)
print(empty_rows)
```

### Output:
```
0    False
1    False
2    False
3    False
dtype: bool
```

---

## **9. Extracting Empty Row Indices**

The `.index` property retrieves the indices of rows meeting a condition.

### Example:
```python
# Get the indices of completely empty rows
empty_row_indices = df[df.isnull().all(axis=1)].index
print(empty_row_indices)
```

### Output:
```
Int64Index([], dtype='int64')
```

---

## **10. Using `.isin()`**

The `.isin()` function checks if elements match a list of specific values.

### Example:
```python
# Example DataFrame
df = pd.DataFrame({
    "A": ["apple", "banana", "cherry", "date"],
    "B": [1, 2, 3, 4]
})

# Check if values in column 'A' are in a list of keywords
keywords = ["apple", "cherry"]
matches = df["A"].isin(keywords)
print(matches)
```

### Output:
```
0     True
1    False
2     True
3    False
Name: A, dtype: bool
```

---

## **11. Finding the Minimum Value with `.min()`**

The `.min()` function retrieves the smallest value in a Series or column.

### Example:
```python
# Example Series
values = pd.Series([5, 10, 15])

# Find the smallest value
smallest = values.min()
print(smallest)
```

### Output:
```
5
```

---

## **12. Filtering Empty Rows After a Specific Index**

Filter empty rows that occur after a given index.

### Example:
```python
# Example Series of empty row indices
empty_row_indices = pd.Series([5, 10, 15])

# Filter indices greater than a specific value
start = 8
filtered_indices = empty_row_indices[empty_row_indices > start]
print(filtered_indices)
```

### Output:
```
1    10
2    15
dtype: int64
```

---
## Sanatizing sheet names
Before I let you begin with the two tasks, I would like to introduce you to a little standard module called 're.' 

Excel can be tricky to work with because it does not allow special characters in sheet names. To address this issue, I have included a function that will help you avoid any problems related to this. 

I hope you find it useful. Now, go have fun with the exercises!
# Task 1 "Using Delimiters"
The Excel file named "messyfile.py" serves as an example of a potential export from a software program called RopStat, which is used for cluster analysis. Like many other programs, RopStat sometimes utilizes delimiters in its output.

Delimiters, such as lines of dashes (------------------), act as visual or programmatic markers to separate sections of data within a file. They are commonly found in messy datasets to indicate boundaries between distinct segments, such as different tables or categories.

You need to complete the script for Task 1 (which you can copy and paste into a new file) to create a Python script that organizes the "messyfile.py."
```py
import pandas as pd
import re

# Function to sanitize sheet names due to Excel restrictions
def sanitize_sheet_name(name):
    """
    Sanitizes the sheet name by:
    - Removing invalid characters: \, /, *, ?, :, [, ]
    - Limiting the name to 31 characters (Excel's limit).
    """
    return re.sub(r'[\\/*?:\[\]]', '', str(name))[:31]

# Step 1: Load the Excel file
file_path = "path_to_messyfile.xlsx"  
df = df = pd.read_excel(file_path, header=None)

# Step 2: Define the delimiter and output file
delimiter = ""
output_file = ""

# Step 3: Find rows with the delimiter
# TODO: Identify rows where the first column contains the delimiter
delimiter_rows = None  # Hint: Use .iloc and .str.contains()

# Step 4: Process sections based on delimiter positions
# TODO: Open a pd.ExcelWriter context to write structured data to a new file
with pd.ExcelWriter(output_file) as writer:
    for i, start in enumerate(delimiter_rows):

        # TODO: Extract the row below the delimiter as the sheet name
        if start + 1 < len(df):
            sheet_name = None  # Replace with sanitize_sheet_name and df.iloc

        else:
            sheet_name = f"Sheet_{i}"  # Fallback name if no valid row exists

        # TODO: Determine the range of the current section (start and end rows)
        end = None  # Replace with logic to find the next delimiter or the end of the file

        # TODO: Extract the section starting two rows after the delimiter
        section = None  # Use .iloc[start:end] and .reset_index(drop=True)

        # The following line writes the section to an Excel sheet
        section.to_excel(writer, sheet_name=sheet_name, index=False, header=False) 
        
        
# Print confirmation
print(f"Data has been split and saved to {output_file}")
```
---

# Task 2 "Using Keywords"
Delimiters are not always guaranteed, so sometimes you need to approach the problem creatively. One option is to use keywords. 

In the `messyfile.py`, there are two tables that hold particular significance: "STANDARDIZED MEANS" and "UNSTANDARDIZED MEANS." 

Your task is to extract these tables into new sheets. To accomplish this, you need to complete the following code
```py
import pandas as pd
import re

# Function to sanitize sheet names due to Excel restrictions
def sanitize_sheet_name(name):
    """
    Sanitizes the sheet name by:
    - Removing invalid characters: \, /, *, ?, :, [, ]
    - Limiting the name to 31 characters (Excel's limit).
    """
    return re.sub(r'[\\/*?:\[\]]', '', str(name))[:31]

# Step 1: Load the Excel file
file_path = "path_to_messyfile.xlsx"  
df = df = pd.read_excel(file_path, header=None)

# Step 2: Define keywords and initialize the output file
keywords = ['UNSTANDARDIZED MEANS', 'STANDARDIZED MEANS']
output_file = "./split_sheets_output_empty_lines.xlsx"

# Step 3: Find rows with exact matches for the keywords
# TODO: Use df.iloc[:, 0] and .isin(keywords) to find rows matching the keywords
keyword_rows = None  

# Step 4: Identify completely empty rows
# TODO: Use df.isnull() and .all(axis=1) to find rows where all elements are NaN
empty_rows = None  

# Step 5: Process sections based on keyword positions and empty rows
with pd.ExcelWriter(output_file) as writer:
    for i, start in enumerate(keyword_rows):
        # Step 5.1: Extract the row containing the keyword as the sheet name
        sheet_name = sanitize_sheet_name(df.iloc[start, 0])  # No changes here

        # Step 5.2: Determine the range of the current section
        # TODO: Find the next empty row after the keyword to set the section end
        end_candidates = None  # Use empty_rows[empty_rows > start]
        end = None  # Use .min() to find the smallest index or set to len(df) if empty

        # The section starting one row after the keyword
        section = df.iloc[start + 1:end].reset_index(drop=True)
        
        # The section to an Excel sheet
        section.to_excel(writer, sheet_name=sheet_name, index=False, header=False)


print(f"Data has been split and saved to {output_file}")
```

