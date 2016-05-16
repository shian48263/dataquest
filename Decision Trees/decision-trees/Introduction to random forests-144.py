## 2. Ensemble models ##

from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import roc_auc_score

columns = ["age", "workclass", "education_num", "marital_status", "occupation", "relationship", "race", "sex", "hours_per_week", "native_country"]

clf = DecisionTreeClassifier(random_state=1, min_samples_leaf=75)
clf.fit(train[columns], train["high_income"])

clf2 = DecisionTreeClassifier(random_state=1, max_depth=6)
clf2.fit(train[columns], train["high_income"])

clf_predictions = clf.predict(test[columns])
clf2_predictions = clf2.predict(test[columns])

clf_auc = roc_auc_score(clf_predictions, test['high_income'])
clf2_auc = roc_auc_score(clf2_predictions, test['high_income'])

print(clf_auc, clf2_auc)

## 3. Combining our predictions ##

predictions = clf.predict_proba(test[columns])[:,1]
predictions2 = clf2.predict_proba(test[columns])[:,1]

print(predictions, predictions2)

import numpy as np

ensembled_predictions = np.round((predictions + predictions2) / 2)
ensembled_auc = roc_auc_score(ensembled_predictions, test['high_income'])

print(ensembled_predictions, ensembled_auc)

## 5. Bagging ##

# We'll build 10 trees
tree_count = 10

# Each "bag" will have 60% of the number of original rows.
bag_proportion = .6

predictions = []
for i in range(tree_count):
    # We select 60% of the rows from train, sampling with replacement.
    # We set a random state to ensure we'll be able to replicate our results.
    # We set it to i instead of a fixed value so we don't get the same sample every loop.
    # That would make all of our trees the same.
    bag = train.sample(frac=bag_proportion, replace=True, random_state=i)
    
    # Fit a decision tree model to the "bag".
    clf = DecisionTreeClassifier(random_state=1, min_samples_leaf=75)
    clf.fit(bag[columns], bag["high_income"])
    
    # Using the model, make predictions on the test data.
    predictions.append(clf.predict_proba(test[columns])[:,1])

import numpy as np

predictions_mean = np.round(np.sum(predictions, axis=0) / tree_count)
auc_mean = roc_auc_score(predictions_mean, test['high_income'])
print(auc_mean)

## 6. Selecting random features ##

# Create the dataset that we used 2 missions ago.
data = pandas.DataFrame([
    [0,4,20,0],
    [0,4,60,2],
    [0,5,40,1],
    [1,4,25,1],
    [1,5,35,2],
    [1,5,55,1]
    ])
data.columns = ["high_income", "employment", "age", "marital_status"]

# Set a random seed to make results reproducible.
numpy.random.seed(1)

# The dictionary to store our tree.
tree = {}
nodes = []

# The function to find the column to split on.
def find_best_column(data, target_name, columns):
    information_gains = []
    
    # Insert your code here.
    
    for col in columns:
        information_gain = calc_information_gain(data, col, "high_income")
        information_gains.append(information_gain)

    # Find the name of the column with the highest gain.
    highest_gain_index = information_gains.index(max(information_gains))
    highest_gain = columns[highest_gain_index]
    return highest_gain

# The function to construct an id3 decision tree.
def id3(data, target, columns, tree):
    unique_targets = pandas.unique(data[target])
    nodes.append(len(nodes) + 1)
    tree["number"] = nodes[-1]

    if len(unique_targets) == 1:
        if 0 in unique_targets:
            tree["label"] = 0
        elif 1 in unique_targets:
            tree["label"] = 1
        return
    
    best_column = find_best_column(data, target, columns)
    column_median = data[best_column].median()
    
    tree["column"] = best_column
    tree["median"] = column_median
    
    left_split = data[data[best_column] <= column_median]
    right_split = data[data[best_column] > column_median]
    split_dict = [["left", left_split], ["right", right_split]]
    
    for name, split in split_dict:
        tree[name] = {}
        id3(split, target, columns, tree[name])


