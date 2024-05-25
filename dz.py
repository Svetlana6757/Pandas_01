import pandas as pd

df = pd.read_csv('dz.csv')
print(df.head(10))

df.dropna(inplace=True)
print(df.head(10))

group = df.groupby('City')['Salary'].mean()
print(group)