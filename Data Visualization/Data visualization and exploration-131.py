## 1. Data exploration ##

import pandas as pd
recent_grads = pd.read_csv('recent-grads.csv')

print(recent_grads.columns)
recent_grads.head()

## 2. Histograms ##

import matplotlib.pyplot as plt

columns = ['Median','Sample_size']
recent_grads.hist(column=columns)

## 3. Customizing histograms ##

import matplotlib.pyplot as plt

columns = ['Median','Sample_size']

# Set the `layout` parameter as `(2,1)` so the graphs are displayed as 2 rows & 1 column 
# Then set `grid` parameter to `False`.
recent_grads.hist(column=columns, layout=(2,1), grid=False)

## 4. Practice: histograms ##

recent_grads.hist(column='Sample_size', bins=50)

## 5. Box plots ##

# Select just `Sample_size` & `Major_category` columns from `recent_grads` 
# Name the resulting DataFrame as `sample_size`
sample_size = recent_grads[['Sample_size', 'Major_category']]

# Run the `boxplot()` function on `sample_size` DataFrame and specify, as a parameter, 
# that we'd like a box and whisker diagram to be generated for each unique `Major_category`
sample_size.boxplot(by='Major_category')

# Format the resulting plot to make the x-axis labels (each `Major_category` value) 
# appear vertically instead of horizontally (by rotating 90 degrees)
plt.xticks(rotation=90)
plt.show()

## 7. Practice: box plots ##

recent_grads[['Sample_size', 'Major_category']].boxplot(by='Major_category')
plt.xticks(rotation=90)
plt.show()
recent_grads[['Total', 'Major_category']].boxplot(by='Major_category')
plt.xticks(rotation=90)
plt.show()

## 8. Multiple plots in one chart ##

# Plot Unemployment_rate on x-axis, Median salary on y-axis, in red
plt.scatter(recent_grads['Unemployment_rate'], recent_grads['Median'], color='red')
# Plot ShareWomen (Female % in major) on x-axis, Median salary on y-axis, in blue
plt.scatter(recent_grads['ShareWomen'], recent_grads['Median'], color='blue')
plt.show()

## 9. Practice: multiple plots in one chart ##

plt.scatter(recent_grads['Unemployment_rate'], recent_grads['P25th'], color='red')
plt.scatter(recent_grads['ShareWomen'], recent_grads['P25th'], color='blue')
plt.show()