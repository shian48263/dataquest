## 1. Probability basics ##

# Print the first two rows of the data.
print(flags[:2])

most_bars_country = flags['name'].loc[flags['bars'].idxmax()]
highest_population_country = flags['name'].loc[flags['population'].idxmax()]
print(most_bars_country, highest_population_country)

## 2. Calculating probability ##

total_countries = flags.shape[0]

orange_probability = len(flags[flags['orange'] == 1]) / total_countries
stripe_probability = len(flags[flags['stripes'] > 1]) / total_countries
print(orange_probability, stripe_probability)

## 3. Conjunctive probabilities ##

five_heads = .5 ** 5

ten_heads = .5 ** 10
hundred_heads = .5 ** 100
print(ten_heads, hundred_heads)

## 4. Dependent probabilities ##

# Remember that whether a flag has red in it or not is in the `red` column.
import numpy as np

def red_prob(n):
    p = (len(flags[flags['red'] == 1]) - n) / (flags.shape[0] - n)
    return(p)
three_red_prob = [red_prob(i) for i in range(3)]
three_red = np.prod(three_red_prob)
print(three_red)

## 5. Disjunctive probability ##

start = 1
end = 18000

hundred_prob_list = [i for i in range(start, end + 1) if (i % 100) == 0]
hundred_prob = len(hundred_prob_list) / 18000
print(hundred_prob)

seventy_prob_list = [i for i in range(start, end + 1) if (i % 70) == 0]
seventy_prob = len(seventy_prob_list) / 18000
print(seventy_prob)

## 6. Disjunctive dependent probabilities ##

stripes_or_bars = None
red_or_orange = None

red = len(flags[flags['red'] == 1])
orange = len(flags[flags['orange'] == 1])
red_orange = len(flags[(flags['red'] == 1) & (flags['orange'] == 1)])
red_or_orange = (red + orange - red_orange) / flags.shape[0]
print(red_or_orange)

stripes = len(flags[flags['stripes'] >= 1])
bars = len(flags[flags['bars'] >= 1])
stripes_bars = len(flags[(flags['stripes'] >= 1) & (flags['bars'] >= 1)])
stripes_or_bars = (stripes + bars - stripes_bars) / flags.shape[0]
print(stripes_or_bars)

## 7. Disjunctive probabilities with multiple conditions ##

heads_or = None

heads_or = 1 - (1/2) ** 3