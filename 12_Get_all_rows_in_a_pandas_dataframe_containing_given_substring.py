import pandas as pd

# Create a sample DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'City': ['New York', 'Los Angeles', 'Chicago', 'San Francisco']}

df = pd.DataFrame(data)

# Find rows where 'City' column contains the substring 'New'
substring = 'or'
filtered_df = df[df['City'].str.contains(substring)]

# Print the filtered DataFrame
print(filtered_df)
