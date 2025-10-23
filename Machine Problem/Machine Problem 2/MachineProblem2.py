# Author: Waken Cean C. Maclang
# Course: BSCSDS 3A
# October 23, 2025
# CSDS 312 - Machine Problem 2

import polars as pl
from plotnine import ggplot, aes, geom_bar, geom_point, labs, scale_fill_manual, theme_classic

# TASK 1: Collecting and Exploring Data

# Load the Dataset
df = pl.read_csv('Machine Problem\\Machine Problem 2\\online_sales.csv')

# Display the first few columns
df.head()

# Compute summary statistics for numeric columns (Quantity, etc.)
# Subset to get the integer columns then get their summary statistics
df.select(['Quantity', 'Unit_Price', 'Total_Price']).describe()

# Find the number of missing values
# We will select the null_count row in the statistic column to get the number of null values
df.describe().filter(
    pl.col('statistic').is_in(['null_count'])
)

# Create visualizations using plotnine

# Distribution of product categories
product_categories = (
    df.select(['Product', 'Category'])
        .unique()
        .group_by('Category')
        .agg(pl.count('Category').alias('Total_Categories'))
        .sort('Total_Categories', descending=True)
)

product_categories_plot = ggplot(product_categories) + \
        geom_bar(stat='identity', mapping=aes(x = 'Category', y='Total_Categories', fill='Category')) + \
        labs(
            title = 'Distribution of product categories',
            x = 'Category',
            y = 'Frequency'
        )
product_categories_plot

# Total Sales by Category
orders_per_category = (
    df.group_by('Category')
        .agg(pl.count('Order_ID').alias('Total_Orders'))
        .sort('Total_Orders', descending=True)
)

orders_per_category_plot = ggplot(orders_per_category) + \
        geom_bar(aes(x = 'Category', y='Total_Orders', fill='Category'), stat='identity') + \
        labs(
            title = 'Total Sales by Category',
            x = 'Category',
            y = 'Frequency'
        )
orders_per_category_plot

sales_per_category = (
    df.group_by('Category')
        .agg(pl.sum('Quantity').alias('Total_Sales'))
        .sort('Total_Sales', descending=True)
)

sales_per_category_plot = ggplot(sales_per_category) + \
        geom_bar(aes(x = 'Category', y='Total_Sales', fill='Category'), stat='identity') + \
        labs(
            title = 'Total Quantity bought by Category',
            x = 'Category',
            y = 'Frequency'
        )
sales_per_category_plot

# ===========================================================================

# TASK 2: Cleaning and Preparing Data

# Handle missing values

# Median imputation for Quantity
df_no_null = df.with_columns(pl.col('Quantity').fill_null(pl.col('Quantity').median()))

# Mean imputation for Unit Price based on Category
category_mean = (
    df.select('Category', 'Unit_Price')
        .group_by('Category')
        .agg(pl.col('Unit_Price').mean().alias('Mean'))
)

df_no_null = df_no_null.join(
                other=category_mean,
                on='Category',
                how='left')
df_no_null = df_no_null.with_columns(
                pl.when(pl.col('Unit_Price').is_null())
                .then(pl.col('Mean'))
                .otherwise(pl.col('Unit_Price'))
                .alias('Unit_Price')
            ) 
df_no_null = df_no_null.drop('Mean')

# Transforming Data (Total Price)
df_no_null = df_no_null.with_columns((pl.col('Quantity') * pl.col('Unit_Price')).alias('Total_Price'))
df_no_null = df_no_null.drop_nulls(['Customer_ID'])
df_no_null

# Standardize Dates
date_formats = [
    '%Y-%m-%d',
    '%d-%m-%Y',
    '%Y/%m/%d'
]

df_standard_date = df_no_null.with_columns(
    pl.coalesce(
        [pl.col('Order_Date').str.strptime(pl.Date, fmt, strict=False) for fmt in date_formats]
    )
)
df_standard_date['Order_Date']

# Convert columns to appropriate types
df_standard_date.head(1)
df_standard_formats = df_standard_date.with_columns(
    pl.col('Quantity').cast(pl.Int32)
)
df_standard_formats

# Remove Duplicates
df_unique = df_standard_formats.unique() \
                .sort('Order_ID', descending=False)
df_unique

# Save the DataFrame
df_unique.write_csv('Machine Problem\\Machine Problem 2\\cleaned_online_sales.csv')
