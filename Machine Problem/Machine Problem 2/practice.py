import polars as pl
# from plotnine import ggplot, aes, geom_histogram, theme_minimal

# Sample dataset with missing values
df = pl.DataFrame({
    "student": ["Waken Maclang", "allan Tagle", "dAve Gigawin", "Jeff pauSal"],
    "date": ["2025-01-01", "2025/01/02", "01-03-2025", None],
    "score": [85, None, 90, None],
    "course": ["Math", "math", "science", None]
})

# Data Cleaning and Preparation 
# 
# 1. Handling Missing and Incomplete Data Values
# 2. Formatting Data
# 3. Transforming Data
# 4. Visualization  
# 

# 1. Handling Missing or Incomplete Data
df_no_null = df.drop_nulls()

df_impute = df.with_columns(
    pl.col('score').fill_null(pl.col('score').mean()),
    pl.col('course').fill_null('Unknown'),
    pl.col('date').forward_fill()
)

# 2. Formatting the data
date_formats = ['%Y-%m-%d', '%m-%d-%Y', '%Y/%m/%d']
df_format = df_impute.with_columns(
    pl.col('student').str.to_titlecase(),
    pl.coalesce(
        [pl.col('date').str.strptime(pl.Date, fmt, strict=False) for fmt in date_formats]
    ),
    pl.col('score').cast(pl.Int32),
    pl.col('course').str.to_titlecase()
)
df_format.head()

# 3. Transforming the Data
df_trans = pl.DataFrame({
    "student": ["Alice", "Bob", "Charlie", "David"],
    "math_score": [85, 70, 90, 60],
    "science_score": [88, 75, 85, 70]
})

df_trans = df_trans.with_columns(
    ((pl.col('math_score') + pl.col('science_score')) / 2).alias('average_score')
)

df_trans = df_trans.with_columns(
    (pl.col('average_score') / pl.col('average_score').max()).alias('normalized_score')
)
df_trans.head()
