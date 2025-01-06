
import os
os.listdir()
import pandas as pd
import numpy as np

df = pd.read_csv('winequality-red.csv')
df.head(2)
df.head()
df.tail()
df.sample(5)
df.describe()
df.info()
df.shape
df.size
df.columns
df.columns.tolist()
df.head()
df.loc[1]
df.loc[1:3]
df.loc[1,'fixed acidity']
df.loc[3,'chlorides']
df.loc[4,'alcohol']
df.loc[0:1, ['chlorides', 'density']]
df.loc[2:3, ['residual sugar','pH']]


##ILOC 
df.head()

##Use iloc to access the value in the 3rd row and 2nd column (corresponding to volatile acidity in row 3).
df.iloc[2,1]
# Use iloc to retrieve the 4th row (all values for fixed acidity, volatile acidity, etc.).
df.iloc[3,:]
# Use iloc to access the 6th column (likely free sulfur dioxide) for all rows.
df.iloc[:,5]
# Use iloc to access the first 3 rows.
df.iloc[0:3]
# Use iloc to select only the 1st, 3rd, and 5th columns.
df.iloc[[0,2,4]]
# Use iloc to access rows 2 to 5 and columns 3 to 6 (slice both rows and columns).
df.iloc[2:5,3:7]
# Non-Sequential Rows and Columns
# Use iloc to access rows at index 0, 2, and 4, and columns 1, 3, and 5.
df.iloc[[0,2,4],[1,2,5]]




