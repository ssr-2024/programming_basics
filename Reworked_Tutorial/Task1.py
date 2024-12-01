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