import pandas as pd

dictionary = {'Name':('Waks', 'Mars', 'Allan'), 
             'Age':(18, 20, 21),
             'Average':(1.59, 1.51, 1.4)}

my_other_dictionary = {'Name':('Cap', 'Jeff', 'Dave'),
                      'Age':(19, 20, 19),
                      'Average':(1.4, 1.4, 1.59)}

def to_dataframe(*dataset: dict, axis = 0):
    dataframes = []
    for data in dataset:
        dataframes.append(pd.DataFrame(data))
    return pd.concat(dataframes, axis=axis, ignore_index=True)


dataset = to_dataframe(dictionary, my_other_dictionary)
print(dataset.head(6))