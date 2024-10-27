import pandas as pd

# Load the Excel sheet
file_path = 'Final_Project/organized_tables.xlsx'
df = pd.read_excel(file_path, sheet_name='CLUSTER STATISTICS FOR 5', header=None)

# Function to find the start of a section by a keyword (exact match)
def find_section_start_exact(keyword):
    matches = df[df[0].str.strip() == keyword].index
    if len(matches) > 0:
        return matches[0] + 1  # Return the row after the match
    else:
        print(f"Warning: '{keyword}' not found in the file.")
        return None

# Function to find the start of a section by a keyword (partial match)
def find_section_start_partial(keyword):
    matches = df[df[0].str.contains(keyword, case=False, na=False)].index
    if len(matches) > 0:
        return matches[0] + 1  # Return the row after the match
    else:
        print(f"Warning: '{keyword}' not found in the file.")
        return None

# Identify the start rows for each section based on keywords
unstandardized_start = find_section_start_exact("UNSTANDARDIZED MEANS")
standardized_start = find_section_start_exact("STANDARDIZED MEANS")
pattern_start = find_section_start_partial("PATTERN OF STANDARDIZED MEANS")

# Check if the section starts are found, otherwise skip extraction
if unstandardized_start is not None and standardized_start is not None and pattern_start is not None:
    
    # Extract Unstandardized Means
    unstandardized_header = unstandardized_start
    unstandardized_means = df.iloc[unstandardized_header + 1:standardized_start - 1].reset_index(drop=True)
    unstandardized_means.columns = df.iloc[unstandardized_header]
    unstandardized_means.set_index(unstandardized_means.columns[0], inplace=True)
    print("Unstandardized Means Columns:", unstandardized_means.columns)
    print("Unstandardized Means Data:\n", unstandardized_means.head())
    
    # Extract Standardized Means
    standardized_header = standardized_start
    standardized_means = df.iloc[standardized_header + 1:pattern_start - 1].reset_index(drop=True)
    standardized_means.columns = df.iloc[standardized_header]
    standardized_means.set_index(standardized_means.columns[0], inplace=True)
    print("Standardized Means Columns:", standardized_means.columns)
    print("Standardized Means Data:\n", standardized_means.head())
    
    # Extract Pattern of Standardized Means
    pattern_header = pattern_start
    pattern_means = df.iloc[pattern_header + 1:].reset_index(drop=True)
    pattern_means.columns = df.iloc[pattern_header]
    pattern_means.set_index(pattern_means.columns[0], inplace=True)
    print("Pattern of Standardized Means Columns:", pattern_means.columns)
    print("Pattern of Standardized Means Data:\n", pattern_means.head())

    # Save the extracted data to new sheets in the same Excel file
    with pd.ExcelWriter(file_path, mode='a', if_sheet_exists='replace') as writer:
        unstandardized_means.to_excel(writer, sheet_name='Unstandardized Means', index=True)
        standardized_means.to_excel(writer, sheet_name='Standardized Means', index=True)
        pattern_means.to_excel(writer, sheet_name='Pattern of Standardized Means', index=True)

# Extract the five tables at the beginning of the first sheet
def extract_initial_tables(df):
    tables = {}
    current_table = []
    current_title = None

    for i in range(len(df)):
        row = df.iloc[i]
        if pd.isna(row[0]):
            continue
        if row[0].startswith('CLUSTER'):
            if current_title is not None:
                tables[current_title] = pd.DataFrame(current_table)
            current_title = row[0]
            current_table = [row]
        else:
            current_table.append(row)

    if current_title is not None:
        tables[current_title] = pd.DataFrame(current_table)

    return tables

initial_tables = extract_initial_tables(df)

# Save the initial tables to new sheets in the same Excel file
with pd.ExcelWriter(file_path, mode='a', if_sheet_exists='replace') as writer:
    for title, table in initial_tables.items():
        title = ' '.join(str(title).split()[:2])  # Shorten the title to the first two words
        title = sanitize_sheet_name(title)  # Sanitize the title
        table.to_excel(writer, sheet_name=title, index=False)