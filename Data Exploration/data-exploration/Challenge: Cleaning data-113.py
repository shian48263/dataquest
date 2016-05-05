## 3. Exploring the data ##

import pandas as pd

avengers = pd.read_csv("avengers.csv")
avengers.head(5)

## 4. Filter out the bad years ##

import matplotlib.pyplot as plt
%matplotlib inline
true_avengers = pd.DataFrame()

avengers['Year'].hist()
true_avengers = avengers[avengers['Year'] >= 1960]

## 5. Consolidating deaths ##

columns = ['Death1', 'Death2', 'Death3', 'Death4', 'Death5']
true_avengers[columns]
deaths = ['Death1', 'Death2', 'Death3', 'Death4', 'Death5']
def count_deaths(row):
  count = 0
  for death in deaths:
    if row[death] == 'YES':
      count += 1;
  return(count)
true_avengers['Deaths'] = true_avengers.apply(lambda row: count_deaths(row), axis=1)

## 6. Years since joining ##

import numpy as np
joined_accuracy_count  = int()
joined_accuracy_count = 0
for i, row in true_avengers[['Years since joining', 'Year']].iterrows():
  if ~np.isnan(row['Year']) or ~np.isnan(row['Years since joining']):
    years_joined = 2015 - int(row['Year'])
    if years_joined == row['Years since joining']:
      joined_accuracy_count += 1