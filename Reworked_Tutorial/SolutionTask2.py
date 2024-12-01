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
keywords = ['UNSTANDARDIZED MEANS', 'STANDARDIZED MEANS']
output_file = "./split_sheets_output_empty_lines.xlsx"

# Find rows with exact matches for the keywords
keyword_rows = df[df.iloc[:, 0].isin(keywords)].index

# Find empty rows
empty_rows = df[df.isnull().all(axis=1)].index

# Process sections based on keyword positions and empty rows
with pd.ExcelWriter(output_file) as writer:
    for i, start in enumerate(keyword_rows):
        # Extract the row containing the keyword as the sheet name
        sheet_name = sanitize_sheet_name(df.iloc[start, 0])
        
        # Determine the range of the current section
        # Find the next empty row after the keyword
        end_candidates = empty_rows[empty_rows > start]
        end = end_candidates.min() if not end_candidates.empty else len(df)
        
        # Extract the section starting one row after the keyword
        section = df.iloc[start + 1:end].reset_index(drop=True)
        
        # Write the section to an Excel sheet
        section.to_excel(writer, sheet_name=sheet_name, index=False, header=False)

print(f"Data has been split and saved to {output_file}")