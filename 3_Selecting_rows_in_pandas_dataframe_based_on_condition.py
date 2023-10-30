import pandas as pd

data = {"emp_name": ['Anshu', 'Sneha', 'Samiksha', 'Shreya', 'Sanya', 'Abhijeet', 'Pradeep'],
    "salary": [100000000, 90000000, 80000000, 70000000, 60000000, 50000000, 40000000]}

df = pd.DataFrame(data, index = [1, 2, 3, 4, 5, 6, 7], columns = ["emp_name", "salary"])
print(df)

print('\r')

res = df[df['salary'] > 80000000]
# res = df.loc[df['salary'] > 80000000]
print(res)