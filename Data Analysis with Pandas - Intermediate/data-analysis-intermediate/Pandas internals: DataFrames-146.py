## 1. Shared index ##

import pandas as pd
fandango = pd.read_csv('fandango_score_comparison.csv')
print(fandango.index)
fandango.head()

## 2. Selecting using integer index ##

fandango = pd.read_csv('fandango_score_comparison.csv')
first_last = fandango.iloc[[fandango.index[0], fandango.index[-1]]]
print(first_last)

## 3. Custom Index ##

fandango = pd.read_csv('fandango_score_comparison.csv')
fandango_films = fandango.set_index('FILM', inplace=False, drop=False)

## 4. Selection using custom index ##

best_movies_ever = fandango_films.loc[["The Lazarus Effect (2015)", "Gett: The Trial of Viviane Amsalem (2015)", "Mr. Holmes (2015)"]]

## 5. Apply() over columns ##

import numpy as np

# returns the data types as a Series
types = fandango_films.dtypes
# filter data types to just floats, index attributes returns just column names
float_columns = types[types.values == 'float64'].index
# use bracket notation to filter columns to just float columns
float_df = fandango_films[float_columns]

# `x` is a Series object representing a column
deviations = float_df.apply(lambda x: np.std(x))

print(deviations)

## 6. Apply() over columns, practice ##

double_df = float_df.apply(lambda x: x*2)
print(double_df.head(1))
halved_df = float_df.apply(lambda x: x/2)
print(halved_df.head(1))

## 7. Apply() over rows ##

rt_mt_user = float_df[['RT_user_norm', 'Metacritic_user_nom']]
rt_mt_deviations = rt_mt_user.apply(lambda x: np.std(x), axis=1)
print(rt_mt_deviations[0:5])
rt_mt_means = rt_mt_user.apply(lambda x: np.mean(x), axis=1)
rt_mt_means.head()