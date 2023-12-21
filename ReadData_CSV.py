# A simple way to store big data sets is to use CSV files (comma separated files).
import pandas as pd
df= pd.read_csv('Data.csv')
print(df)

# To print data of all file
print(df.to_string())

print(pd.options.display.max_rows)
pd.options.display.max_rows=10

print(df)
