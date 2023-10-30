import pandas as pd

# Create a sample DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
        'Age': [25, 30, 35, 28, 32]}

df = pd.DataFrame(data)

# Randomly select 2 rows from the DataFrame
random_rows = df.sample(n=2)

# Print the randomly selected rows
print(random_rows)
