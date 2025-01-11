# Questions based on Pandas Functions

# INDEXING 

# 1. How do you select rows and columns by labels in Pandas using `loc`?
# The loc function in Pandas is used to select rows and columns by labels (index labels and column names).

# It follows the syntax:
# df.loc[row_labels, column_labels]
    
# row_labels: Can be a single label, list of labels, or a slice of labels (e.g., 'row1':'row3').
# column_labels: Can be a single label, list of labels, or slice of labels.

# 2. How can you select rows and columns by their numerical indices using `iloc`?
# Select a single row by label: df.loc['row1']
# Select specific rows and columns: df.loc[['row1', 'row2'], ['column1', 'column2']]
# Select all rows for specific columns : df.loc[:, ['column1', 'column2']]

# 3. What's the difference between `loc` and `iloc` in Pandas?
# loc selects data using labels.
# It’s useful when you work with row names (index labels) or column names directly.
# For example: df.loc['row_label', 'column_label']
# Here, 'row_label' and 'column_label' are the names of the row and column.
# If you want rows A to C and columns X to Z, you can write:
# df.loc['A':'C', 'X':'Z']
# Both start and end labels are included.

# iloc selects data using integer positions.
# It’s useful when you work with row and column positions instead of their names.
# For example: df.iloc[0, 1]
# Here, 0 is the first row, and 1 is the second column.
# To select rows 0 to 2 and columns 1 to 3, you can write:
# df.iloc[0:3, 1:4]
# Important: The end position is excluded



#COUNTING 
# 4. How do you count the number of non-NA/null observations in a DataFrame using Pandas?
# To count the number of non-NA/null observations in a DataFrame, use the count() function.

# By default, it operates column-wise, counting non-null values in each column.
# If you want row-wise counts, specify axis=1.

# Syntax:
# df.count(axis=0)  #Default: Counts non-null values in each column
# df.count(axis=1)  #Counts non-null values in each row

# 5. What function can you use to get the total size (number of elements) in a Pandas DataFrame?
# To get the total size (number of elements in all rows and columns) of a DataFrame, use the size attribute.
# df.size


# 6. How can you count the occurrences of unique values in a Pandas Series using value_counts()?
# The value_counts() function is used to count the occurrences of unique values in a Pandas Series. 
# It returns a Series with unique values as the index and their counts as values, sorted in descending order.

# series.value_counts(normalize=False, sort=True, ascending=False)
# normalize=True: Return proportions instead of counts.
# sort=False: Disable sorting by count.
# ascending=True: Sort counts in ascending order.


# NULL Handling
# 7. How do you check for missing values in a Pandas DataFrame using `isna()` or `isnull()`?
# The isna() (or its alias isnull()) function is used to check for missing (NaN/None) values in a Pandas DataFrame or Series.
# It returns a DataFrame/Series of the same shape, with True for missing values and False for non-missing values.
# df.isna()  # or df.isnull()



# 8. What function do you use to replace missing values in Pandas?
# The fillna() function is used to replace missing (NaN/None) values in a DataFrame or Series with a specified value or method.

# df.fillna(value, method=None, axis=None, inplace=False)

# value: The value to replace missing values with.
# method: Options are 'ffill' (forward fill) or 'bfill' (backward fill).
# inplace: If True, modifies the DataFrame in place.


# 9. How can you drop rows with missing values from a DataFrame using Pandas?
# The dropna() function removes rows (or columns) with missing values from a DataFrame.

# df.dropna(axis=0, how='any', inplace=False)
# axis=0: Drops rows (default).
# axis=1: Drops columns.
# how='any': Drops rows/columns if any value is missing.
# how='all': Drops rows/columns only if all values are missing.

# 10. How do you find non-null values in a DataFrame using `notnull()`?
# The notnull() function is used to check for non-missing (non-NaN) values in a DataFrame or Series.
#  It returns a DataFrame/Series of the same shape, with True for non-null values and False for null values

# df.notnull()


# UNIQUE VALUES 

# 11. How can you retrieve unique values from a Pandas Series using `unique()`?
# The unique() function is used to retrieve all unique values from a Pandas Series.
# It returns a NumPy array of unique values.

# series.unique()
# unique_values = data.unique()

# 12. What function in Pandas can you use to count the number of unique values in a column (`nunique`)?
# The nunique() function counts the number of unique values in a Series or DataFrame column.
# It excludes NaN values by default

# series.nunique(dropna=True)
# df['column_name'].nunique(dropna=True)



# Duplicate Handling
# 13. How do you check for duplicate rows in a Pandas DataFrame using `duplicated()`?
# The duplicated() function identifies duplicate rows in a DataFrame.
# It returns a Series of True for duplicate rows and False for unique rows.

