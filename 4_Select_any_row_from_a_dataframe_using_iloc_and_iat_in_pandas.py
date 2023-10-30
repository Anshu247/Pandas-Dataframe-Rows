import pandas as pd

data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35]}

df = pd.DataFrame(data)
print(df)

print('\r')

# Select the second row using iloc[]
selected_row = df.iloc[1]

# Print the selected row
print(selected_row)

print('\r')

# Select a specific element in the second row and first column using iat[]
selected_element = df.iat[1, 0]

# Print the selected element
print(selected_element)
