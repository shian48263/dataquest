## 2. College majors and employment ##

import pandas as pd

all_ages = pd.read_csv("all-ages.csv")
all_ages.head(5)

## 3. Summarizing major categories ##

import numpy as np
# All values for Major_category
print(all_ages['Major_category'].value_counts().index)

all_ages_major_categories = dict()
recent_grads_major_categories = dict()

all_ages_major_categories = all_ages.pivot_table(index='Major_category', values='Total', aggfunc=np.sum).to_dict()
recent_grads_major_categories = recent_grads.pivot_table(index='Major_category', values='Total', aggfunc=np.sum).to_dict()

## 4. Low wage jobs rates ##

low_wage_percent = 0.0
low_wage_percent = float(recent_grads['Low_wage_jobs'].sum()) / float(recent_grads['Total'].sum())

## 5. Comparing datasets ##

# All majors, common to both DataFrames
majors = recent_grads['Major'].value_counts().index

recent_grads_lower_emp_count = 0
all_ages_lower_emp_count = 0

for major in majors:
  if all_ages[all_ages['Major'] == major]['Unemployment_rate'].values[0] > recent_grads[recent_grads['Major'] == major]['Unemployment_rate'].values[0]:
    recent_grads_lower_emp_count += 1
  elif recent_grads[recent_grads['Major'] == major]['Unemployment_rate'].values[0] > all_ages[all_ages['Major'] == major]['Unemployment_rate'].values[0]:
    all_ages_lower_emp_count += 1