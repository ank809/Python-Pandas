import pandas as pd
import numpy as np
df = pd.DataFrame([[np.nan, 2, np.nan, 0],
                   [3, 4, np.nan, 1],
                   [np.nan, np.nan, np.nan, np.nan],
                   [np.nan, 3, np.nan, 4]],
                  columns=list("ABCD"))
print(df)

# Replace all nan values with 0
print(df.fillna(0))

# Replace all the nan values in column A, B, C, D as 0,1,2,3
values= {'A':0, 'B':1, 'C':2, 'D':3}
print(df.fillna(value=values))
