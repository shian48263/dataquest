## 1. Introduction to the Data ##

import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline
from sklearn.linear_model import LogisticRegression

admissions = pd.read_csv("admissions.csv")

model = LogisticRegression()
model.fit(admissions[["gpa"]].values, admissions["admit"])

labels = model.predict(admissions[['gpa']])
admissions['predicted_label'] = labels
print(admissions['predicted_label'].value_counts())
print(admissions.head())

## 2. Accuracy ##

labels = model.predict(admissions[["gpa"]].values)
admissions["predicted_label"] = labels

admissions['actual_label'] = admissions['admit']
matches = admissions['actual_label'] == admissions['predicted_label']
correct_predictions = admissions[matches]
accuracy = correct_predictions.shape[0] / admissions.shape[0]
print(accuracy)

## 3. Binary classification outcomes ##

true_positives = sum((admissions['actual_label'] == 1) & (admissions['predicted_label'] == 1))
true_negatives = sum((admissions['actual_label'] == 0) & (admissions['predicted_label'] == 0))
print(true_positives, true_negatives)

## 4. Sensitivity ##

# From the previous screen
true_positive_filter = (admissions["predicted_label"] == 1) & (admissions["actual_label"] == 1)
true_positives = len(admissions[true_positive_filter])

false_negative_filter = (admissions["predicted_label"] == 0) & (admissions["actual_label"] == 1)
false_negatives = len(admissions[false_negative_filter])

sensitivity = true_positives / (true_positives + false_negatives)
print(sensitivity)

## 5. Specificity ##

# From previous screens
true_positive_filter = (admissions["predicted_label"] == 1) & (admissions["actual_label"] == 1)
true_positives = len(admissions[true_positive_filter])
false_negative_filter = (admissions["predicted_label"] == 0) & (admissions["actual_label"] == 1)
false_negatives = len(admissions[false_negative_filter])
true_negative_filter = (admissions["predicted_label"] == 0) & (admissions["actual_label"] == 0)
true_negatives = len(admissions[true_negative_filter])

false_positive_filter = (admissions["predicted_label"] == 1) & (admissions["actual_label"] == 0)
false_positives = len(admissions[false_positive_filter])

specificity = true_negatives / (true_negatives + false_positives)
print(specificity)