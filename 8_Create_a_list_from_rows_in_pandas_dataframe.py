import pandas as pd

# Create a sample DataFrame
data = {'Name': ['Anshu', 'Sneha', 'Shreya'],
        'Age': [20, 19, 18]}

df = pd.DataFrame(data)

# Convert the DataFrame rows to a list of lists using 'values' property
list_of_rows = df.values.tolist()

# Print the list of rows
print(list_of_rows)
