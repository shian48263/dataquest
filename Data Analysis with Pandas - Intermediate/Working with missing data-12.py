## 2. Finding the missing data ##

# Using the as keyword assigns the import to a different name, so we can reference it more easily
# In this case, instead of having to type pandas all the time, we can just type pd
import pandas as pd

# Read in the survival data
f = "titanic_survival.csv"
titanic_survival = pd.read_csv(f)

# Print out the age column
print(titanic_survival["age"])

# We can use the isnull function to find which values in a column are missing
age_null = pd.isnull(titanic_survival["age"])

# age_null is a boolean vector, and has "True" where age is NaN, and "False" where it isn't
null_true = age_null[age_null == True]
age_null_count = len(null_true)
print(type(null_true), type(age_null_count), age_null.sum(), len(age_null), len(null_true))

## 3. Whats the big deal with missing data? ##

import pandas as pd
mean_age = sum(titanic_survival["age"]) / len(titanic_survival["age"])

# Unfortunately, mean_age is NaN.  This is because any calculations we do with a null value also result in a null value.
# This makes sense when you think about it -- how can you add a null value to a known value?
print(mean_age)

# What we have to do instead is filter the missing values out before we compute the mean.
age_null = pd.isnull(titanic_survival["age"])
age_not_null = pd.notnull(titanic_survival['age'])
filtered_age = titanic_survival['age'].loc[age_not_null]
correct_mean_age = filtered_age.sum() / filtered_age.count()

## 4. Easier ways to do math ##

import pandas as pd

# This is the same value that we computed in the last screen, but it's much simpler.
# The ease of using the .mean() method is great, but it's important to understand how the underlying data looks.
correct_mean_age = titanic_survival["age"].mean()
correct_mean_fare = titanic_survival['fare'].mean()

## 5. Computing summary statistics ##

# Passengers are divided into classes based on the "pclass" column
# Passengers can be in first class (1), second class (2), or third class (3)
# Let's compute the average fare for each class
passenger_classes = [1, 2, 3]
fares_by_class = {}
for pclass in passenger_classes:
    fare_for_class = None
    # Insert code here to compute the average fare for pclass
    filtered = titanic_survival.loc[titanic_survival['pclass'] == pclass]
    fare_for_class = filtered['fare'].mean()
    # Assign the result to fare_for_class
    fares_by_class[pclass] = fare_for_class

## 6. Making pivot tables ##

import pandas as pd
import numpy as np

# Let's compute the survival change from 0-1 for people in each class
# The closer to one, the higher the chance people in that passenger class survived
# The "survived" column contains a 1 if the passenger survived, and a 0 if not
# The pivot_table method on a pandas dataframe will let us do this
# index specifies which column to subset data based on (in this case, we want to compute the survival percentage for each class)
# values specifies which column to subset based on the index
# The aggfunc specifies what to do with the subsets
# In this case, we split survived into 3 vectors, one for each passenger class, and take the mean of each
passenger_survival = titanic_survival.pivot_table(index="pclass", values="survived", aggfunc=np.mean)

# First class passengers had a much higher survival chance
print(passenger_survival)
passenger_age = titanic_survival.pivot_table(index="pclass", values='age', aggfunc=np.mean)

## 7. More complex pivot tables ##

import numpy as np

# This will compute the mean survival chance and the mean age for each passenger class
passenger_survival = titanic_survival.pivot_table(index="pclass", values=["age", "survived"], aggfunc=np.mean)
print(passenger_survival)

port_stats = titanic_survival.pivot_table(index='embarked', values=['age', 'survived', 'fare'], aggfunc=np.mean)

## 8. Drop missing values ##

import pandas as pd

# Drop all rows that have missing values
new_titanic_survival = titanic_survival.dropna()

# It looks like we have an empty dataframe now.
# This is because every row has at least one missing value.
print(new_titanic_survival)

# We can also use the axis argument to drop columns that have missing values
new_titanic_survival = titanic_survival.dropna(axis=1)
print(new_titanic_survival)

