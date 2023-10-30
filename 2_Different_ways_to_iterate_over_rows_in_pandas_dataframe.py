import pandas as pd
# Method 1: Using the index attribute of the Dataframe

data = {"Name": ['Anshu', 'Sneha', 'Samiksha', 'Shreya', 'Sanya'],
    "Stream": ['Science(Maths)', 'Science(Bio)', 'Commerce', 'Science(Maths)', 'Science(Maths)'],
    "Percentage": [100, 96, 95, 99, 98]}

df = pd.DataFrame(data, columns = ["Name", "Stream", "Percentage"])
print(df)

print('\r')

for dt in df.index:
    print(df['Name'][dt],':',df['Stream'][dt])
print('\r')
# -----------------------------------------------------------------------------------------------------------

# Method 2: Using loc[] function of the Dataframe
for i in range(len(df)):
    print(df.loc[i, 'Name'],":",df.loc[i, 'Percentage'])
print('\r')
# -----------------------------------------------------------------------------------------------------------

# Method 3: Using iloc[] function of the DataFrame
for i in range(len(df)):
    print(df.iloc[i, 0],":",df.iloc[i, 1],":",df.iloc[i, 2])
print('\r')
# -----------------------------------------------------------------------------------------------------------

# Method 4: Using iterrows() method of the Dataframe
for idx, row in df.iterrows():
    print(row['Name'],":",row['Stream'])
print('\r')
# -----------------------------------------------------------------------------------------------------------

# Method 5: Using itertuples() method of the Dataframe
for row in df.itertuples(index=False):
    print(f"Name: {row.Name}, Percentage: {row.Percentage}")
