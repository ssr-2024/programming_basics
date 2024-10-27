import pandas as pd
import re

# Function to sanitize sheet names because Excel sheet names have restrictions like no special characters
def sanitize_sheet_name(name):
    # Remove invalid characters
    return re.sub(r'[\\/*?:\[\]]', '', name)

# Load the entire sheet
file_path = '/Users/eliaskehrli/Library/Mobile Documents/com~apple~CloudDocs/Uni/Master/Sport/SSR Basismodul/programming_basics/Final_Project/testdata.xlsx'
df = pd.read_excel(file_path, header=None)  # Load without headers for flexibility

# Initialize variables to track table start and table names
table_start = 0
tables = {}
title = None

# Loop through rows to find delimiters and titles
for i in range(len(df)):
    # Check for delimiter line
    if df.iloc[i].str.contains('___________________').any():
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

# Save each table to a separate sheet in a new Excel file
with pd.ExcelWriter('Final_Project/organized_tables.xlsx') as writer:
    for title, table in tables.items():
        table.to_excel(writer, sheet_name=title, index=False)
