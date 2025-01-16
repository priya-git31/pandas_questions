import pandas as pd
# Read the CSV file into the 'sales_df' object (Sales DataFrame)
sales_df = pd.read_csv('retail_sales_profits.csv')
sales_df.head()

# Print the DataFrame index
sales_df.index

#INDEX 1.1

# Set Index While Loading Data

# sales_df = pd.read_csv('retail_sales_profits.csv', 
#                       index_col='Store Department')

# sales_df.head()

#INDEX 1.2

# Change Index After Data is Loaded

sales_df = sales_df.set_index('Store Department')
sales_df.head()

# ACCESS ROWS BY INDEX 1.1

# Access a row (department) using the string index label

sales_df.loc['Haircare']
sales_df.loc['TVs']

# Access rows for multiple departments
# Notice the use of double square brackets

sales_df.loc[['Haircare', 'TVs']]

sales_df.loc[['Football', 'Men']]

# Print DataFrame Information

sales_df.info()

# Summarize Numerical Data
sales_df.describe()

# RENAME 1.1

# Rename Column Labels

sales_df.columns

# Relabel Specific Columns
# sales_df = sales_df.rename(columns={"Store Category" : 'Category', "Q3 Sales ($)" : "Q3_sales"})
# sales_df.head()

sales_df.head()
# Change Labels for All Columns

new_column_labels  = ['Category', 'Q3_Sales', 'Q3_Profit' , 'Q4_Sales', 'Q4_Profit']

sales_df = sales_df.set_axis(new_column_labels, axis=1)
sales_df.head()
# Update Index Name
sales_df.index.name = 'Department'
sales_df.tail()
# SELECT COLUMNS 
# Get a single column
sales_df['Category']
# Retrieve Multiple Columns
# You’ll need to use double square brackets, [[]], to fetch multiple columns. Why is that?
# The inner square brackets create a list of columns. 
# Then we pass that list to outer square brackets. That tells Pandas to retrieve all the columns from the list.

sales_df[['Category', 'Q3_Sales']]
# SUMMAZRIZE CATEGORICAL COLUMNS 
sales_df.head()
# Get Unique Values
sales_df['Category'].unique()
# Count Unique Values

sales_df['Category'].value_counts()
# Drop Columns

sales_df.head()
sales_df = sales_df.drop(columns=['Q3_Profit', 'Q4_Profit'])
sales_df.head()
sales_df.head()
# Fetch all the rows from the electronics category
# You'll need to pass the 'Electronics' in single quotes

sales_df.query("Category == 'Home'")
# Search rows that match both conditions:
# 1. product category is Clothing
# 2. Q3 sales over $5,000

sales_df.query("Category == 'Sports' and Q3_Sales > 2000")
# SORT DATA
sales_df.sort_values(by='Q4_Sales', ascending=True )



