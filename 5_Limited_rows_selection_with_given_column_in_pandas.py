# Import pandas package
import pandas as pd
	
# Define a dictionary containing employee data
data = {'Name':['Anshu', 'Sneha', 'Samiksha', 'Abhijeet'],
		'Age':[20, 19, 18, 19],
		'Address':['Chandigarh', 'Gurgaon', 'Delhi', 'Dehradun'],
		'Qualification':['B.C.A', 'B.C.A', 'B.C.A', 'B.tech']}
	
# Convert the dictionary into DataFrame
df = pd.DataFrame(data)
	
# select three rows and two columns
print(df.loc[0:1, ['Name','Age','Address','Qualification']])
print('\r')

print(df.loc[0:3, ['Name','Qualification']])
print('\r')

print(df.iloc [0:2, 1:3] )
