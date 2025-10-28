# Author: Waken Cean C. Maclang
# Course: BSCSDS 3A
# October 28, 2025
# CSDS 312 - Lab Activity 5

# You can find the same/updated file on this link: https://github.com/WakenMac/Waks-CSDS312-Stuff/tree/main/Lab%20Activity/Lab%20Activity%205

# The following packages are needed.
# !pip install kagglehub polars pandas plotnine

import kagglehub
import os
import polars as pl
import pandas as pd
from plotnine import ggplot, aes, geom_point, geom_smooth, geom_bar, facet_wrap, labs, theme_minimal

# Activity #1 Pattern Detection
# Using the same dataset, find which color of diamond has the highest average price.

## Importing the dataset
diamonds = pl.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/diamonds.csv")

## Summarization with Polars
diamonds_color = (diamonds.select(['color', 'price'])
                    .group_by('color')
                    .agg(pl.col('price').mean().alias('mean_price'))
                    .sort('mean_price', descending=True))
print(diamonds_color)

## Visualize using plotnine
## Note: Requires the diamonds_color variable.
(
    ggplot(data=diamonds_color) +
    aes(x='color', y='mean_price') +
    geom_bar(stat='identity', fill='blue') +
    labs(
        title='A diamond\'s average price per color',
        x='Color',
        y='Price'
    ) +
    theme_minimal()
)

# Activity 3 : Correlation Analysis
numeric_rows = ['carat', 'depth', 'table', 'price', 'x', 'y', 'z']
corr_matrix = diamonds.select(numeric_rows).to_pandas().corr()

## Which variable has the strongest positive correlation with price?
price_corrs = corr_matrix.iloc[3, :].sort_values(ascending=False)
print(price_corrs)

"""
As seen in the recent print out of price and its correlation to all variables,
aside from Price, Carat is the second variable with the strongest positive correlation.
"""

## Which variable has the weakest correlation?

## If we were to interpret "weakest" as the most negative correlated variables in the dataset:

## Correlations across depth are seen to have the weakest correlation
corr_matrix[corr_matrix < 0]
depth = corr_matrix["depth"].sort_values(ascending=True)
print(f'The variables with the weakest correlation between "depth" and "{depth.index[0]}" with a correlation of: {depth.iat[0]}')

# Activity 3 : Visualization Challenge
# Plot a scatter plot showing the relationship betwene x (length) and price

"""
[1] Add a smooth line

While plotting, I noticed that there are entries on the graph where the x 
or length value is 0, so this may affect the way our linear regression line is formed.
"""

(
    ggplot(data=diamonds.to_pandas()) +
    aes(x='x', y='price') + 
    geom_point(alpha=0.3, color='green') +
    geom_smooth(method='lm', color='black') +
    labs(
        title='Correlation between a Diamond\'s x (length) and price',
        x='x (length)',
        y='Price'
    ) +
    theme_minimal()
)

diamonds.select(['price', 'x']).filter(pl.col('x') < 1).shape[0]
print(f'Corr of Price and x (Length): {diamonds.select(numeric_rows).to_pandas().corr()["x"].loc["price"]}')

""" 
Interpret the result:

Price and x (length) has a corr value of 0.88, indicating their strong positive correlation.
This means that as the x's value increases, the price strongly increases and the same applies in vice-versa

However, given the distribution of points in our previous graph, there exists 8 entries whose lenth is 0, thus requires cleaning.
Similarly, the distribution of points resembles that of an exponential relationship rather than that of a
linear one, thus for diamonds of higher lengths may cause the correlation coefficient to be smaller.
"""

# Activity 4 : Kaggle Challenge
# Choose a dataset from kaggle

