import math
import sqlite3
import pandas as pd

conn = sqlite3.connect('factbook.db')
facts = pd.read_sql_query('select * from facts', conn)
facts = facts.dropna(axis=0, subset=['area_land', 'population', 'population_growth'])
def estimate_pop(row, y):
    pop = row['population']
    pop_g = row['population_growth']
    return int(pop * (math.e ** ((pop_g/100) * y)))
facts['population_2050'] = facts.apply(lambda row: estimate_pop(row, 35), axis=1)
facts = facts.sort(columns='population_2050', ascending=False)
print(facts[['name', 'population_2050']].head(10))
conn.close()