# df.duplicated(subset=None, keep='first')
# subset: Columns to consider for identifying duplicates (default is all columns).
# keep: Options are:
# 'first': Mark duplicates except the first occurrence (default).
# 'last': Mark duplicates except the last occurrence.
# False: Mark all duplicates as True.

# 14. How can you remove duplicate rows from a DataFrame using `drop_duplicates()`?
# The drop_duplicates() function removes duplicate rows from a DataFrame.

# df.drop_duplicates(subset=None, keep='first', inplace=False)

# subset: Columns to consider for identifying duplicates (default is all columns).
# keep: Options are:
# 'first': Keep the first occurrence of duplicates (default).
# 'last': Keep the last occurrence.
# False: Remove all duplicates.
# inplace: If True, modifies the DataFrame in place.

#  ROW OPERATIONS
# 15. What function allows you to drop specific rows or columns in a DataFrame?
# The drop() function allows you to remove specific rows or columns from a DataFrame.

# df.drop(labels, axis=0, inplace=False)
# labels: The row/column labels to drop.
# axis:
# 0 (default): Drops rows.
# 1: Drops columns.
# inplace: If True, modifies the DataFrame in place.


# Value Checking
# 16. How do you check if a value exists in a DataFrame or Series using `isin()`?

# The isin() function is used to check if a value (or set of values) exists in a DataFrame or Series.
# It returns a boolean DataFrame/Series where True indicates the presence of the value(s).

# df.isin(values)
# series.isin(values)

# values: A single value, list, or set of values to check.

# 17. How can you check if values in a Series or DataFrame fall within a specified range using `between()`?
# The between() function checks if values in a Series or
# DataFrame fall within a specified range (inclusive by default).

# series.between(left, right, inclusive='both')

# left: The lower bound of the range.
# right: The upper bound of the range.
# inclusive: Defines whether the bounds are inclusive. Options:
# 'both': Include both bounds (default).
# 'neither': Exclude both bounds.
# 'left': Include only the lower bound.
# 'right': Include only the upper bound.


# TYPE CONVERSION
# 18. How do you change the data type of a column in Pandas using `astype()`?
# The astype() function is used to change the data type of a column in Pandas. 
# It allows you to convert a column to types like int, float, str, or even category.

# df['column_name'] = df['column_name'].astype('desired_type')


# VALUE REPLACEMENT 
# 19. What function in Pandas can you use to replace specific values in a DataFrame?

# The replace() function is used to replace specific values in a DataFrame or Series. 
# You can replace single values, lists, or even use regular expressions.

# df.replace(to_replace, value, inplace=False)
# to_replace: The value(s) to be replaced.
# value: The new value(s) to replace with.
# inplace: If True, modifies the DataFrame in place.

# RENAMING
# 20. How do you rename columns or index labels in a Pandas DataFrame using `rename()`?
# The rename() function allows you to rename columns or 
# index labels in a DataFrame by providing a mapping of old names to new names.


# df.rename(columns={'old_column': 'new_column'}, index={'old_index': 'new_index'}, inplace=False)

# CLIPPING
# 21. How can you clip values in a DataFrame or Series to within a specified range using `clip()`?
# The clip() function restricts values in a DataFrame or Series to fall within a specified range.
# Any values outside the range are replaced by the boundary values.

# df.clip(lower=None, upper=None, inplace=False)

# lower: The minimum value.
# upper: The maximum value.
# inplace: If True, modifies the DataFrame in place.

# EXPANSION
# 22. How do you transform a list-like column of a DataFrame into separate rows using `explode()`?

# The explode() function transforms a list-like column in a DataFrame into separate rows.
# Each element in the list becomes a new row, while the other columns are duplicated for these rows.

# df.explode(column, ignore_index=False)
# column: The name of the column to be exploded.
# ignore_index: If True, resets the index of the resulting DataFrame (default is False).

# import pandas as pd

# data = {
#     'Name': ['Alice', 'Bob'], 
#     'Hobbies': [['Reading', 'Cycling'], ['Cooking', 'Swimming']]
# }
# df = pd.DataFrame(data)

# print(df)
#      Name                 Hobbies
# 0   Alice     [Reading, Cycling]
# 1     Bob   [Cooking, Swimming]

#  After using explode
#      Name      Hobbies
# 0   Alice     Reading
# 0   Alice     Cycling
# 1     Bob     Cooking
# 1     Bob     Swimming

# What happened here?
# Each element from the lists in the Hobbies column became a separate row.
# The other column (Name) is repeated to match the new rows.



# FLATTENING 
# 23. What function can be used to flatten nested data in Pandas?

# To flatten nested data, you can use json_normalize() (from pandas.json)
# for JSON-like structures or manually process using apply(pd.Series) for specific columns.

# Option 1: Using json_normalize()
# This is useful for flattening JSON-like nested structures into a DataFrame.


