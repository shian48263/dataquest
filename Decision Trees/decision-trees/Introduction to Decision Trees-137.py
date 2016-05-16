## 2. Our dataset ##

import pandas

# Set index_col to False to avoid pandas thinking that the first column is row indexes (it's age).
income = pandas.read_csv("income.csv", index_col=False)
print(income.head(5))

## 3. Converting categorical variables ##

# Convert a single column from text categories into numbers.
col = pandas.Categorical.from_array(income["workclass"])
income["workclass"] = col.codes
print(income["workclass"].head(5))

cols = ['education', 'marital_status', 'occupation', 'relationship', 'race', 'sex', 'native_country', 'high_income']
for c in cols:
    income[c] = pandas.Categorical.from_array(income[c]).codes

print(income.head())

## 5. Performing a split ##

# Enter your code here.

private_incomes = income[income['workclass'] == 4]
public_incomes = income[income['workclass'] != 4]
print(private_incomes.head(), public_incomes.head())

## 8. Entropy ##

import math
# We'll do the same calculation we did above, but in Python.
# Passing 2 as the second parameter to math.log will take a base 2 log.
entropy = -(2/5 * math.log(2/5, 2) + 3/5 * math.log(3/5, 2))
print(entropy)

length = income.shape[0]
prob_high = sum(income['high_income'] == 1) / length
prob_low = sum(income['high_income'] == 0) / length
income_entropy = -(prob_high * math.log(prob_high, 2) + prob_low * math.log(prob_low, 2))
print(income_entropy)

## 9. Information gain ##

import numpy

def calc_entropy(column):
    """
    Calculate entropy given a pandas Series, list, or numpy array.
    """
    # Compute the counts of each unique value in the column.
    counts = numpy.bincount(column)
    # Divide by the total column length to get a probability.
    probabilities = counts / len(column)
    
    # Initialize the entropy to 0.
    entropy = 0
    # Loop through the probabilities, and add each one to the total entropy.
    for prob in probabilities:
        if prob > 0:
            entropy += prob * math.log(prob, 2)
    
    return -entropy

# Verify our function matches our answer from earlier.
entropy = calc_entropy([1,1,0,0,1])
print(entropy)

information_gain = entropy - ((.8 * calc_entropy([1,1,0,0])) + (.2 * calc_entropy([1])))
print(information_gain)

age_median = income['age'].median()
left_split = income[income['age'] <= age_median]['high_income']
right_split = income[income['age'] > age_median]['high_income']
income_entropy = calc_entropy(income['high_income'])
age_information_gain = income_entropy - (left_split.shape[0] / income.shape[0] * calc_entropy(left_split) + right_split.shape[0] / income.shape[0] * calc_entropy(right_split))
print(age_information_gain)

## 10. Finding the best split ##

def calc_information_gain(data, split_name, target_name):
    """
    Calculate information gain given a dataset, column to split on, and target.
    """
    # Calculate original entropy.
    original_entropy = calc_entropy(data[target_name])
    
    # Find the median of the column we're splitting.
    column = data[split_name]
    median = column.median()
    
    # Make two subsets of the data based on the median.
    left_split = data[column <= median]
    right_split = data[column > median]
    
    # Loop through the splits, and calculate the subset entropy.
    to_subtract = 0
    for subset in [left_split, right_split]:
        prob = (subset.shape[0] / data.shape[0]) 
        to_subtract += prob * calc_entropy(subset[target_name])
    
    # Return information gain.
    return original_entropy - to_subtract

# Verify that our answer is the same as in the last screen.
print(calc_information_gain(income, "age", "high_income"))

columns = ["age", "workclass", "education_num", "marital_status", "occupation", "relationship", "race", "sex", "hours_per_week", "native_country"]

information_gains = [calc_information_gain(income, c, 'high_income') for c in columns]

highest_gain = columns[information_gains.index(max(information_gains))]
print(highest_gain)