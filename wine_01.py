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
#Null Handling 
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
# Question 1: What are all the unique values in the 'quality' column, including NULL values?
# Expected output should show: [5, 6, None]

# Question 2: How many unique fixed_acidity values are there (including NULL)?
# Hint: Use len() with unique()

# Question 3: Create a list of all unique alcohol percentages sorted in ascending order.
# Hint: Combine unique() with sort()
df['quality'].unique()
len(df['fixed acidity'].unique())
sorted(df['alcohol'].unique())
# nunique() Practice:
#  Question 4: How many unique values are there in each column, excluding NULL values?
# Hint: Use nunique() on the entire DataFrame

# Question 5: Which column has the most unique values (excluding NULL)?
# Hint: Use nunique() and idxmax()

# Question 6: Compare the difference between unique() and nunique() for the 'rating' column.
# What's different about their outputs?
df.nunique()
df.nunique().idxmax()
difference = df['alcohol'].unique() - df['alcohol'].nunique()
print(difference)
df.head()
#Duplicates 
# Identify Duplicate Rows in a DataFrame:
# Use the duplicated() function to find all duplicate rows in the dataframe, considering all columns. 
#(Display the rows that are duplicates.)
df.duplicated()
#Drop Functions
# Drop Rows or Columns:
# a) Drop the row with index 2 from the dataset.

# b) Drop the column 'quality' from the dataset.

df.drop(2, axis = 0, inplace=False)
df.drop('quality', axis =1, inplace=False)
# 2. Value Checking with isin():
# a) Create a list of ['7.8', '9.8'] and check if the values in the 'alcohol' column match any value in the list.

# b) Check if the 'quality' column contains the values ['5', '6'].

# c) Check if the alcohol column contains any of the following values: 7.4, 9.4, 10.0.


df['alcohol'].isin([7.9,9.8])
df['quality'].isin([5,6])
df['alcohol'].isin([7.4,9.4,10.0])
# Value Checking with between():
# a) Check if the values in the 'alcohol' column are between 7.0 and 9.0 (inclusive).

# b) Check if the values in the 'sulphates' column are between 0.5 and 1.0 (exclusive).

# c) Check if the values in the 'citric acid' column are between 0.0 and 0.5 (inclusive
df['alcohol'].between(7.0,9.0, inclusive='both')
df['sulphates'].between(1.0, 5.0, inclusive='neither')
df['citric acid'].between(0.0,0.5, inclusive='both')
# 1. Convert Data Types:
# a) Convert the 'fixed acidity' column to integer type (e.g., int).
# b) Convert the 'quality' column to category type, as it has a limited number of unique values.
# c) Convert the 'alcohol' column to integer type (round off the decimal points).
df['column_name'] = df['column_name'].astype(new_type)
df['fixed acidity'] = df['fixed acidity'].astype(int)
print(df.dtypes)
df['quality'] = df['quality'].astype('category')
print(df.dtypes)

df['aclohol'] = df['alcohol'].astype(int)
print(df.dtypes)
#  Replace Specific Values:
# a) Replace all occurrences of the value 0.00 in the 'citric acid' column with 0.1.
# b) Replace the value 0.9978 in the 'density' column with 0.9985.
# df.replace(['Jane', 'Jack'], ['Janet', 'Jackson'], inplace=True)

df['citric acid'].replace([0.00, 0.01], inplace=False)

df.head()
df['citric acid'].replace(0.00,None)
df['quality'].replace({5 : 'Low, 6 : High'})

df[df['alcohol'] > 10]
df['pH'].mean()
df['quality'].unique()
# Replace Specific Values
# Replace all rows where quality equals 5 with Low Quality.
# Replace all rows where quality equals 6 with High Quality
df['quality'].replace({5 : 'Low Quality'})
df['quality'].replace({6 : 'High Quality'})
# Replace Values Based on Conditions
# Replace all values in the alcohol column that are less than 10 with Below Average.
# Replace all values in the pH column that are greater than 3.5 with High pH.
df['pH'].replace(df['pH'] > 3.5)
df['alcohol'].apply(lambda x : 'Below Average' if x < 10 else x )
