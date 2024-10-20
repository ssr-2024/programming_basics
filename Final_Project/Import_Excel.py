import pandas as pd
import os

# Define the absolute path to the Excel file
file_path = os.path.join('/Users/eliaskehrli/Library/Mobile Documents/com~apple~CloudDocs/Uni/Master/Sport/SSR Basismodul/programming_basics/Final_Project/testdata.xlsx')

# Read the entire Excel file without specifying the header
data = pd.read_excel(file_path, sheet_name='ropi_akt', header=None)

# Extract the header row (row 390)
header_row = data.iloc[391]

# Extract the table from rows 391 to 397 (inclusive)
start_idx = 392
end_idx = 397

# Extract the table and set the header
standardized_means_table = data.iloc[start_idx:end_idx + 1]
standardized_means_table.columns = header_row

# Display the extracted table
print("Standardized Means Table:")
print(standardized_means_table)