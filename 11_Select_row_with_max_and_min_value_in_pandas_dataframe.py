# importing pandas and numpy
import pandas as pd
import numpy as np

# data of 2018 drivers world championship
dict1 = {'Driver': ['Hamilton', 'Vettel', 'Raikkonen',
					'Verstappen', 'Bottas', 'Ricciardo',
					'Hulkenberg', 'Perez', 'Magnussen',
					'Sainz', 'Alonso', 'Ocon', 'Leclerc',
					'Grosjean', 'Gasly', 'Vandoorne',
					'Ericsson', 'Stroll', 'Hartley', 'Sirotkin'],

		'Points': [408, 320, 251, 249, 247, 170, 69, 62, 56,
					53, 50, 49, 39, 37, 29, 12, 9, 6, 4, 1],

		'Age': [33, 31, 39, 21, 29, 29, 31, 28, 26, 24, 37,
				22, 21, 32, 22, 26, 28, 20, 29, 23]}

# creating dataframe using DataFrame constructor
df = pd.DataFrame(dict1)
print(df.head(10))

print('\r')

# creating dataframe using DataFrame constructor
df = pd.DataFrame(dict1)

# the result shows max on
# Driver, Points, Age columns.
print(df.max())
print('\r')

# creating dataframe using DataFrame constructor
df = pd.DataFrame(dict1)

# Who scored more points ?
print(df[df.Points == df.Points.max()])
print('\r')

# creating dataframe using DataFrame constructor
df = pd.DataFrame(dict1)

# what is the maximum age ?
print(df.Age.max())
print('\r')

# creating dataframe using DataFrame constructor
df = pd.DataFrame(dict1)

# the result shows min on
# Driver, Points, Age columns.
print(df.min())
print('\r')

# creating dataframe using DataFrame constructor
df = pd.DataFrame(dict1)

# Who scored less points ?
print(df[df.Points == df.Points.min()])
print('\r')

# creating dataframe using DataFrame constructor
df = pd.DataFrame(dict1)

# Which row has maximum age |
# who is the youngest driver ?
print(df[df.Age == df.Age.min()])