"""
Dataset Chosen:     Energy Efficiency Dataset
Taken from:         https://www.kaggle.com/datasets/elikplim/eergy-efficiency-dataset?resource=download

Details:            It is a dataset consisting of 768 rows where each row represents a building design parameters (inputs) 
                    and their resulting energy performance (outputs) or the energy needed to maintain comfortable indoor 
                    temperatures. The dataset was generated from EnergyPlus, a software used to simulate heating and 
                    cooling load demands of residential buildings. 
                    
                    The dataset contains the following input and output features.
                    Input: 'relative_compactness', 'surface_area', 'wall_area', 'roof_area', 'overall_height',
                           'orientation', 'glazing_area', and 'glazing_area_distribution' (originally named X1 to
                            X8 in the csv file.)
                    Output: heating_laod and cooling_load (originally named Y1 & Y2 in the csv file.)

                    Thus, this dataset shall be used to see which variables/inputs have a greater effect to our outputs
                    (e.g., heating_load and cooling_load), and the patterns hidden among them.

Feature Definition: X1 relative_compactness         Ratio of a building's volume to its surface area (High compactness
                                                    means lower heating/cooling load)    
                    X2 surface_area                 Exterior surface area of the building
                    X3 wall_area                    Total area of exterior walls
                    X4 roof_area                    Total area of roof
                    X5 overall_height               Height of the building
                    X6 orientation                  Cardinal orientation of the building (2, 3, 4, 5 for North, East, 
                                                    South, and West respectively). It is the place where the main 
                                                    entrance of a building is facing (i.e., a house with its entrance
                                                    placed North is called a 'north-facing house' with its orientation
                                                    as 2, for North).
                    X7 glazing_area                 Fraction of wall area covered by windows (Windows conduct more
                                                    heat than walls)
                    X8 glazing_area_distribution    Where glazing windows are detected.
                                                    (0 - none, 1 - uniform, 2 to 5 is for N, E, S, and W)
                    Y1 heating_load                 Energy required for heating
                    Y2 cooling_load                 Energy required for cooling

How to Import:      I designed a small program that allows you to either [1] download the dataset automatically, or 
                    [2] import the csv by pasting the path of the dataset in your machine. I left a comment on a code
                    line that indicates whether you would want to do option [1] or [2].
"""


## Download and import the dataset
path = kagglehub.dataset_download("elikplim/eergy-efficiency-dataset")
print("Path to dataset files:", path)

eed = pl.DataFrame()
file_prepared = False

import_manually = False   # Annotate this code to manually upload the dataset.

if not import_manually:
    for file in os.listdir(path):
        if file == 'ENB2012_data.csv':
            eed = pl.read_csv(os.path.join(path, file))
            file_prepared = True
        else:
            print(f'Expected csv file was not found in {path}.')
else:
    try:
        path_to_dataset = 'path/to/dataset'
        eed = pl.read_csv(path_to_dataset)
        file_prepared = True
    except FileNotFoundError:
        print(f'File path: {path}, did not lead to a csv file. The expected file name must be \'ENB2012_data.csv\'')
        file_prepared = False

if not file_prepared:
    print('The Energy Efficiency Dataset was not downlodaded successfully. Try downlodading it via (https://www.kaggle.com/datasets/elikplim/eergy-efficiency-dataset?resource=download) then import it.')
