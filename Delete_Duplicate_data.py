import pandas as pd
df = pd.DataFrame({
    'brand': ['Yum Yum', 'Yum Yum', 'Indomie', 'Indomie', 'Indomie'],
    'style': ['cup', 'cup', 'cup', 'pack', 'pack'],
    'rating': [4, 4, 3.5, 15, 5]
})
print(df)
# By default, for each set of duplicated values, the first occurrence is set on False and all others on True.
print(df.duplicated())

# By using ‘last’, the last occurrence of each set of duplicated values is set on False and all others on True.
print(df.duplicated(keep='last'))

# By setting keep on False, all duplicates are True.
print(df.duplicated(keep=False))

# To find duplicates on specific column(s), use subset.
print(df.duplicated(subset=['brand']))

print(df.drop_duplicates())
print(df.drop_duplicates(subset=['brand']))