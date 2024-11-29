
'''
Welcome to your first task.
You have been provided with an almost finished code.
Your mission, should you choose to except it, is to 
complete the missing parts of the code. I have included
headers for each pre-provided section of the code so you understand, what is going on.
Good Luck!
This message will not self-destruct in 5 seconds
'''

import pandas as pd
import re

# Function of the "re" package, to sanitize sheet names because Excel sheet names have restrictions like no special characters
def sanitize_sheet_name(name):
    # re.sub() is used to replace all occurrences of certain patterns in a string.
    return re.sub(r'[\\/*?:\[\]]', '', name)

'''1. Provide the path to the excel file (messyfile.xlsx)'''
file_path = 'code/review_elias/messyfile.xlsx'
df = pd.read_excel(file_path, header=None)  # read the entire excel file into a dataframe and treat no row as a header

# Initialize variables to track table start and table names
table_start = 0
tables = {}
title = None

# 2. Loop through rows to find delimiters and titles'''
for i in range(len(df)):
    # 3. Check for delimiter line using the iloc function to access the row and the str.contains() function to check if the row contains the delimiter string.'''
    if df.iloc[i].str.contains('___________________________________').any():


    # From this point the code is again provided to you'''
         # If this is not the first table, save the previous table
        if title is not None:
            tables[title] = df.iloc[table_start:i]
        # Get the title from the next row as the sheet name
        title = df.iloc[i + 1, 0]
        title = ' '.join(str(title).split()[:4])  # Shorten the title to the first four words
        title = sanitize_sheet_name(title)  # Sanitize the title
        
        # Update table_start to the row after the current title row
        table_start = i + 2

# Handle the last table
if title is not None and table_start < len(df):
    tables[title] = df.iloc[table_start:]

# Save each table to a separate sheet in a new  Excel file
with pd.ExcelWriter('Step1.xlsx') as writer:
    for title, table in tables.items():
        table.to_excel(writer, sheet_name=title, index=False)

