import polars as pl

# Dropping values / Imputation

# Sample dataset with missing values
df = pl.DataFrame({
    "student": ["Alice", "Bob", "Charlie", "David"],
    "score": [85, None, 90, None],
    "course": ["Math", "Math", "Science", None]
})

print("Original DataFrame:")
print(df)

# Drop rows with missing values
df_drop = df.drop_nulls()
print("\nAfter dropping missing values:")
print(df_drop)

# Fill missing numerical values with mean
df_fill_mean = df.with_columns(
    df["score"].fill_null(df["score"].mean())
)

# Fill missing categorical values with a constant
df_fill_course = df.with_columns(
    df["course"].fill_null("Unknown")
)

print("\nAfter filling missing values:")
print(df_fill_mean)
print(df_fill_course)

# ================================================================================================
# Formatting Data

df_format = pl.DataFrame({
    "date": ["2025-01-01", "2025/01/02", "01-03-2025"],
    "grade": ["85", "90", "88"],
    "course": ["math", "Math", "MATH"]
})

df_format = df_format.with_columns(
    pl.col('date').str.strptime(pl.Date, '%Y-%m-%d', strict=False),
    pl.col('grade').cast(pl.Int32),
    pl.col('course').str.to_titlecase()
)

# ================================================================================================
# Transforming the data

df_trans = pl.DataFrame({
    "student": ["Alice", "Bob", "Charlie", "David"],
    "math_score": [85, 70, 90, 60],
    "science_score": [88, 75, 85, 70]
})

df_trans = df_trans.with_columns(
    ((pl.col('math_score') + pl.col('science_score')) / 2).alias('avg_score')
)

df_trans = df_trans.with_columns(
    (pl.col('avg_score') / pl.col('avg_score').max()).alias('normalized_score')
)
