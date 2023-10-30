import pandas as pd

# Create a sample DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Score': [85, 92, 78]}

df = pd.DataFrame(data)

# Rank the rows based on the 'Score' column
df['Rank'] = df['Score'].rank(ascending=False)

# Print the DataFrame with ranks
print(df)
