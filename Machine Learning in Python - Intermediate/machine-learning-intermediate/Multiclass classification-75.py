## 1. Introduction to the Auto Dataset ##

import pandas
import numpy as np

# Filename
auto_file = "auto.txt"

# Column names, not included in file
names = ['mpg', 'cylinders', 'displacement', 'horsepower', 'weight', 'acceleration', 
         'year', 'origin', 'car_name']

# Read in file 
# Delimited by an arbitrary number of whitespaces 
auto = pandas.read_table(auto_file, delim_whitespace=True, names=names)

# Show the first 5 rows of the dataset
print(auto.head())

unique_regions = auto['origin'].unique()
print(unique_regions)

## 2. Clean Dataset ##

# The Dataframe auto is in memory

# Delete the column car_name
del auto["car_name"]

auto = auto[auto['horsepower'] != '?']
print(auto.head())

## 4. Using Dummy Variables ##

# input a column with categorical variables
def create_dummies(var):
    # get the unique values in var and sort
    var_unique = var.unique()
    var_unique.sort()
    
    # Initialize a dummy DataFrame to store variables
    dummy = pandas.DataFrame()
    
    # loop through all but the last value
    for val in var_unique[:-1]:
        # which columns are equal to our unique value
        d = var == val
        
        # make a new column with a dummy variable
        dummy[var.name + "_" + str(val)] = d.astype(int)
    
    # return dataframe with our dummy variables
    return(dummy)

# lets make a copy of our auto dataframe to modify with dummy variables
modified_auto = auto.copy()

# make dummy variables from the cylinder categories
cylinder_dummies = create_dummies(modified_auto["cylinders"])

# merge dummy variables to our dataframe
modified_auto = pandas.concat([modified_auto, cylinder_dummies], axis=1)

# delete cylinders column as we have now explained it with dummy variables
del modified_auto["cylinders"]

print(modified_auto.head())

year_dummies = create_dummies(modified_auto['year'])
modified_auto = pandas.concat([modified_auto, year_dummies], axis=1)
del modified_auto['year']
print(modified_auto.head())

## 5. Multiclass Classification ##

# get all columns which will be used as features, remove 'origin'
features = np.delete(modified_auto.columns, modified_auto.columns == 'origin')

# shuffle data
shuffled_rows = np.random.permutation(modified_auto.index)

# Select 70% of the dataset to be training data
highest_train_row = int(modified_auto.shape[0] * .70)

train = modified_auto.loc[shuffled_rows[:highest_train_row]]
test = modified_auto.loc[shuffled_rows[highest_train_row:]]
print(train.head(), test.head())

## 6. Training a Multiclass Logistic Regression ##

from sklearn.linear_model import LogisticRegression

# find the unique origins
unique_origins = modified_auto["origin"].unique()
unique_origins.sort()

# dictionary to store models
models = {}

for origin in unique_origins:
    # initialize model to dictionary
    models[origin] = LogisticRegression()
    
    # select columns for predictors and predictands
    X_train = train[features]
    y_train = train["origin"] == origin
        
    # fit model with training data
    models[origin].fit(X_train, y_train)

# Dataframe to collect testing probabilities
testing_probs = pandas.DataFrame(columns=unique_origins)

print(unique_origins, models)

for i in models:
    x_axis = test[features]
    testing_probs[i] = models[i].predict_proba(x_axis)[:,1]

print(testing_probs)

## 7. Choose the Origin ##

# Variable testing_probs is in memory

predicted_origins = testing_probs.idxmax(axis=1)
print(predicted_origins)

## 8. Confusion Matrix ##

# Remove pandas indicies
predicted_origins = predicted_origins.values
origins_observed = test['origin'].values

# fill in this confusion matrix
confusion = pandas.DataFrame(np.zeros(shape=(unique_origins.shape[0], unique_origins.shape[0])), index=unique_origins, columns=unique_origins)

print(confusion)

for i, j in confusion.iterrows():
    for x, y in j.iteritems():
        confusion.loc[i, x] = sum((predicted_origins == i) & (origins_observed == x))

print(confusion)

## 9. Confusion Matrix Cont. ##

#Variable confusion is in memory

fp1 = confusion.loc[[2,3],1].sum()
print(fp1)

## 10. Average Accuracy ##

# The confusion DataFrame is in memory

print(confusion)

avgacc_list = []
for i, j in confusion.iterrows():
    avgacc_list.append(j[i] / j.sum())

avgacc = sum(avgacc_list) / len(avgacc_list)
print(avgacc)

## 11. Precision and Recall ##

# Variable to add all precisions
ps = 0
# Loop through each origin (class)
for j in confusion.index:
    # True positives
    tps = confusion.ix[j,j]
    # Positively predicted for that origin 
    positives = confusion.ix[j,:].sum()
    # Add to precision
    ps += tps/positives

# divide ps by the number of classes to get precision 
precision = ps/confusion.shape[0]
print('Precision = {0}'.format(precision))

rs = 0
for i, j in confusion.iteritems():
    tps = confusion.loc[i,i]
    tps_fns = confusion.loc[:,i].sum()
    rs += tps / tps_fns
recall = rs / confusion.shape[1]
print('Recall = {0}'.format(recall))

## 12. F-Score ##

# Confusion DataFrame is in memory

ps = []
for j in confusion.index:
    tps = confusion.ix[j,j]
    positives = confusion.ix[j,:].sum()
    ps.append(tps/positives)

rs = []
for i, j in confusion.iteritems():
    tps = confusion.loc[i,i]
    tps_fns = confusion.loc[:,i].sum()
    rs.append(tps / tps_fns)

fs = 0
for i, e in confusion.iteritems():
    fs += (2 * ps[i-1] * rs[i-1]) / (ps[i-1] + rs[i-1])
fscore = fs/confusion.shape[0]
print(fscore)

## 13. Metrics with Sklearn ##

# Import metric functions from sklearn
from sklearn.metrics import precision_score, recall_score, f1_score

# Compute precision score with micro averaging
pr_micro = precision_score(test["origin"], predicted_origins, average='micro')
print(pr_micro)

pr_weighted = precision_score(test['origin'], predicted_origins, average='weighted')
rc_weighted = recall_score(test['origin'], predicted_origins, average='weighted')
f_weighted = f1_score(test['origin'], predicted_origins, average='weighted')

print(pr_weighted, rc_weighted, f_weighted)