# from pandas import json_normalize
# json_normalize(data, record_path=None, meta=None)
# record_path: Path to the nested list/records to be flattened.
# meta: Additional fields to extract.

# Option 2: Using apply(pd.Series) for a single column
# If a column contains dictionaries or lists, this flattens it.

# data = {'A': [1, 2], 'B': [{'C': 3, 'D': 4}, {'C': 5, 'D': 6}]}
# df = pd.DataFrame(data)

# # Flatten column 'B'
# df_flattened = pd.concat([df.drop(columns='B'), df['B'].apply(pd.Series)], axis=1)
# print(df_flattened)
# # Output:
# #    A  C  D
# # 0  1  3  4
# # 1  2  5  6

# data = {'A': [1, 2], 'B': [{'C': 3, 'D': 4}, {'C': 5, 'D': 6}]}
# df = pd.DataFrame(data)

# # Flatten column 'B'
# df_flattened = pd.concat([df.drop(columns='B'), df['B'].apply(pd.Series)], axis=1)
# print(df_flattened)
# # Output:
# #    A  C  D
# # 0  1  3  4
# # 1  2  5  6


# INDEX RESETTING 
# 24. How can you reset the index of a DataFrame using `reset_index()`?
The melt() function reshapes a DataFrame from wide format (columns represent variables) to long format (rows represent variables)
# The reset_index() function resets the index of a DataFrame. 
# By default, the old index is added as a new column, and a new sequential index is created.

# df.reset_index(drop=False, inplace=False)
# drop: If True, the old index is not added as a column (default is False).
# inplace: If True, modifies the DataFrame in place.


# DATA RESHAPING 
# 25. How do you reshape a DataFrame from wide to long format using `melt()`?
# The melt() function reshapes a DataFrame from wide format (columns represent variables) to long format (rows represent variables)

# pd.melt(df, id_vars, value_vars, var_name, value_name)
# id_vars: Columns to keep fixed (identifier columns).
# value_vars: Columns to "melt" into rows (optional).
# var_name: Name for the melted variable column (optional).
# value_name: Name for the melted value column (optional).
    
#     data = {'Name': ['Alice', 'Bob'], 'Math': [90, 80], 'Science': [85, 95]}
# df = pd.DataFrame(data)

#     Name  Math  Science
# 0  Alice    90       85
# 1    Bob    80       95

# # After `melt()`
# df_melted = pd.melt(df, id_vars=['Name'], var_name='Subject', value_name='Score')
# print(df_melted)

#     Name   Subject  Score
# 0  Alice      Math     90
# 1    Bob      Math     80
# 2  Alice   Science     85
# 3    Bob   Science     95

# Key Points:
# id_vars specifies columns to keep as-is:
# These columns will remain in the melted DataFrame as they are. In your case, 'Name' is listed in id_vars, so it is preserved in the resulting DataFrame.
# All other columns are melted:
# Any column not explicitly mentioned in id_vars is automatically treated as a variable and melted into the new "variable" column (named Subject in your example).
# Even if there are more columns:
# It doesn't matter how many additional columns are in the DataFrame. As long as they are not listed in id_vars, they will be melted

# 26. How do you stack the columns of a DataFrame into rows using Pandas?

# The stack() function stacks the columns of a DataFrame into a multi-indexed Series. 
# It moves the column labels to the row index.

# df.stack(level=-1, dropna=True)
# level: The column level to stack (default is -1, the innermost level).
# dropna: Whether to drop missing values (default is True).

# data = {'Math': [90, 80], 'Science': [85, 95]}
# df = pd.DataFrame(data, index=['Alice', 'Bob'])

#        Math  Science
# Alice    90       85
# Bob      80       95

# df_stacked = df.stack()
# Alice  Math        90
#        Science     85
# Bob    Math        80
#        Science     95


# 27. What does the `unstack()` function do in Pandas?
# The unstack() function reshapes a DataFrame or
# Series by moving the innermost row index level to the column level.

# df.unstack(level=-1, fill_value=None)
# level: The row level to unstack (default is -1, the innermost level).
# fill_value: Value to fill missing data (default is None).

# data = {'Math': [90, 80], 'Science': [85, 95]}
# df = pd.DataFrame(data, index=['Alice', 'Bob']).stack()

# # Before `unstack()`
# print(df)

# Alice  Math        90
#        Science     85
# Bob    Math        80
#        Science     95
# dtype: int64

# After `unstack()`
# df_unstacked = df.unstack()
# print(df_unstacked)

#        Math  Science
# Alice    90       85
# Bob      80       95



# 28. How do you pivot a DataFrame to transform unique values of a column into column headers?
# 29. What is the use of `crosstab()` in Pandas?

# DATA EXPANSION
# 30. How can you use the `expanding()` function in Pandas for cumulative operations?
# 31. How do you perform interpolation to fill missing values in a DataFrame using `interpolate()`?