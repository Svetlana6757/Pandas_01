import pandas as pd
import openpyxl



df = pd.read_excel('netflix_titles.xlsx')
print(df.head())

print(df.info())
print(df.describe())

df.fillna(0, inplace=True)

df.drop('description', axis=1, inplace=False)
print(df)

group = df.groupby('year_added1')
print(group)