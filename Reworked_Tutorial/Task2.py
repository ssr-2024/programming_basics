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