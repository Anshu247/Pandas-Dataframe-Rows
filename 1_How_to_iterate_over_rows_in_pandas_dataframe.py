import pandas as pd

# Create a sample DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35]}

df = pd.DataFrame(data)

# Using iterrows
for index, row in df.iterrows():
    print(f"Index: {index}, Name: {row['Name']}, Age: {row['Age']}")

print('\r')

# Using itertuples
for row in df.itertuples(index=False):
    print(f"Name: {row.Name}, Age: {row.Age}")
