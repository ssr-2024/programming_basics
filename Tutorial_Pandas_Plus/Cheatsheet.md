# Cheatsheet for the Pandas Plus Tutorial

This file contains the solutions for both Tasks 

## Task 1
```py
# Loop through rows to find delimiters and titles
for i in range(len(df)):
    # Check for delimiter line
    if df.iloc[i].str.contains('___________________').any():
```

## Task 2
```py

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
```

