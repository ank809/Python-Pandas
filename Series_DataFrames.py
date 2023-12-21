import pandas as pd
import numpy as np

ser= pd.Series(np.random.randint(1, 10,7))
# gives the result with index
print(ser)
print(type(ser))

# In random you just pass the shape of the array
# In randint you pass the low and the high value and also the shape/size of the array
df= pd.DataFrame(np.random.rand(334, 5))
df1= pd.DataFrame(np.random.randint(1, 1000, size=(334, 5)))
print(df1)
print(type(df1))

print(df1.describe())

print(df1.head())

print(df1.tail())

df1[1][1]='Ankita'

print(df1)

print(type(df1))

print(df1.dtypes)
print(df1.index)
print(df1.columns)

# Print transpose of array i.e. roe to column and column to rows
print(df1.T)

# To convert dataframe to numpy array
print(df1.to_numpy())

# Sort array index wise axis=0 is rows and axis=1 is column
print(df1.head().sort_index(axis=0, ascending=False))

print(df1.head().sort_index(axis=1, ascending=False))

# To print column only i.e 3
print(df1.head())

print(df1[2])
print(type(df1[2]))

df2=df1
print(df2)
df2[1][4]=101
print(df1)
print(df2)

df1.columns= list("ABCDE")
print(df1)

print(df1['A'])

print(df1['A'][ 4])
# print(df1[4]['A']) error
print(df1.loc[4, 'A'])

df1.loc[0,0]=62   # if the column do not exist it create a new one
print(df1.head())

# To delete a column or row
# it will delete the first row
df1=df1.drop(0, axis=0)
print(df1.head())

df1.drop(0, axis=1) # if you do this it will not actually change the dataframe
# and to do write inplace
df1.drop(0, axis=1, inplace=True) # if you write like this it will change the original data frame
# it will delete column

# df1= df1.drop(0, axis=1)   # here 0 is the label
print(df1.head())


# df1.columns= list('!@#$%')
# print(df1.head())

# To print specific rows and columns
print(df1.loc[[2,3],['B','C','D']])

# All columns and specific row
print(df1.loc[[2,3],:])

# All rows and specific columns
print(df1.loc[:,['B','C','D']])

# To get rows on the basis of some condition
print(df1.loc[(df1['A']<400)])

print(df1.loc[(df1['A']<400) & (df1['C']>500)])

# To search from index
print(df1.iloc[0,4])

# If you want to reset index after deletion
print(df1.head())
df1.drop([3,5], axis=0, inplace=True)
print(df1.head())
# print(df1.reset_index())
# But the problem is it add a new column of name index and to remove that
# df1.reset_index(drop=True, inplace=True)
print(df1.head())