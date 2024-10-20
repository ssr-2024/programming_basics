import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns

# Define the absolute path to the Excel file
file_path = os.path.join('/Users/eliaskehrli/Library/Mobile Documents/com~apple~CloudDocs/Uni/Master/Sport/SSR Basismodul/programming_basics/Final_Project/testdata.xlsx')

# Read the entire Excel file without specifying the header
data = pd.read_excel(file_path, sheet_name='ropi_akt', header=None)

# Extract the header row (row 391)
header_row = data.iloc[391]

# Extract the table from rows 392 to 396 (inclusive)
start_idx = 392
end_idx = 396

# Extract the table and set the header
standardized_means_table = data.iloc[start_idx:end_idx + 1]
standardized_means_table.columns = header_row

# Drop the last row if it contains NaN values
standardized_means_table.dropna(how='all', inplace=True)

# Display the extracted table
print("Standardized Means Table:")
print(standardized_means_table)

# Exclude the cluster size column
cluster_size_column = 'CLsize'
standardized_means_table_no_size = standardized_means_table.drop(columns=[cluster_size_column])

# Melt the DataFrame to long format for plotting
melted_data = standardized_means_table_no_size.melt(id_vars=['Cluster'], var_name='Variable', value_name='Value')

# Custom titles for each cluster
custom_titles = {
    'CL1': 'Cluster 1 Coconut',
    'CL2': 'Cluster 2 Analysis',
    'CL3': 'Cluster 3 Analysis',
    'CL4': 'Cluster 4 Ananas',
    'CL5': 'Cluster 5 Analysis'
}

# Homogeneity Coefficient (HC) for each cluster
homogeneity_coefficients = {
    'CL1': 'HC: 1.70',
    'CL2': 'HC: 1.02',
    'CL3': 'HC: 0.78',
    'CL4': 'HC: 1.08',
    'CL5': 'HC: 0.73'
}

# Create a plot for each cluster
clusters = melted_data['Cluster'].unique()
for cluster in clusters:
    cluster_data = melted_data[melted_data['Cluster'] == cluster]
    cluster_size = standardized_means_table.loc[standardized_means_table['Cluster'] == cluster, cluster_size_column].values[0]
    
    plt.figure(figsize=(10, 6))
    sns.lineplot(data=cluster_data, x='Variable', y='Value', marker='o')
    plt.title(f'{custom_titles[cluster]}\n{homogeneity_coefficients[cluster]}')
    plt.xlabel('Variable')
    plt.ylabel('Standardized Mean')
    plt.ylim(-3, 3)  # Set y-axis range from -3 to 3
    plt.grid(True)
    plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
    plt.tight_layout()  # Adjust layout to prevent clipping of labels
    plt.legend([f'{cluster} (n={cluster_size})'], title='Cluster')
    plt.savefig(f'cluster_{cluster}.png')  # Save the plot as a PNG file
    plt.show()
    