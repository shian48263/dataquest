## 2. Introduction to the data ##

import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline

admissions = pd.read_csv('admissions.csv')
plt.scatter(admissions['gpa'], admissions['admit'])
plt.show()

## 4. Logit function ##

import numpy as np

# Logit Function
def logit(x):
    # np.exp(x) raises x to the exponential power, ie e^x. e ~= 2.71828
    return np.exp(x)  / (1 + np.exp(x)) 
    
# Generate 50 real values, evenly spaced, between -6 and 6.
x = np.linspace(-6,6,50, dtype=float)

# Transform each number in t using the logit function.
y = logit(x)

# Plot the resulting data.
plt.plot(x, y)
plt.ylabel("Probability")
plt.show()

## 5. Training a logistic regression model ##

from sklearn.linear_model import LinearRegression
linear_model = LinearRegression()
linear_model.fit(admissions[["gpa"]], admissions["admit"])

from sklearn.linear_model import LogisticRegression
logistic_model = LogisticRegression()
logistic_model.fit(admissions[['gpa']], admissions['admit'])

## 6. Plotting probabilities ##

logistic_model = LogisticRegression()
logistic_model.fit(admissions[["gpa"]].values, admissions["admit"])

pred_probs = logistic_model.predict_proba(admissions[['gpa']])
print(pred_probs)

import matplotlib.pyplot as plt
%matplotlib inline

plt.scatter(admissions['gpa'], pred_probs[:,1])
plt.show()

## 7. Predict labels ##

logistic_model = LogisticRegression()
logistic_model.fit(admissions[["gpa"]].values, admissions["admit"])

fitted_labels = logistic_model.predict(admissions[['gpa']])
print(fitted_labels[:10])

import matplotlib.pyplot as plt
%matplotlib inline

plt.scatter(admissions['gpa'], fitted_labels)
plt.show()