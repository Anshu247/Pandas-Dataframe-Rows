import pandas as pd

# Create a sample DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35]}

df = pd.DataFrame(data)

# Create a new row to insert
new_row = {'Name': 'David', 'Age': 28}

# Define the position where you want to insert the new row (0-based index)
insert_position = 1

# Use the DataFrame 'loc' method to insert the new row
df.loc[insert_position] = new_row

# Reset the index if needed
df.reset_index(drop=True, inplace=True)

# Print the modified DataFrame
print(df)