else:
    # Preparing the dataset
    eed.columns = ['relative_compactness', 'surface_area', 'wall_area', 'roof_area', 'overall_height', 'orientation',
                        'glazing_area', 'glazing_area_distribution', 'heating_load', 'cooling_load']
    eed = eed.with_columns(pl.col('orientation').cast(pl.Int16))
    eed_long = eed.melt(
        id_vars=eed.columns[0:-2],
        value_vars=["heating_load", "cooling_load"],
        variable_name="load_type",
        value_name="load_value"
    )
    eed.columns
    eed.head()

    
    # [1] Identify at least 2 patterns in the data.
    eed_wall_area = pl.concat(
        [eed.sort('wall_area', descending=True).select(['wall_area', 'heating_load', 'cooling_load'])[:12, :],
        eed.sort('wall_area', descending=False).select(['wall_area', 'heating_load', 'cooling_load'])[:12, :]],
        how='vertical'
    )
    eed_wall_area

    eed_surface_area = pl.concat(
        [eed.sort('surface_area', descending=True).select(['surface_area', 'heating_load', 'cooling_load'])[:12, :],
        eed.sort('surface_area', descending=False).select(['surface_area', 'heating_load', 'cooling_load'])[:12, :]],
        how='vertical'
    )
    eed_surface_area
    
    eed_roof_area = pl.concat(
        [eed.sort('roof_area', descending=True).select(['roof_area', 'heating_load', 'cooling_load'])[:12, :],
        eed.sort('roof_area', descending=False).select(['roof_area', 'heating_load', 'cooling_load'])[:12, :]],
        how='vertical'
    )
    eed_roof_area


    """
    After playing around with the input and output features, we found the following.
        [1] Roof Area and Surface Area area are directly proportional to the heating and cooling load
        [2] Wall Area is directly proportional to the heating and cooling load
    """

    # [2] Perform Correlation Analysis
    eed_corr_matrix = eed.to_pandas().corr()
    print(eed_corr_matrix[['heating_load', 'cooling_load']])

    """
    After running correlation analysis, we can support the patterns we found earlier.
        [1] Roof Area and Surface Area are negatively correlated to our output vars.
        [2] Wall Area, Overall Height, and Relative Compactness are strongly correlated to our output vars.
        [3] Orientation and Glazing Area Distribution have weak correlation to our output vars.
        [4] Heating and Cooling loads have a strong positive correlation with each other.
    """

    # [3] Create at least 2 visualizations using plotnine.
    (
        ggplot(data=eed)
        + aes(x = 'surface_area')
        + geom_bar(aes(y='heating_load'), stat='summary', fill='red', alpha=0.5)
        + geom_bar(aes(y='cooling_load'), stat='summary', fill='lightblue', alpha=0.5)
        + labs(
            title='Effect of Surface Area on Heating and Cooling Load',
            x='Surface Area',
            y='Load',
            fill=['heating_load', 'cooling_load'] 
        )
        + theme_minimal()
    )

    (
        ggplot(eed_long)
        + aes(x='surface_area', y='load_value', color='load_type')
        + geom_point(alpha=0.5)
        + facet_wrap('~load_type')
        + geom_smooth(method='lm', color='red')
        + labs(
            title='Effect of Surface Area on Heating and Cooling Load',
            x='Surface Area',
            y='Load',
            color='Load Type'
        )
    )

    (
        ggplot(eed_long)
        + aes(x='wall_area', y='load_value', color='load_type')
        + geom_point(alpha=0.5)
        + facet_wrap('~load_type')
        + geom_smooth(method='lm', color='red')
        + labs(
            title='Effect of Wall Area on Heating and Cooling Load',
            x='Surface Area',
            y='Load',
            color='Load Type'
        )
    )

    
    (    
        ggplot(eed_long)
        + aes(x='roof_area', y='load_value', color='load_type')
        + geom_point(alpha=0.5)
        + facet_wrap('~load_type')
        + geom_smooth(method='lm', color='red')
        + labs(
            title='Effect of Roof Area on Heating and Cooling Load',
            x='Surface Area',
            y='Load',
            color='Load Type'
        )
    )

    (
        ggplot(eed)
        + aes(x='heating_load', y='cooling_load')
        + geom_point(alpha=0.5, color='teal')
        + geom_smooth(method='lm', color='red')
    )


    # [4] Write a short interpretation (3-5 sentences).
    """
    After analyzing the variables between the Energy Efficiency Dataset, we can derrive that our input variables have
    no correlation with each other. Whereas, correlations among certain input variables and our output variables, 
    such as relative_compactness, wall_area, and overall_height have a positive correlation, while surface_area and 
    roof_area have a strong negative correlation. 

    However, there exist columns with repetetive records such as: roof_area, overall_height, and orientation, which
    affect the correlations among heating and cooling loads due them having being concentrated in terms of room_area,
    overall_height, etc. but are dispersed in terms of energy usage, causing misinterpreted correlations among
    variables (Expected Low MAE, MSAE, and R^2 score).

    Overall, our input variables can be used as determinants for the two loads, but should be used with caution
    especially for columns with less dispersed data, and is suggested to instead predict loads with all 
    input variables due to their independency (based on the corr_matrix) and may have patterns that 
    better predict heating and cooling loads.
    """

