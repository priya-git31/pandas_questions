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


# Counting - Count 
df.head(5)
# 1. Using count()
# How many non-null values are there in each column of the dataset?
# How many non-null values are there in the column quality?
df.count()
df['quality'].count()
# 2. Using size
# What is the total number of elements (rows × columns) in the dataset?
# How many total elements are present in the first 5 rows of the dataset?
df.size
df.loc[0:4].size
#  Using value_counts()
# How many times does each unique value appear in the quality column?
# What is the frequency distribution of the alcohol column values in the first 5 rows?
# Which pH value appears most frequently in the dataset?
df['quality'].value_counts()
df.loc[0:4,'alcohol'].value_counts()
df['pH'].value_counts().max()
df.head()


#NULL HANDLING 
# sna() and isnull() : 

# Question 1: Using isna() or isnull(), find out how many missing values are in each column of wine_df?

# Question 2: Which row has the most missing values? Write code to find this.
missing_per_row = wine_df.isna().sum(axis=1)
most_missing_row = missing_per_row.idxmax()
df.isna().sum()
missing_per_row = df.isna().sum(axis=1)
most_missing_row = missing_per_row.idxmax()
print(most_missing_row)
# fillna() Practice:
    
# Question 3: Fill all missing values in the 'fixed_acidity' column with the mean of existing values.

# Question 4: Fill missing values in 'volatile_acidity' with the previous valid value (forward fill).

df['fixed acidity'].fillna(df['fixed acidity'].mean())
df['volatile acidity'].fillna(method='ffill')

fill_dict = {
    'fixed_acidity': wine_df['fixed_acidity'].median(),
    'chlorides': 0
}
wine_df = wine_df.fillna(value=fill_dict).fillna(wine_df.mean())
# notnull() Practice:
#  Question 6: How many complete cases (rows with no missing values) are there in the dataset?
complete_cases = df.notnull().all(axis=1).sum()
print(complete_cases)

# Question 8: Remove all rows that have any missing values.

# Question 9: Remove only the rows where 'quality' is missing.
# Hint: Look up the 'subset' parameter

df.dropna()
df.dropna(subset=['quality'])
