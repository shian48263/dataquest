## 2. Calculating differences ##

expected = 16280.5
female = 10771
male = 21790

female_diff = (female - expected) / expected
male_diff = (male - expected) / expected

print(female_diff, male_diff)

## 3. Updating the formula ##

expected = 16280.5
female = 10771
male = 21790

female_diff = (female - expected) ** 2 / expected
male_diff = (male - expected) ** 2 / expected
gender_chisq = female_diff + male_diff

print(gender_chisq)



from scipy.stats import chisquare

chisquare_value, pvalue = chisquare([21790, 10771], [expected, expected])
print(chisquare_value, pvalue)

## 4. Generating a distribution ##

import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline

expected = 16280.5
chi_squared_values = []

for _ in range(1000):
    genders = np.random.random(32561)
    males = 0
    females = 0
    for i in genders:
        if i < .5:
            males += 1
        else:
            females += 1
    chi_squared_values.append(((males - expected) ** 2 / expected) + ((females - expected) / expected))

plt.hist(chi_squared_values)
plt.show()

## 6. Smaller samples ##

female_diff = (107.71 - 162.805) ** 2 / 162.805
male_diff = (217.9 - 162.805) ** 2 / 162.805
gender_chisq = female_diff + male_diff
print(gender_chisq)

## 7. Sampling distribution equality ##

import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline

expected = 150
chi_squared_values = []

for _ in range(1000):
    ls = np.random.random(300)
    males = 0
    females = 0
    for i in ls:
        if i < 0.5:
            males += 1
        else:
            females += 1
    male_diff = (males - expected) ** 2 / expected
    female_diff = (females - expected) ** 2 / expected
    chi_squared_values.append(male_diff + female_diff)

plt.hist(chi_squared_values)
plt.show()

## 9. Increasing degrees of freedom ##

races = ['White', 'Black', 'Asian-Pac-Islander', 'Amer-Indian-Eskimo', 'Other']
observed = [27816, 3124, 1039, 311, 271]
expected = [26146.5, 3939.9, 944.3, 260.5, 1269.8]
races_chisq = []

for i, race in enumerate(races):
    observe = observed[i]
    expect = expected[i]
    races_chisq.append((observe - expect) ** 2 / expect)

race_chisq = sum(races_chisq)
print(race_chisq)

## 10. Using SciPy ##

from scipy.stats import chisquare
import numpy as np

observed = np.array([27816, 3124, 1039, 311, 271])
expected = np.array([26146.5, 3939.9, 944.3, 260.5, 1269.8])

race_chisquare_value, race_pvalue = chisquare(observed, expected)
print(race_chisquare_value, race_pvalue)