## 2. Calculating expected values ##

males_over50k = .241 * .669 * 32561
males_under50k = .759 * .669 * 32561
females_over50k = .241 * .331 * 32561
females_under50k = .759 * .331 * 32561
print(.241 * .669 + .759 * .669 + .241 * .331 + .759 * .331)
print(males_over50k, males_under50k, females_over50k, females_under50k)

## 3. Calculating chi-squared ##

observed = [6662, 1179, 15128, 9592]
expected = [5249.8, 2597.4, 16533.5, 8180.3]
values = []

for i, obs in enumerate(observed):
    exp = expected[i]
    value = (obs - exp) ** 2 / exp
    values.append(value)

chisq_gender_income = sum(values)

print(chisq_gender_income)

## 4. Finding statistical significance ##

import numpy as np
from scipy.stats import chisquare

observed = [6662, 1179, 15128, 9592]
expected = [5249.8, 2597.4, 16533.5, 8180.3]

chisquare_value_gender_income, pvalue_gender_income = chisquare(observed, expected)
print(chisquare_value_gender_income, pvalue_gender_income)

## 5. Cross tables ##

import pandas as pd

table = pd.crosstab(income['sex'], [income['race']])
print(table)

## 6. Finding expected values ##

import numpy as np
import pandas as pd
from scipy.stats import chi2_contingency

table = pd.crosstab(income['sex'], [income['race']])
chisq_value, pvalue, df, expected = chi2_contingency(table)
print(chisq_value, pvalue, df, expected)

pvalue_gender_race = pvalue
print(pvalue_gender_race)