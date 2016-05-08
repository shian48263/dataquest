## 1. Introduction ##

import sqlite3
conn = sqlite3.connect("factbook.db")

query_plan_one = conn.execute('explain query plan select * from facts where population > 1000000 and population_growth < 0.05;').fetchall()
print(query_plan_one)
conn.close()

## 2. Query plan for multi-column queries ##

conn = sqlite3.connect("factbook.db")

conn.execute('create index if not exists pop_idx on facts(population);')
conn.execute('create index if not exists pop_growth_idx on facts(population_growth);')

query_plan_two = conn.execute('explain query plan select * from facts where population > 1000000 and population_growth < 0.05;').fetchall()
print(query_plan_two)
conn.close()

## 5. Creating a multi-column index ##

conn = sqlite3.connect("factbook.db")

conn.execute('create index if not exists pop_pop_growth_idx on facts(population, population_growth);')

query_plan_three = conn.execute('explain query plan select * from facts where population > 1000000 and population_growth < 0.05;').fetchall()
print(query_plan_three)

## 6. Covering index ##

conn = sqlite3.connect("factbook.db")
conn.execute("create index if not exists pop_pop_growth_idx on facts(population, population_growth);")

query_plan_four = conn.execute('explain query plan select population, population_growth from facts where population > 1000000 and population_growth < 0.05;').fetchall()
print(query_plan_four)
conn.close()

## 7. Covering index for single column ##

conn = sqlite3.connect("factbook.db")
conn.execute("create index if not exists pop_pop_growth_idx on facts(population, population_growth);")

query_plan_five = conn.execute('explain query plan select population from facts where population > 1000000;').fetchall()
print(query_plan_five)
conn.close()