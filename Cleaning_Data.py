# Data cleaning means fixing bad data in your data set.
import pandas as pd
import numpy as np
df = pd.DataFrame({"name": ['Alfred', 'Batman', 'Catwoman'],
                   "toy": [np.nan, 'Batmobile', 'Bullwhip'],
                   "born": [pd.NaT, pd.Timestamp("1940-04-25"),
                            pd.NaT]})
print(df)
# Drop the rows where at least one element is missing.
df=df.dropna()
print(df)
df['born']=np.nan
print(df)

# Drop the columns where at least one element is missing.
df=df.dropna(axis='columns')
print(df)

# Drop the rows where all elements are missing.
df= df.dropna(how="all")
print(df)

# Keep only the rows with at least 2 non-NA values.
df.dropna(thresh=2, inplace=True)
print(df)

# Define in which columns to look for missing values.
df.dropna(subset=['name', 'toy'])
print(df)

print(df.notnull())

print(df.isnull())