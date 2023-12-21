# Pandas is a Python library used for working with data sets(ordered collection of data)
# It has functions for analyzing, cleaning, exploring, and manipulating data.
# Pandas allows us to analyze big data and make conclusions based on statistical theories.
# Pandas can clean messy data sets, and make them readable and relevant.
# Pandas are also able to delete rows that are not relevant, or contains wrong values,
# like empty or NULL values. This is called cleaning the data.
# Pandas have two types of data structure:
# 1. Series:it is one dimensional array with indexes and store data in single row and column in dataframe
# can store only one data of one type
# 2. DataFrames:it is 2-d array and has spreadsheet like structure representing rows and columns
# stores data of different types

import pandas as pd

dict1 = {
    "Name": ["Ankita", 'Astha', 'Anshuman', 'Rahul', 'Surya'],
    "Age": [19, 21, 11, 14, 23],
    "City": ['Mandi', 'Kullu', 'Rampur', 'Hamirpur', 'Shimla']
}
print(dict1)
df = pd.DataFrame(dict1)
print(df)

df.to_csv('Friends.csv')
df.to_csv('Friends_Index_False.csv', index=False)

# You want to see only first two rows
print(df.head(2))

# You want to see only last two rows
print(df.tail(2))

print(df.describe())

df.to_excel("Names.xlsx")
