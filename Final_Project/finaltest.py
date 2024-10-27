import pandas as pd
import re

# Function to sanitize sheet names because Excel sheet names have restrictions like no special characters
def sanitize_sheet_name(name):
    # Remove invalid characters
    return re.sub(r'[\\/*?:\[\]]', '', name)

# Load the Excel sheet
file_path = 'Final_Project/organized_tables.xlsx'  # Update with your actual file path
try:
    df = pd.read_excel(file_path, sheet_name=0, header=None)  # Load the first sheet
except Exception as e:
    print(f"Error loading Excel file: {e}")
    exit(1)

# Find rows where a new cluster starts (rows with "Cluster" followed by a number in the first column)
try:
    cluster_indices = df[df[0].str.match(r'^Cluster \d+', case=False, na=False)].index
    print(f"Found cluster indices: {cluster_indices}")  # Debug print
except Exception as e:
    print(f"Error finding cluster indices: {e}")
    exit(1)

# Dictionary to store each formatted cluster's data
clusters = {}

# Loop over each cluster start index to extract and reformat tables
for i, start_idx in enumerate(cluster_indices):
    # Define the end of the current table
    end_idx = cluster_indices[i + 1] if i + 1 < len(cluster_indices) else len(df)
    
    # Extract the title row (metadata) and parse it
    title_row = df.iloc[start_idx, 0]
    print(f"Processing title row: {title_row}")  # Debug print
    metadata_parts = title_row.split()  # Assumes metadata is space-separated
    print(f"Metadata parts: {metadata_parts}")  # Debug print
    
    # Check if metadata_parts has the expected number of elements
    if len(metadata_parts) < 2:
        print(f"Warning: Unexpected metadata format in row {start_idx}: {metadata_parts}")
        continue
    
    # Parse metadata (e.g., Cluster number, size, homogeneity coefficient)
    cluster_number = metadata_parts[1]  # Second word, e.g., "2" in "Cluster 2"
    
    # Extract size and homogeneity coefficient from the same row but later columns
    size_info = 'N/A'
    hc_info = 'N/A'
    
    # Loop through the columns to find size and HC information
    for col in df.iloc[start_idx]:
        if isinstance(col, str):
            if 'Size=' in col:
                size_info = col.split('=')[1]
            elif 'HC' in col:
                hc_info = col.split('=')[1].strip()
    
    # Extract the data table, skipping the title row and including the header row
    table_data = df.iloc[start_idx + 2:end_idx].reset_index(drop=True)
    table_data.columns = df.iloc[start_idx + 1].values  # Set column names from the header row
    
    # Ensure column names are unique
    table_data.columns = pd.Index([f"{col}_{i}" if col in table_data.columns[:i] else col for i, col in enumerate(table_data.columns)])
    
    # Check for an empty row to determine the end of the cluster data
    empty_row_index = table_data[table_data.isnull().all(axis=1)].index
    if not empty_row_index.empty:
        table_data = table_data.iloc[:empty_row_index[0]]
    
    # Filter out columns that contain only empty values
    table_data = table_data.dropna(axis=1, how='all')
    
    # Create a new DataFrame for the formatted output with metadata as the title row
    metadata_row = pd.DataFrame({
        'Cluster Number': [f"Cluster {cluster_number}"],
        'Size': [f"Size={size_info}"],
        'Homogeneity Coefficient': [f"HC={hc_info}"]
    })
    
    # Add empty columns for variables to align with the data columns
    for col in table_data.columns:
        if col not in metadata_row.columns:
            metadata_row[col] = ""
    
    # Concatenate metadata row, header row, and table data into a single DataFrame
    formatted_table = pd.concat([metadata_row, table_data], ignore_index=True)
    
    # Store the formatted table with a name based on the cluster number
    clusters[f"Cluster_{cluster_number}"] = formatted_table

# Write each formatted table to a new sheet in the existing Excel file
output_file = 'Final_Project/organized_tables.xlsx'
try:
    with pd.ExcelWriter(output_file, mode='a', if_sheet_exists='replace') as writer:
        if not clusters:
            print("No clusters found to write to the Excel file.")
        else:
            for cluster_name, cluster_data in clusters.items():
                print(f"Writing cluster: {cluster_name}")  # Debug print
                cluster_data.to_excel(writer, sheet_name=cluster_name, index=False)
    print(f"Data has been successfully reformatted and saved to {output_file}")
except Exception as e:
    print(f"Error writing to Excel file: {e}")