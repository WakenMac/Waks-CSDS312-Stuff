# Author: Waken Maclang
# Purpose: To learn the basic Data Analysis techniques

import polars as pl
import pandas as pd
from plotnine import ggplot, aes, geom_point, geom_smooth, geom_bar, labs, theme_minimal

# [1] Importing and inspecting the data
diamonds = pl.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/diamonds.csv")
diamonds.head()
diamonds.shape
diamonds.columns

# [2] Finding patterns in the data

## Summary Statistics
diamonds.describe()

## Finding patterns (Price by cut)
(
    ggplot(data=diamonds.to_pandas()) +
    aes(x = 'cut', y='price') +
    geom_bar(stat='summary', fill='lightblue') +
    labs(
        title='Average diamond price by cut',
        x='Cut',
        y='Price'
    ) +
    theme_minimal()
)

# [3] Basic correlation using Polars
numeric_rows = ['carat', 'depth', 'table', 'price', 'x', 'y', 'z']
corr_matrix = diamonds.select(numeric_rows).to_pandas().corr()
print(corr_matrix)

"""
Based from the corr_matrix, we can determine the following:

Strong positive correlation : a increases, b increases
Strong negative correlation : a increases, b decreases

1. Carat has a strong positive correlation to a diamond's x, y, and z values. 
2. The higher the diamond's carat, the more expensive it is.
3. As x, y, and z each have a strong positive correlation with each other.
4. x, y, and z values are the ground indicators to a diamond's carat as well as its price.
"""

## Visualizing correlation (Carat and Price)
(
    ggplot(data=diamonds.to_pandas()) +
    aes(x = 'carat', y = 'price') +
    geom_point(alpha=0.3) + # alpha means opacity
    geom_smooth(method='lm', color='red') + 
    labs(
        title='Relationship between a diamond\'s price and carat',
        x='Carat',
        y='Price'
    ) + 
    theme_minimal()
)

## Visualizing correlation (Depth and Price)
(
    ggplot(data=diamonds.to_pandas()) +
    aes(x = 'depth', y = 'price') +
    geom_point(alpha=0.3, color='purple') + # alpha means opacity
    geom_smooth(method='lm', color='black') + 
    labs(
        title='Relationship between a diamond\'s depth and price',
        x='Depth',
        y='Price'
    ) + 
    theme_minimal()
)