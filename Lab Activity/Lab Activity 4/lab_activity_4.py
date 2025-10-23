#   Waken Cean C. Maclang
#   BSCS 3A
#   CSDS 312: Lab Activity 4

# ==================================================================================================
# Exercise 1: Handling Missing Data

import polars as pl
from plotnine import ggplot, aes, geom_bar, geom_point, labs, scale_fill_manual, theme_classic

df1 = pl.DataFrame({
    "student": ["Alice", "Bob", "Charlie", "David", "Eva"],
    "math_score": [85, None, 90, 72, None],
    "science_score": [88, 75, None, None, 80],
    "course": ["Math", "Math", "Science", None, "Science"]
})

print(df1)

# Task 1: Drop all rows with null values
df1_drop = df1.drop_nulls()

# Task 2: Fill null values in the math_score column with its mean
df1_mean = df1.with_columns(
    pl.col('math_score').fill_null(value=pl.col('math_score').mean())
)

# Task 3: Fill null values in the science_score column with its median
df1_median = df1.with_columns(
    pl.col('science_score').fill_null(value=pl.col('science_score').median())
)

# Task 4: Fill null values in the columns column with 'Unknown'
df1_course = df1.with_columns(
    pl.col('course').fill_null(value='Unknown')
)

print(df1_drop)
print(df1_mean)
print(df1_median)
print(df1_course)

# ==================================================================================================
# Exercise 2: Formatting Data

df2 = pl.DataFrame({
    "id": ["001", "002", "003", "004"],
    "date": ["2025-01-01", "2025/01/02", "01-03-2025", "2025.01.04"],
    "grade": ["85", "90", "88", "92"],
    "course": ["math", "Math", "MATH", "sci"]
})

print(df2)

# Task 1: Convert the ID into integers
# Task 2: Convert date into a proper date format.
# Task 3: Convert grade into integers.
# Task 4: Standardize course names so "math", "Math", and "MATH" all become "math".

date_formats = [
    '%Y-%m-%d',
    '%Y/%m/%d',
    '%d-%m-%Y',
    '%Y.%m.%d'
]

df2_formatted = df2.with_columns(
    pl.col('id').cast(pl.Int32),
    pl.coalesce([pl.col('date').str.strptime(pl.Date, fmt, strict=False) for fmt in date_formats]).alias('date'),
    pl.col('grade').cast(pl.Int32),
    pl.col('course').str.to_lowercase()
)

print(df2_formatted)

# ==================================================================================================
# Transforming Data

df3 = pl.DataFrame({
    "student": ["Alice", "Bob", "Charlie", "David"],
    "math_score": [85, 70, 90, 60],
    "science_score": [88, 75, 85, 70],
    "english_score": [82, 65, 78, 72]
})

print(df3)

# Task 1: Create a new column avg_score as the average of the three subjects.
df3_trans = df3.with_columns(
    ((pl.col('math_score') + pl.col('science_score') + pl.col('english_score')) / 3).alias('avg_score')
)

# Task 2: Create a normalized version of avg_score between 0–1
df3_trans = df3_trans.with_columns(
    ((pl.col('avg_score') / pl.col('avg_score').max())).alias('normalized_score')
)

# Task 3: Create a new categorical column status: (`"Pass"` if `avg_score >= 75`) `"Fail"` otherwise
df3_trans = df3_trans.with_columns(
    pl.when(pl.col('avg_score') >= 75)
    .then(pl.lit('Pass'))
    .otherwise(pl.lit('Fail'))
    .alias('Status')
)

print(df3_trans)

# ==================================================================================================
# Exercise 4: Visualization of Cleaned Data

# Task 1: Create a bar chart of average scores by student
plot1 = ggplot(df3_trans, aes(x='student', y='avg_score')) + \
    geom_bar(stat='identity', fill='#4285F4') + \
    labs(
        title='Average Score per Student',
        x='Student',
        y='Average Score'
    ) + \
    theme_classic()
plot1

# Task 2: Create a scatter plot comparing math_score and science_score
plot2 = ggplot(df3_trans, aes(x='math_score', y='science_score')) + \
    geom_point() + \
    labs(
        title='Scatterplot of Math and Science Scores',
        x='Math Score',
        y='Science Score'
    ) + \
    theme_classic()
plot2

# Create a bar chart showing the number of students who "Pass" vs "Fail".
plot3 = ggplot(df3_trans, aes(x='Status', fill='Status')) + \
    geom_bar() + \
    scale_fill_manual(values={'Pass': '#008000', 'Fail': '#FF0000'}) + \
    labs(
        title='Frequency Distribution of students who Passed or Failed',
        x='Pass or Fail',
        y = 'Frequency'
    ) + \
    theme_classic()
plot3