# Run the id3 algorithm on our dataset and print the resulting tree.
id3(data, "high_income", ["employment", "age", "marital_status"], tree)
print(tree)

import numpy as np

def find_best_column(data, target_name, columns):
    information_gains = []
    
    cols = np.random.choice(columns, 2)
    
    for col in cols:
        information_gain = calc_information_gain(data, col, "high_income")
        information_gains.append(information_gain)

    highest_gain_index = information_gains.index(max(information_gains))
    highest_gain = cols[highest_gain_index]
    return highest_gain
    
id3(data, "high_income", ["employment", "age", "marital_status"], tree)
print(tree)

## 7. Random subsets in scikit-learn ##

# We'll build 10 trees
tree_count = 10

# Each "bag" will have 70% of the number of original rows.
bag_proportion = .7

predictions = []
for i in range(tree_count):
    # We select 80% of the rows from train, sampling with replacement.
    # We set a random state to ensure we'll be able to replicate our results.
    # We set it to i instead of a fixed value so we don't get the same sample every time.
    bag = train.sample(frac=bag_proportion, replace=True, random_state=i)
    
    # Fit a decision tree model to the "bag".
    clf = DecisionTreeClassifier(random_state=1, min_samples_leaf=75)
    clf.fit(bag[columns], bag["high_income"])
    
    # Using the model, make predictions on the test data.
    predictions.append(clf.predict_proba(test[columns])[:,1])

combined = numpy.sum(predictions, axis=0) / 10
rounded = numpy.round(combined)

print(roc_auc_score(rounded, test["high_income"]))

tree_count = 10

bag_proportion = .7

predictions = []
for i in range(tree_count):
    bag = train.sample(frac=bag_proportion, replace=True, random_state=i)
    
    clf = DecisionTreeClassifier(random_state=1, min_samples_leaf=75, splitter='random', max_features='auto')
    clf.fit(bag[columns], bag["high_income"])
    
    predictions.append(clf.predict_proba(test[columns])[:,1])

combined = numpy.sum(predictions, axis=0) / 10
rounded = numpy.round(combined)

print(roc_auc_score(rounded, test["high_income"]))

## 8. Putting it all together ##

from sklearn.ensemble import RandomForestClassifier

clf = RandomForestClassifier(n_estimators=10, random_state=1, min_samples_leaf=75)

clf.fit(train[columns], train['high_income'])

predictions = clf.predict(test[columns])

auc = roc_auc_score(predictions, test['high_income'])
print(auc)

## 9. Parameter tweaking ##

from sklearn.ensemble import RandomForestClassifier

clf = RandomForestClassifier(n_estimators=10, random_state=1, min_samples_leaf=75)

clf.fit(train[columns], train["high_income"])

predictions = clf.predict(test[columns])
print(roc_auc_score(predictions, test["high_income"]))

clf = RandomForestClassifier(n_estimators=150, random_state=1, min_samples_leaf=75)

clf.fit(train[columns], train["high_income"])

predictions = clf.predict(test[columns])
print(roc_auc_score(predictions, test["high_income"]))

## 10. Reducing overfitting ##

clf = DecisionTreeClassifier(random_state=1, min_samples_leaf=75)

clf.fit(train[columns], train["high_income"])

predictions = clf.predict(train[columns])
print(roc_auc_score(predictions, train["high_income"]))

predictions = clf.predict(test[columns])
print(roc_auc_score(predictions, test["high_income"]))

clf = RandomForestClassifier(n_estimators=150, random_state=1, min_samples_leaf=75)

clf.fit(train[columns], train["high_income"])

predictions = clf.predict(train[columns])
print(roc_auc_score(predictions, train["high_income"]))

predictions = clf.predict(test[columns])
print(roc_auc_score(predictions, test["high_income"]))