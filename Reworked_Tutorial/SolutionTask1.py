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

# Load the Excel file
file_path = "Final_Project/Tutorial_Pandas_Plus Kopie/1_messyfile.xlsx"
df = pd.read_excel(file_path, header=None)

# Initialize variables
delimiter = '___________________'
output_file = "./split_sheets_output.xlsx"

# Find rows with the delimiter
delimiter_rows = df[df.iloc[:, 0].str.contains(delimiter, na=False)].index

# Process sections based on delimiter positions
with pd.ExcelWriter(output_file) as writer:
    for i, start in enumerate(delimiter_rows):
        # Extract the row below the delimiter as the sheet name
        if start + 1 < len(df):
            sheet_name = sanitize_sheet_name(df.iloc[start + 1, 0])
        else:
            sheet_name = f"Sheet_{i}"  # Fallback sheet name if no valid row below delimiter
        
        # Determine the range of the current section
        end = delimiter_rows[i + 1] if i + 1 < len(delimiter_rows) else len(df)
        
        # Extract the section starting two rows after the delimiter
        section = df.iloc[start + 2:end].reset_index(drop=True)
        
        # Write the section to an Excel sheet
        section.to_excel(writer, sheet_name=sheet_name, index=False, header=False)

print(f"Data has been split and saved to {output_file}")