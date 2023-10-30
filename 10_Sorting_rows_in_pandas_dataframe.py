import pandas as pd

# Create a sample DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [25, 30, 35, 28],
        'Score': [85, 92, 78, 92]}

df = pd.DataFrame(data)

# Sort the DataFrame by the 'Age' column in ascending order
sorted_df = df.sort_values(by='Age')

# Print the sorted DataFrame
print("Sorted by Age:")
print(sorted_df)

# Sort the DataFrame by multiple columns
sorted_df = df.sort_values(by=['Score', 'Age'], ascending=[False, True])

# Print the sorted DataFrame
print("\nSorted by Score (descending) and Age (ascending):")
print(sorted_df)
