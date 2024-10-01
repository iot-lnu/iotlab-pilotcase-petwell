import pandas as pd
import json
import sys

FILE_PATH = sys.argv[1]

with open(FILE_PATH, 'r') as file:
    json_data = json.load(file)

# Assuming 'data' is the top-level key where 'dataColumns' and 'specimenDataPoints' are nested
root_key = 'data'
nested_json_data = json_data[root_key]

# Extract dataColumns and specimenDataPoints
data_columns = nested_json_data['dataColumns']
specimen_data_points = nested_json_data['specimenDataPoints']

# Create a dictionary to map 'key' to 'name' for column names
column_mapping = {col['key']: col['name'] for col in data_columns}

# Create a DataFrame
df = pd.DataFrame(specimen_data_points, columns=column_mapping.keys())

# Rename columns from 'key' to 'name'
df.rename(columns=column_mapping, inplace=True)

print(df)

# Calculate and print the averages for all the columns
averages = df.mean()
print("\nAverage values for each column:")
print(averages)
