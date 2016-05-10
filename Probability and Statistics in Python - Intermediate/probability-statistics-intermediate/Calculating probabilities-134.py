## 2. Probability of renting bikes ##

import pandas
bikes = pandas.read_csv("bike_rental_day.csv")

# Find the number of days the bikes rented exceeded the threshold.
days_over_threshold = bikes[bikes["cnt"] > 2000].shape[0]
# Find the total number of days we have data for.
total_days = bikes.shape[0]

# Get the probability that more than 2000 bikes were rented for any given day.
probability_over_2000 = days_over_threshold / total_days
print(probability_over_2000)

probability_over_4000 = bikes[bikes['cnt'] > 4000].shape[0] / bikes.shape[0]
print(probability_over_4000)

## 4. Calculating probabilities ##

# Enter your code here.

coin_1_prob = (1/2) ** 3 * 3

print(coin_1_prob)

## 6. Calculating the number of combinations ##

sunny_1_combinations = None

sunny_1_combinations = 5

## 8. Finding the number of combinations ##

import math
def find_outcome_combinations(N, k):
    # Calculate the numerator of our formula.
    numerator = math.factorial(N)
    # Calculate the denominator.
    denominator = math.factorial(k) * math.factorial(N - k)
    # Divide them to get the final value.
    return numerator / denominator

combinations_7 = find_outcome_combinations(10, 7)

combinations_8 = find_outcome_combinations(10, 8)
combinations_9 = find_outcome_combinations(10, 9)
print(combinations_7, combinations_8, combinations_9)

## 10. Calculating the probability of one combination ##

prob_combination_3 = None

prob_combination_3 = .7 ** 3 * .3 ** 2
print(prob_combination_3)

## 12. Function to calculate the probability of a single combination ##

p = .6
q = .4

import math

def prob(n, k):
    return(p ** k * q ** (n-k))

def comb(N, k):
    # Calculate the numerator of our formula.
    numerator = math.factorial(N)
    # Calculate the denominator.
    denominator = math.factorial(k) * math.factorial(N - k)
    # Divide them to get the final value.
    return numerator / denominator

prob_8 = prob(10, 8) * comb(10, 8)
prob_9 = prob(10, 9) * comb(10, 9)
prob_10 = prob(10, 10) * comb(10, 10)
print(prob_8, prob_9, prob_10)