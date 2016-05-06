## 1. Counting in Python ##

import sqlite3
conn = sqlite3.connect('factbook.db')
facts = conn.execute('select * from facts;').fetchall()
facts_count = len(facts)
print(facts_count)
conn.close()

## 2. Counting in SQL ##

conn = sqlite3.connect("factbook.db")
birth_rate_count = conn.execute('select count(birth_rate) from facts;').fetchall()[0][0]
print(birth_rate_count)
conn.close()

## 3. Min and max in SQL ##

conn = sqlite3.connect("factbook.db")
min_population_growth = conn.execute('select min(population_growth) from facts;').fetchall()[0][0]
print(min_population_growth)
max_death_rate = conn.execute('select max(death_rate) from facts;').fetchall()[0][0]
print(max_death_rate)
conn.close()

## 4. Sum and average in SQL ##

conn = sqlite3.connect("factbook.db")
total_land_area = conn.execute('select sum(area_land) from facts;').fetchall()[0][0]
print(total_land_area)
avg_water_area = conn.execute('select avg(area_water) from facts;').fetchall()[0][0]
print(avg_water_area)
conn.close()

## 5. Multiple aggregation functions ##

conn = sqlite3.connect("factbook.db")
query = 'select avg(population), sum(population), max(birth_rate) from facts;'
facts_stats = conn.execute(query).fetchall()
print(facts_stats)
conn.close()

## 6. Conditional aggregation ##

conn = sqlite3.connect("factbook.db")
population_growth = conn.execute('select avg(population_growth) from facts where population > 10000000;').fetchall()[0][0]
print(population_growth)
conn.close()

## 7. Selecting unique rows ##

conn = sqlite3.connect("factbook.db")
unique_birth_rates = conn.execute('select distinct birth_rate from facts;').fetchall()
print(unique_birth_rates)
conn.close()

## 8. Distinct aggregations ##

conn = sqlite3.connect("factbook.db")
average_birth_rate = conn.execute('select avg(distinct birth_rate) from facts where population > 20000000;').fetchall()[0][0]
print(average_birth_rate)
average_population = conn.execute('select sum(distinct population) from facts where area_land > 1000000;').fetchall()[0][0]
print(average_population)
conn.close()

## 9. Arithmetic in SQL ##

conn = sqlite3.connect("factbook.db")
population_growth_millions = conn.execute('select population_growth / 1000000.0 from facts;').fetchall()
print(population_growth_millions)
conn.close()

## 10. Arithmetic between columns ##

conn = sqlite3.connect("factbook.db")
conn = sqlite3.connect("factbook.db")
next_year_population = conn.execute('select population + (population_growth * population) from facts;').fetchall()
print(next_year_population)
conn.close()