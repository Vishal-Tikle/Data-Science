import pandas as pd

# Read data from a CSV file
data = pd.read_csv('House_Price.csv')

# Filter data based on a condition
filtered_data = data[data['BHK'] > 2]

print(filtered_data)

# Sort data based on a column
sorted_data = data.sort_values('Floor')

print("---------------------------------------")
print(sorted_data)

data1 = data[["Location", "BHK"]]
data2 = data[["Location", "Floor"]]

# Merge the two DataFrames based on the 'ID' column
merged_data = pd.merge(data1, data2, on='Location')

print("------------------------------------------")
# Print the merged data
#print(merged_data)