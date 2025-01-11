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
