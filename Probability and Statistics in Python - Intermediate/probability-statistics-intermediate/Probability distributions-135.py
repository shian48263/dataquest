## 3. Bikesharing distribution ##

import pandas
bikes = pandas.read_csv("bike_rental_day.csv")

prob_over_5000 = len(bikes['cnt'][bikes['cnt'] > 5000]) / bikes.shape[0]
print(prob_over_5000)

## 4. Computing the distribution ##

import math

# Each item in this list represents one k, starting from 0 and going up to and including 30.
outcome_counts = list(range(31))
def outcome_prob(n, k):
    comb = math.factorial(n) / (math.factorial(k) * math.factorial(n-k))
    p = 0.39
    q = 1 - p
    prob = (p ** k) * (q ** (n-k))
    return(comb * prob)
    
outcome_probs = [outcome_prob(outcome_counts[-1], i) for i in outcome_counts]
print(outcome_probs)

## 5. Plotting the distribution ##

import matplotlib.pyplot as plt

# The most likely number of days is between 10 and 15.
plt.bar(outcome_counts, outcome_probs)
plt.show()

## 6. Simplifying the computation ##

import scipy
from scipy import linspace
from scipy.stats import binom
import matplotlib.pyplot as plt

# Create a range of numbers from 0 to 30, with 31 elements (each number has one entry).
outcome_counts = linspace(0, 30, 31)
dist = binom.pmf(outcome_counts, 30, 0.39)
plt.bar(outcome_counts, dist)
plt.show()

## 8. Computing the mean of a probability distribution ##

dist_mean = None

n = 30
p = 0.39
dist_mean = n * p
print(dist_mean)

## 9. Computing the standard deviation ##

dist_stdev = None

n = 30
p = 0.39
q = 1 - p
dist_stdev = (n * p * q) ** (1/2)
print(dist_stdev)

## 10. A different plot ##

# Enter your answer here.
import scipy as sp
import matplotlib.pyplot as plt

outcome_counts = sp.linspace(0, 10, 11)
dist = sp.stats.binom.pmf(outcome_counts, 10, 0.39)
plt.bar(outcome_counts, dist)
plt.show()

outcome_counts = sp.linspace(0, 100, 101)
dist = sp.stats.binom.pmf(outcome_counts, 100, 0.39)
plt.bar(outcome_counts, dist)
plt.show()

## 11. The normal distribution ##

# Create a range of numbers from 0 to 100, with 101 elements (each number has one entry).
outcome_counts = scipy.linspace(0,100,101)

# Create a probability mass function along the outcome_counts.
outcome_probs = binom.pmf(outcome_counts,100,0.39)

# Plot a line, not a bar chart.
plt.plot(outcome_counts, outcome_probs)
plt.show()

## 12. Cumulative density function ##

outcome_counts = linspace(0, 30, 31)

import scipy as sp
import matplotlib.pyplot as plt
dist = sp.stats.binom.cdf(outcome_counts, 30, 0.39)
plt.plot(outcome_counts, dist)
plt.show()

## 14. Faster way to calculate likelihood ##

left_16 = None
right_16 = None

left_16 = binom.cdf(16, 30, 0.39)
right_16 = 1 - left_16
print(left_16, right_16)