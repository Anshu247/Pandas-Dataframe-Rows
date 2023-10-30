import pandas as pd

# Create a sample DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35]}

df = pd.DataFrame(data)

# Set the 'Name' column as the row index
df.set_index('Name', inplace=True)

# Print the DataFrame with 'Name' as the row index
print(df)