# We can use the subset argument to only drop rows if certain columns have missing values.
# This drops all rows where "age" or "sex" is missing.
new_titanic_survival = titanic_survival.dropna(subset=["age", "sex"])
print(new_titanic_survival)

new_titanic_survival = titanic_survival.dropna(subset=['age', 'body', 'home.dest'])

## 9. Row indices ##

# See the numbers to the left of each row?
# Those are row indexes.
# Since the data has so many columns, it is split into multiple lines, but there are only 5 rows.
print(titanic_survival.iloc[:5,:])


new_titanic_survival = titanic_survival.dropna(subset=["body"])
# Now let's print out the first 5 rows in new_titanic_survival
# The row indexes here aren't the same as in titanic_survival
# This is because we modified the titanic_survival dataframe to generate new_titanic_survival
# The row indexes you see here are the rows from titanic_survival that made it through the dropna method (didn't have missing values in the "body" column)
# They retain their original numbering, though
print(new_titanic_survival.iloc[:5,:])

# We've been using the .iloc method to address rows and columns
# .iloc works by position (row/column number)

# This code prints the fourth row in the data
print(new_titanic_survival.iloc[4,:])

# Using .loc instead addresses rows and columns by index, not position
# This actually prints the first row, because it has index 3
print(new_titanic_survival.loc[3,:])

row_index_25 = new_titanic_survival.loc[25,:]
row_position_fifth = new_titanic_survival.iloc[4,:]

## 10. Column indices ##

new_titanic_survival = titanic_survival.dropna(subset=["body"])

# This prints the value in the first column of the first row
print(new_titanic_survival.iloc[0,0])

# This prints the exact same value -- it prints the value at row index 3 and column "pclass"
# This happens to also be at row 0, index 0
print(new_titanic_survival.loc[3,"pclass"])

row_1100_age = new_titanic_survival.loc[1100,'age']
row_25_survived = new_titanic_survival.loc[25,'survived']

## 11. Reindex rows ##

# The indexes are the original numbers from titanic_survival
new_titanic_survival = titanic_survival.dropna(subset=["body"])
print(new_titanic_survival)

# Reset the index to an integer sequence, starting at 0.
# The drop keyword argument specifies whether or not to make a dataframe column with the index values.
# If True, it won't, if False, it will.
# We'll almost always want to set it to True.
new_titanic_survival = new_titanic_survival.reset_index(drop=True)
# Now we have indexes starting from 0!
print(new_titanic_survival)

titanic_reindexed = titanic_survival.dropna(subset=['age','boat']).reset_index(drop=True)

## 12. Use the apply function ##

import pandas as pd

# Let's look at a simple example.
# This function counts the number of null values in a series
def null_count(column):
    # Make a vector that contains True if null, False if not.
    column_null = pd.isnull(column)
    # Create a new vector with only values where the series is null.
    null = column[column_null == True]
    # Return the count of null values.
    return len(null)

# Compute null counts for each column
column_null_count = titanic_survival.apply(null_count)
print(column_null_count)

def not_null_count(column):
    column_not_null = pd.notnull(column)
    not_null = column[column_not_null == True]
    return(len(not_null))
column_not_null_count = titanic_survival.apply(not_null_count)
print(column_not_null_count)

## 13. Applying a function to a row ##

# This function will check if a row is an entry for a minor (under 18), or not.
def is_minor(row):
    if row["age"] < 18:
        return True
    else:
        return False

# This is a boolean series with the same length as the number of rows in titanic_survival
# Each entry is True if the row at the same position is a record for a minor
# The axis of 1 specifies that it will iterate over rows, not columns
minors = titanic_survival.apply(is_minor, axis=1)

def age_label(row):
    if pd.isnull(row['age']):
        return('unknown')
    else:
        if row['age'] < 18:
            return('minor')
        else:
            return('adult')
age_labels = titanic_survival.apply(age_label, axis=1)
print(age_labels)

## 14. Computing survival percentage by age group ##

# The titanic_survival variable now has the added column "age_labels", which is our age labels series from the last screen.
age_group_survival = titanic_survival.pivot_table(index='age_labels', values=['survived'], aggfunc=np.mean)
print(age_group_survival)